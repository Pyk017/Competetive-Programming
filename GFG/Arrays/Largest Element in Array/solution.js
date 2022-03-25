class Solution {
    largest(arr, n) {
        let min = arr.reduce((acc, val) => {
            if (acc <= val) {
                acc = val;
            } 
            
            return acc;
        });
        
        return min;
    }
}