 class Solution {

    convertToWave(arr, n){
        
        for (let i = 0; i<n - 1; i+=2) {
            {
                [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
            }    
        }
        
    }
}