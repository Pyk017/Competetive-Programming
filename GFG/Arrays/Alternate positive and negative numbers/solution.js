class Solution{
    rearrange(arr,n){
        let positive = arr.filter(val => val >= 0);
        let negative = arr.filter(val => val < 0);
        
        let [i, j, k] = [0, 0, 0];
        let [N, M] = [positive.length, negative.length];
        
        while (i < N && j < M) {
            if (k % 2 === 0) {
	            arr[k] = positive[i];
	            i += 1;
	        } else {
	            arr[k] = negative[j];
	            j += 1;
	        }
	        k += 1;
        }
        
        while(i < N) {
	        arr[k] = positive[i];
	        i += 1;
	        k += 1;
	    }
	    
	    while (j < M) {
	        arr[k] = negative[j];
	        j += 1;
	        k += 1;
	    }
        
        return arr
    }
}