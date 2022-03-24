class Solution {

    segregate0and1(arr,n){
        
        let [i, a, temp] = [0, 0, 0];
        
        while(arr[i++] == 0);
        
        a = i - 1;
        
        for(let j = i; j < n; j++) {
            if (arr[j] == 0) {
                {
                    [arr[j], arr[a]] = [arr[a], arr[j]];
                }
                
                a += 1;
            }
        }
        
    }
}