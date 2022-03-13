class Solution {
    rotateArr(arr, d, n){
        let temp = []
        
        for(let i=0; i<d; i++) temp.push(arr[i])
        
        for (let i=0; i<(n - d); i++){
            arr[i] = arr[i + d];
        }
        
        let j = n - d;
        
        for(let k = 0; k<d; k++) {
            arr[k + j] = temp[k];
        }
    }
}