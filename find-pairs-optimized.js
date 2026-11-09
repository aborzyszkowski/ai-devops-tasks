function findPairs(arr, targetSum) {
  const pairs = [];
  const indicesByValue = new Map();

  for (let index = 0; index < arr.length; index++) {
    const indices = indicesByValue.get(arr[index]);
    if (indices) {
      indices.push(index);
    } else {
      indicesByValue.set(arr[index], [index]);
    }
  }

  for (let i = 0; i < arr.length; i++) {
    const matchingIndices = indicesByValue.get(targetSum - arr[i]);
    if (!matchingIndices) {
      continue;
    }

    let left = 0;
    let right = matchingIndices.length;
    while (left < right) {
      const middle = Math.floor((left + right) / 2);
      if (matchingIndices[middle] <= i) {
        left = middle + 1;
      } else {
        right = middle;
      }
    }

    for (let position = left; position < matchingIndices.length; position++) {
      const j = matchingIndices[position];
      if (arr[i] + arr[j] === targetSum) {
        pairs.push([arr[i], arr[j]]);
      }
    }
  }

  return pairs;
}

module.exports = findPairs;
