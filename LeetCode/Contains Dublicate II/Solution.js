let numbers = [1, 2, 3, 4, 1, 5, 4, 6, 7];
numbers = [0, 1, 2, 3, 4, 5, 0];
let k = 6;

function containsNearbyDublicates(numbers, k) {
  let n = numbers.length;

  let hashmap = new Map();

  for (let i = 0; i <= k; i++) {
    console.log("numbers[i] :>> ", numbers[i]);
    if (hashmap.has(numbers[i])) {
      console.log("hashmap, numbers[i], i :>> ", hashmap, numbers[i], i);
      return true;
    }

    if (numbers[i] !== undefined) hashmap.set(numbers[i], true);
  }

  for (let i = k + 1; i < n; i++) {
    hashmap.delete(numbers[i - k - 1]);

    if (hashmap.has(numbers[i])) {
      console.log("i, i-k+1 :>> ", i, i - k - 1);
      console.log("hashmap :>> ", hashmap);
      return true;
    }

    hashmap.set(numbers[i], true);
  }

  console.log("hashmap :>> ", hashmap);
  return false;
}

let result = containsNearbyDublicates(numbers, k);
console.log("result :>> ", result);
