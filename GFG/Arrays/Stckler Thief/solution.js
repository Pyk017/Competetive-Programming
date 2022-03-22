class Solution
{
    //Function to find the maximum money the thief can get.
    findMaxSum(arr, n){ 
        let inc = 0, exc=0, temp = 0;
        
        let max = (a, b) => (a > b) ? a: b;
        
        arr.forEach((val, idx, array) => {
            temp = inc;
            inc = val + exc;
            exc = max(exc, temp);
        });
        
        return max(exc, inc);
        
    }
}