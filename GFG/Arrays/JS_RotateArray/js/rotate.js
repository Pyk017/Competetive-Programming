function rotate(arr, d) {
  let res = Array(arr.length).fill(0);
  arr.forEach((val, idx, array) => {
    res[idx] = array[(idx + d) % res.length];
  });
  return res;
}

function rotateReverse(arr, d) {
  let firstHalf = arr.splice(0, d);
  return [...arr, ...firstHalf];
}

export { rotate, rotateReverse };
