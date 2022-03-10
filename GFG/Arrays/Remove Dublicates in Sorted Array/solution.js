class Solution{
    remove_duplicate(arr,n){
        let [i, j, count] = [0, 0, 0];
        
        while (i < n) {
            while(i < n - 1 &&  arr[i] == arr[i + 1]) 
                i += 1;
                
            i += 1;
            j += 1;
            
            if (i < n && j <  n) 
                arr[j] = arr[i];
                
            count += 1;
        }
        
        return count;
    }
}