class Solution {
    threeWayPartition(array, a, b){
        let j=0;
        let n = array.length;
        
        for (let i = 0; i<n; i++) {
            if (array[i] < a) {
                {
                    [array[i], array[j]] = [array[j], array[i]];
                }
                j += 1;
            }
        }
        
        for (let i = j; i<n; i++) {
            if (array[i] >= a && array[i] <= b) {
                {
                    [array[i], array[j]] = [array[j], array[i]];
                }
                j += 1;
            }
        }
        
        for (let i = j; i<n; i++) {
            if (array[i] > b) {
                {
                    [array[i], array[j]] = [array[j], array[i]];
                }
                j += 1;
            }
        }
        
    }
}