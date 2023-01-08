class Solution {
  rotate(arr, n) {
    let i = n - 1;
    let temp = arr[i];

    while (i > 0) {
      arr[i] = arr[i - 1];
      i -= 1;
    }

    arr[0] = temp;
  }
}
