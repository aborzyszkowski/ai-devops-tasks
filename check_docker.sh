#!/usr/bin/env bash

if ! command -v systemctl >/dev/null 2>&1; then
    echo "Błąd: systemctl nie jest dostępny. Ten skrypt wymaga systemu Linux z systemd."
    exit 1
fi

if systemctl is-active --quiet docker; then
    echo "Usługa Docker już działa."
    exit 0
fi

echo "Usługa Docker nie działa. Próbuję ją uruchomić..."

if ! sudo systemctl start docker; then
    echo "Błąd: nie udało się uruchomić usługi Docker."
    exit 1
fi

if systemctl is-active --quiet docker; then
    echo "Usługa Docker została uruchomiona."
    exit 0
fi

echo "Błąd: polecenie start zakończyło się, ale usługa Docker nadal nie działa."
exit 1
