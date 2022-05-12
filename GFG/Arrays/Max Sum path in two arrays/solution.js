class Solution {
    
    max_path_sum(a, b, M, N){
        
        let [i, j, sumA, sumB] = [0, 0, 0, 0];
        let result = 0;
        
        let max = (a, b) => {
            return (a > b) ? a: b;
        }
        
        while (i < M && j < N) {
            
            if (a[i] == b[j]) {
                sumA += a[i];
                sumB += b[j];
                result += max(sumA, sumB);
                i++;
                j++;
                sumA = 0;
                sumB = 0;
                
            }
            
            if (a[i] < b[j]) {
                sumA += a[i];
                i += 1;
            }
            
            if (a[i] > b[j]) {
                sumB += b[j];
                j+= 1;
            }
        }
    
        while (i < M) {
            sumA += a[i];
            i++;
        }
        
        while (j < N) {
            sumB += b[j];
            j++;
        }
    
        return result + max(sumA, sumB);    
    }
}