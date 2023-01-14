function twoSum(nums: number[], target: number): number[] {
  let obj: object = {};
  for (let i = 0; i < nums.length; i++) {
    let temp = target - nums[i];
    if (obj[temp] !== undefined) {
      return [obj[temp], i];
    }
    obj[nums[i]] = i;
  }

  return [-1, -1];
}
