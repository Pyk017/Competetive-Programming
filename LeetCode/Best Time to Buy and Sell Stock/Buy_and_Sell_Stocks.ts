function maxProfit(prices: number[]): number {
  let maximumProfit = 0;

  for (let i = 0; i < prices.length; i++) {
    let idx = getMax(prices, i);

    let j = i;

    while (j < idx) {
      maximumProfit = Math.max(prices[idx] - prices[j], maximumProfit);
      j += 1;
    }

    i = j;
  }

  return maximumProfit;
}

function getMax(arr: number[], start: number): number {
  let maxi = -1;
  let idx = -1;

  for (let i = start; i < arr.length; i++) {
    if (arr[i] > maxi) {
      maxi = arr[i];
      idx = i;
    }
  }

  return idx;
}
