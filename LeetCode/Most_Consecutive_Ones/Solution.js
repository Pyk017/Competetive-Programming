let nums = [0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0];
nums = [1, 1, 0, 1];
function findMaxZeroes() {
  let current = 0;
  let finalMax = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 0) {
      current = 0;
    } else {
      current += 1;

      if (current > finalMax) {
        finalMax = current;
      }
    }
  }

  return finalMax;
}

let result = findMaxZeroes();
console.log("result :>> ", result);
