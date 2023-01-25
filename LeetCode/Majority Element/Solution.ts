// Boyer–Moore majority vote algorithm

function majorityElementUsingAlgorithm(nums: number[]): number {
  let winner = nums[0];
  let votes = 0;
  for (const candidate of nums) {
    if (candidate === winner) {
      votes += 1;
    } else if (votes > 1) {
      votes -= 1;
    } else {
      winner = candidate;
      votes = 1;
    }
  }
  return winner;
}

function majorityElement(nums: number[]): number {
  let count = 0;
  let len = nums.length;

  nums.sort((a, b) => +a - +b);

  for (let i = 0; i < len; i++) {
    count = 1;

    while (i < len - 1 && nums[i] === nums[i + 1]) {
      i += 1;
      count += 1;
    }

    if (count > Math.floor(len / 2)) {
      return nums[i];
    }
  }
  return nums[0];
}
