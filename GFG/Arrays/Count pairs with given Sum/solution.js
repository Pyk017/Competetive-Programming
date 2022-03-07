class Solution {
    getPairsCount(arr,n,k){
        let count = 0;
        let temp;
        let map = arr.reduce((acc, val) => {
                acc[val] = acc[val] + 1 || 1;
                return acc;
            }, {});
            
        arr.forEach((val, idx, array) => { 
            temp = k - val;
            
            if (temp in map) {
                map[val] -= 1;
                count += map[temp]; 
            }
        });
        
        return count;
    }
}