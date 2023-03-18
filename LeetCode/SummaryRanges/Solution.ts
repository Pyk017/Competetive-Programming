function summaryRanges(nums: number[]): string[] {
  let result: string[] = [];

  let i = 0;
  let n = nums.length;

  for (i = 0; i < n; i++) {
    let j = i;
    while (j + 1 < n && nums[j + 1] === nums[j] + 1) j += 1;

    if (i == j) result.push(nums[i].toString());
    else {
      result.push(`${nums[i]}-> ${nums[j]}`);
      i = j;
    }
  }

  return result;
}
