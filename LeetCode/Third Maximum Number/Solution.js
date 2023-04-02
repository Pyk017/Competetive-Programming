let arr = [6, 3, 0, 5];
arr = [6, 3, 0, 5, 0, 1, 7, 2];

arr = [1, 2, 2, 1];

function bubbleSort() {
  let n = arr.length;

  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      console.log("i, j, n - i - 1 :>> ", i, j, n - i - 1);
      if (arr[j] > arr[j + 1]) {
        {
          [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
        }
      }
    }
  }
}

console.log("before sorting arr :>> ", arr);

bubbleSort();

console.log("after sorting arr :>> ", arr);
