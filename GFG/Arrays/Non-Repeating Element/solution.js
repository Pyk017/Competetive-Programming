class Solution{
    firstNonRepeating(arr,n){
        let dict = arr.reduce((acc, val) => {
            acc[val] = (acc[val] || 0) + 1;
            return acc;
        },{});
        
        let result = arr.filter(val => dict[val] == 1);
        // console.log(result);
        
        return (result.length) > 0 ? result[0]: 0;
    }
}