
class Solution {
    
    peakElement(arr, n)
    {
        // code here
        if (n == 1) return 0;
        for(let i=0; i<n; i++) {
        
        if (i == 0 && arr[i] > arr[i + 1]) {
            // printf("in firstone");
            return i;
        }
        
        if (i == n - 1 && arr[i] > arr[i - 1]) {
            // printf("in secondone");
            return i;
        }
        
        if (arr[i] > arr[i + 1] && arr[i] > arr[i - 1]) {
            // printf("in thirdone");
            return i;
        }
    }
    
   
   return 0;
    }
}