class Solution {
    
    duplicates(a, n)
    {
        let result = [];
        
        let temp = Array(n).fill(0);
        temp.forEach((val, idx, array) => {
            // console.log(val, idx, array);
            array[a[idx]] += 1; 
        });
        // let temp = Array(n).fill(0);
        // console.log(temp)
        
        temp.forEach((val, idx, array) => {
            if (val > 1) result.push(idx)
        });
        
        let res =  (result.length == 0) ? [-1]: result;
        return res;
    }
}


let a = [0, 1, 3, 2]
let n = a.length;
let obj = new Solution()
let res = obj.duplicates(a, n);
console.log(res);