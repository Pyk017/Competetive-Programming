function missingNumber(nums: number[]): number {
  let n = nums.length;

  let totalSum = (n * (n + 1)) / 2;
  let sumArray = nums.reduce((a, v) => a + v);

  return totalSum - sumArray;
}
