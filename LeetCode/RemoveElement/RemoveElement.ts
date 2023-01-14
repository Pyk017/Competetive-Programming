function removeElement(nums: number[], val: number): number {
  let i = nums.length - 1;
  let j = i;

  while (i >= 0) {
    if (nums[i] === val) {
      {
        [nums[i], nums[j]] = [nums[j], nums[i]];
      }
      j -= 1;
    }

    i -= 1;
  }

  return j + 1;
}
