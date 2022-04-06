class Solution {

    findSwapValues(A,n,B,m){
        A.sort((a, b) => a - b);
        B.sort((a, b) => a - b);
        
        let sum_a = A.reduce((acc, val) => acc + val);
        let sum_b = B.reduce((acc, val) => acc + val);
        
        let [i, j] = [0, 0];
        
        while (i < n && j < m) {
            let x = sum_a - A[i] + B[j];
            let y = sum_b - B[j] + A[i];
            
            if (x == y) return 1;
            
            if ( x > y ) {
                i += 1;
            }
            
            else {
                j += 1;
            }
        }
        
        return -1;
        //code here
    }
}