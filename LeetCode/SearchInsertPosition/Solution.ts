function searchInsert(nums: number[], target: number): number {
  let len = nums.length;
  let start = 0;
  let end = len - 1;
  let mid = 0;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);

    while (nums[mid] == target) return mid;

    if (nums[mid] > target) {
      end = mid - 1;
    }

    if (nums[mid] < target) {
      start = mid + 1;
    }
  }

  return start;
}
