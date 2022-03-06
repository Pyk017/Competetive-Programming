class Solution {
    //Function to find the leaders in the array.
    leaders(arr, n){
        let result = []
        let j = n - 2;
        let temp = arr[n - 1]
        
        result.push(temp)
        
        while(j >= 0){
            if (arr[j] >= temp) {
                result.push(arr[j]);
                temp = arr[j];
            }
            j -= 1;
        }
        
        return result.reverse();
        
    }
}