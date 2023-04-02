let nums1 = [4, 9, 5];
let nums2 = [9, 4, 9, 8, 4];

function _intersection(nums1, nums2) {
  let set = new Set(nums1);
  let result = [];

  for (let i = 0; i < nums2.length; i++) {
    if (!set.has(nums2[i])) continue;

    result.push(nums2[i]);
    set.delete(nums2[i]);
  }

  return result;
}

let result = _intersection(nums1, nums2);

console.log("result :>> ", result);
