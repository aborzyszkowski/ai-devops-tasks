$DB_NAME = 'app_database'
$BACKUP_DIR = Join-Path $env:ProgramData 'db-backups'
$DATE = Get-Date -Format 'yyyyMMdd_HHmmss'
$FILENAME = Join-Path $BACKUP_DIR "${DB_NAME}_${DATE}.sql.gz"

$directoryExisted = Test-Path -LiteralPath $BACKUP_DIR
New-Item -ItemType Directory -Path $BACKUP_DIR -Force | Out-Null
if (-not $directoryExisted) {
    Write-Output "Utworzono katalog $BACKUP_DIR"
}

Write-Output "Rozpoczynam backup bazy $DB_NAME..."

$startInfo = New-Object System.Diagnostics.ProcessStartInfo
$startInfo.FileName = 'mysqldump'
$startInfo.Arguments = "-u root -p `"$DB_NAME`""
$startInfo.UseShellExecute = $false
$startInfo.RedirectStandardOutput = $true

$process = New-Object System.Diagnostics.Process
$process.StartInfo = $startInfo
$fileStream = $null
$gzipStream = $null
$processStarted = $false

try {
    if (-not $process.Start()) {
        throw 'Nie udało się uruchomić mysqldump.'
    }
    $processStarted = $true

    $fileStream = [System.IO.File]::Create($FILENAME)
    $gzipStream = New-Object -TypeName System.IO.Compression.GZipStream -ArgumentList $fileStream, ([System.IO.Compression.CompressionMode]::Compress)
    $process.StandardOutput.BaseStream.CopyTo($gzipStream)
    $gzipStream.Dispose()
    $gzipStream = $null
    $fileStream = $null

    $process.WaitForExit()
    if ($process.ExitCode -ne 0) {
        throw "mysqldump zakończył pracę z kodem $($process.ExitCode)."
    }

    Write-Output "Backup zakończony sukcesem: $FILENAME"
}
catch {
    $errorMessage = $_.Exception.Message
    if ($processStarted -and -not $process.HasExited) {
        $process.Kill()
        $process.WaitForExit()
    }
    if ($gzipStream) {
        $gzipStream.Dispose()
    }
    elseif ($fileStream) {
        $fileStream.Dispose()
    }
    if (Test-Path -LiteralPath $FILENAME) {
        Remove-Item -LiteralPath $FILENAME -Force
    }
    Write-Error "Błąd podczas wykonywania backupu: $errorMessage"
    exit 1
}
finally {
    if ($process) {
        $process.Dispose()
    }
}
