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

    betterSolution(array, a, b) {
        let n = array.length;
        let [start, end, i] = [0, n - 1, 0]

        while(i <= end) {
            if (array[i] < a) {
                {
                    [array[i], array[start]] = [array[start], array[i]];
                    start += 1;
                    i += 1;
                }
            }
            else if (array[i] > b) {
                {
                    [array[i], array[end]] = [array[end], array[i]];
                    end -= 1;
                }   
            }
            else {
                i += 1;
            }
        }
    }


}