class Solution {
  firstElementKTime(arr, n, k) {
    let obj = {};

    for (let i = 0; i < n; i++) {
      obj[arr[i]] = (obj[arr[i]] || 0) + 1;
      if (obj[arr[i]] == k) return arr[i];
    }

    return -1;
  }
}
