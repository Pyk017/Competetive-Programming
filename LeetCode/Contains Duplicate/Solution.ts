function containsDuplicate(nums: number[]): boolean {
  let map = {};

  for (const num of nums) {
    if (map.hasOwnProperty(num)) return true;
    else {
      map[num] = "true";
    }
  }

  return false;
}
