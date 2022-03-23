class Solution {
    
    countOddEven(arr,n){
        let ans = arr.reduce((acc, value) => {
            (value % 2) ? acc["countOdd"]++: acc["countEven"]++;
            return acc;
        }, {
            countOdd: 0,
            countEven: 0
        });
        
        console.log(ans["countOdd"], ans["countEven"]);
    }
}