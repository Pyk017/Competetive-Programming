class Solution {
    findExtra(a,b,n){
        //code here
        let m = n - 1;
        for(let i = 0; i<n; i++) {
            if (a[i] != b[i]) return i;
            
            if(a[n-i-1] != b[m-i-1]) {
                return n - i - 1;
            }
        }
    }
}