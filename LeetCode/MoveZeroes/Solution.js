let data = [0, 1, 0, 4, 6, 8, 0, 0, 10, 0, 11];
// data = [0, 1, 0, 3, 12];
data = [0];
data = [1];
data = [1, 2, 3, 4];
let n = data.length;

console.log("data :>> ", data, data.length);

let j = 0;
let temp;

while (j < n && data[j] !== 0) j++;

console.log("j :>> ", j);

// while (j < n) {
//   let i = j;

//   while (i < n && data[i + 1] === 0) i++;

//   if (i + 1 >= n) break;

//   temp = data[i + 1];
//   data[i + 1] = data[j];
//   data[j] = temp;

//   j = j + 1;
// }

// console.log("data :>> ", data, data.length);
