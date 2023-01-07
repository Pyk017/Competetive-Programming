class Solution {
  reverseInGroups(arr, n, k) {
    let i = 0;
    while (i < n) {
      let [start, end] = [i, Math.min(i + k - 1, n - 1)];
      this.reverse(arr, start, end);
      i += k;
    }
  }

  reverse(arr, x, y) {
    while (x <= y) {
      {
        [arr[x++], arr[y--]] = [arr[y], arr[x]];
      }
    }
  }
}
