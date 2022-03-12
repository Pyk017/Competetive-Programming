class Solution {
    frequencyCount(arr,N,P){
       
       arr.forEach((val, idx) => {
           if (val > N) arr[idx] = 0
       });
       
       arr.forEach((val, i) => {
           if (arr[i] % (N + 1) > 0) {
               arr[(arr[i] % (N + 1)) -  1] += (N + 1);
           }
       });
       
       arr.forEach((val, i) => {
           arr[i] = Math.floor(arr[i] / (N + 1))
       })
       
       
    }
}