class Solution {
    longestCommonPrefix(arr,n){ 
        if (n == 1) return arr[0];
        
        let first = arr[0];
        let mini = Number.MAX_VALUE ;
        let ans = "";
        let [i, m] = [0, 0];
        
        
        for(let j = 1; j < n; j++) {
            let word = arr[j];
            i = 0;
            
            while (i < word.length) {
                if (i >= first.length) break;
                
                if (first[i] != word[i]) break;
                
                i += 1;
            }
            
            if (i === 0) return "-1";
            
            if (i <= mini) {
                ans = word.substring(0, i);
                mini = i;
            }
            
        }
        
        return ans;
    }
}