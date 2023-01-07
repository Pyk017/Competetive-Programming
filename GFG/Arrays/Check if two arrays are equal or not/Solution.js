class Solution {
  check(A, B, N) {
    let dict = A.reduce((acc, item) => {
      acc[item] = (acc[item] || 0) + 1;
      return acc;
    }, {});

    return B.every((item) => {
      return dict.hasOwnProperty(item) && dict[item]-- !== 0;
    });
  }
}
