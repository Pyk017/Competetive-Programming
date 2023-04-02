function moveZeroes(nums: number[]): void {
  let temp = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      [nums[i], nums[temp]] = [nums[temp], nums[i]];
      temp += 1;
    }
  }
}
