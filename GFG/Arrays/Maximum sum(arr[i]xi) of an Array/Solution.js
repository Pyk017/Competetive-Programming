class Solution {
  Maximize(arr, n) {
    let sortedArr = arr.sort((a, b) => parseInt(a) - parseInt(b));

    let result = sortedArr.reduce((acc, item, idx) => {
      return acc + idx * item;
    }, 0);

    return result % (Math.pow(10, 9) + 7);
  }
}
