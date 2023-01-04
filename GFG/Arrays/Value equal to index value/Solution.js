class Solution {
  valueEqualToIndex(arr, n) {
    let res = [];
    let i = 1;

    while (i <= n) {
      if (i == arr[i - 1]) {
        res.push(arr[i - 1]);
      }
      i += 1;
    }

    return res;
  }
}

let { readFileSync } = require("fs");

let lines = readFileSync("./tc.txt", "utf-8").split(/\r?\n/);

let n = parseInt(lines.at(0));

let arr = lines
  .at(1)
  .trim()
  .split(" ")
  .map((x) => +x);

let obj = new Solution();

let result = obj.valueEqualToIndex(arr, n);

let r = result.join(" ");

console.log(r);
