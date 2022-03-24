class Solution {
    hasArrayTwoCandidates(arr,n,x){
        let map = new Map();
        let temp = 0;
        
        for(let i=0; i<n; i++) {
            temp = x - arr[i];
            
            if (map.has(arr[i])) {
                return true;
            } else {
                map.put(temp, arr[i]);
            }
        }
        
    }
}