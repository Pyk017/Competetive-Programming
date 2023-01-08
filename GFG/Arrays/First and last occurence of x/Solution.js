class Solution {
  find(arr, n, x) {
    let result =
      arr.indexOf(x) != -1 ? [arr.indexOf(x), arr.lastIndexOf(x)] : [-1, -1];

    return result;
  }
}
