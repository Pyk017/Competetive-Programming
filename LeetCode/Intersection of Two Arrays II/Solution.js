let nums1 = [4, 9, 5];
let nums2 = [9, 4, 9, 8, 4];

function intersection(nums1, nums2) {
  let res = [];

  let map = new Map();

  nums1.map((num) => {
    if (map.has(num)) {
      map.set(num, map.get(num) + 1);
    } else {
      map.set(num, 1);
    }
  });

  nums2.map((num) => {
    if (!map.has(num)) return;

    res.push(num);

    if (map.get(num) === 1) {
      map.delete(num);
    } else {
      map.set(num, map.get(num) - 1);
    }
  });

  return res;
}

let result = intersection(nums1, nums2);
console.log("result :>> ", result);
