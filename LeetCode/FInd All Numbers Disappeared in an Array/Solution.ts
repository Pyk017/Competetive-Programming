function findDisappearedNumbers(nums: number[]): number[] {
  let map = new Map();
  let n = nums.length;
  let result: number[] = [];

  for (let i = 0; i < n; i++) {
    if (map.has(nums[i])) {
      map.set(nums[i], map.get(nums[i]) + 1);
    } else {
      map.set(nums[i], 1);
    }
  }

  for (let i = 1; i <= n; i++) {
    if (!map.has(i)) {
      result.push(i);
    }
  }

  return result;
}
