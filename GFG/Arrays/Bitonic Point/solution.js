class Solution {
    
    findMaximum(arr,n){
        let i=0;
        
        while(i < n - 1 && arr[i] < arr[i + 1]) {
            i += 1;
        }
        
        return arr[i];
    }
}