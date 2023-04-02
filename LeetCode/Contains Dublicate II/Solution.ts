//? Primary Solution
function containsNearbyDublicate(numbers: number[], k: number): boolean {
  let n = numbers.length;

  let hashmap = new Map();

  for (let i = 0; i <= k; i++) {
    if (hashmap.has(numbers[i])) return true;

    hashmap.set(numbers[i], true);
  }

  for (let i = k + 1; i < n; i++) {
    hashmap.delete(numbers[i - k - 1]);

    if (hashmap.has(numbers[i])) return true;

    hashmap.set(numbers[i], true);
  }

  return false;
}

//? Another solution
function containsNearbyDuplicate(numbers: number[], k: number): boolean {
  let n = numbers.length;
  let set = new Set();
  let leftmost: number = 0;

  for (let rightmost = 0; rightmost < numbers.length; rightmost++) {
    if (rightmost - leftmost > k) set.delete(numbers[leftmost++]);

    if (set.has(numbers[rightmost])) return true;

    set.add(numbers[rightmost]);
  }

  return false;
}
