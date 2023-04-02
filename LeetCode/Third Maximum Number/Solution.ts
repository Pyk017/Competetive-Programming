function thirdMax(nums: number[]): number {
  let n = nums.length;

  let setArr = new Set(nums);

  nums = Array.from(setArr);

  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        {
          [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
        }
      }
    }
  }

  if (nums.length < 3) {
    return nums[nums.length - 1];
  } else {
    return nums[nums.length - 3];
  }
}
