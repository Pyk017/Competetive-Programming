class Solution {
  PalinArray(arr, n) {
    const isPalindrome = (num) =>
      num.toString() === num.toString().split("").reverse().join("");

    let result = arr.every((item) => isPalindrome(item));

    return result ? 1 : 0;
  }
}

let n = 5;
let arr = [111, 222, 333, 444, 555];

let obj = new Solution();
let res = obj.PalinArray(arr, n);
console.log("result :>> ", res);
