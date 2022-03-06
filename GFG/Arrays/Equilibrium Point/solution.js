
class Solution {
    // Function to find equilibrium point in the array.
    equilibriumPoint(a, n)
    {
        let sum_left = a.reduce((acc, val) => acc + val);
        
        let sum_right=0;
        // console.log(sum_left)
        let i = n - 1;
        
        while (i >= 0) {
            sum_left -= a[i];
            
            if (sum_left == sum_right) {
                return i + 1;
            }
            
            sum_right += a[i];
            
            i -= 1;
        }
        
        return -1;
        
    }
}