let pascal = function (value) {
  triangle = [];
  triangle.push([1]);
  for (let i = 1; i < value; i++) {
    triangle[i] = [];
    triangle[i].push(1);
    for (let j = 1; j < i; j++) {
      triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
    }
    triangle.push(1);
  }
  return triangle;
};

let readline = require("readline");
let read = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

read.question("", function (value) {
  let result = pascal(value);
  console.log(result);
  read.close();
});

read.close("", function () {
  process.exit();
});
