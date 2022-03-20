class Solution {
    firstRepeated(arr, n) {
        let current = n + 1;
        let map = {};
        
        arr.forEach((val, idx, array) => {
            if (val in map) {
                current = Math.min(current, map[val]);
            } else {
                map[val] = idx;
            }
        });
        
        return (current == n + 1) ? -1: current + 1;
    }
}