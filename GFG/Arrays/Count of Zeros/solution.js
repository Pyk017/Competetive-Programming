class Solution {
    countZeroes(arr, n) {
        if (arr[0] == 0) return n;
        
        for(let i = n - 1; i >= 0; i--) {
            if (arr[i] == 1) return n - (i + 1);
        }
        
        return 0;
    }
}