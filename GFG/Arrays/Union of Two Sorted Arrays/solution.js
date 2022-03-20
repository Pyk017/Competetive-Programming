class Solution {
    //Function to return a list containing the union of the two arrays. 
    findUnion(arr1, arr2, n, m){
        let a = [...new Set(arr1)].sort((a, b) => a - b);
        let b = [...new Set(arr2)].sort((a, b) => a - b);
        let combine = [...new Set([...a, ...b])].sort((a, b) => a - b);
        return combine;
    }
}