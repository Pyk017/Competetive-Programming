class Solution {
    //Function to find triplets with zero sum.
    findTriplets(arr, n){
        arr.sort((a, b) => a - b);
        
        let [i, j, k, temp] = [0, 0, 0, 0];
        
        for(i = 0; i < n - 2; i++) {
            k = i + 1;
            j = n - 1;
            
            while (k < j) {
                temp = arr[i] + arr[k] + arr[j];
                if (temp == 0) {
                    return true;
                } else if (temp < 0) {
                    k += 1;
                } else {
                    j -= 1;
                }
            }
        }
        
        return false;
        
    }
}