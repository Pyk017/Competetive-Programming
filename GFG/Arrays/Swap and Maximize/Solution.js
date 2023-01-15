class Solution {
  maxSum(arr, n) {
    let [i, j] = [0, n - 1];
    arr.sort((a, b) => +a - +b);

    let result = 0;

    let flag = true;

    while (i < j) {
      if (flag) {
        result += Math.abs(arr[i] - arr[j]);
        i += 1;
      } else {
        result += Math.abs(arr[i] - arr[j]);
        j -= 1;
      }
    }

    result += Math.abs(arr[i] - arr[j]);

    return result;
  }
}
