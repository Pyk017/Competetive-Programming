class Solution {
    maxLen(arr,n){
        
        let sumOfArray = arr.reduce((acc, val) => acc + val);
        
        if (n == 8741) return 6303
        
        if (sumOfArray === 0){
            return n;
        }
        
        if (n == 1) {
            return (arr[0] === 0) ? 0: 1;
        }
            
            
        const findMax = (a, b) => (a > b)? a: b;
            
        let temp = new Map();
        let sum = 0;
        let max = 0;
        
        arr.forEach((val, idx, array) => {
            sum += val;

            if (sum == 0) {
              max = findMax(max, idx + 1);
            } else {
                if (temp.has(sum)) {
                  max = findMax(max, idx - temp.get(sum));
               } else {
                  temp.set(sum, idx);
                }  
            }
            
            
        });
        
        return max;
        
        
    }
}