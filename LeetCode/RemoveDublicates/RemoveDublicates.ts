function removeDuplicates(nums: number[]): number {
  let i = 0;

  for (let j = 1; j < nums.length; j++) {
    if (nums[i] != nums[j]) {
      i += 1;
      nums[i] = nums[j];
    }
  }

  return i + 1;
}
