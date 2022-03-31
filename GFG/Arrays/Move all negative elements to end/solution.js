class Solution{
    segregateElements(arr,n){
        //code here
        let pos = arr.filter(val => val >= 0);
        let neg = arr.filter(val => val < 0);
        
        let [i, j] = [0, 0];
        
        while(i < pos.length) {
            arr[i] = pos[i];
            i += 1;
        }
        
        
        while (j < neg.length) {
            arr[i] = neg[j];
            i += 1;
            j += 1;
        }
        
    }
}