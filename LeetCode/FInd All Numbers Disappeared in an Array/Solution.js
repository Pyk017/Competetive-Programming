let arr = [4, 3, 2, 7, 8, 2, 3, 1];
let n = arr.length;

function disappearingNumbers() {
  let map = new Map();

  let result = [];

  arr.forEach((item) => {
    map.set(item, (map.get(item) || 0) + 1);
  });

  for (let i = 1; i <= n; i++) {
    if (map.has(i)) continue;
    result.push(i);
  }

  return result;
}

let res = disappearingNumbers();
console.log("res :>> ", res);
