class Solution{
    allPairs(A, B, N, M, X){
        let res = [];
        
        let mp = new Map();
        
        for(let item of B) {
            mp.set(X - item, item);
        }
        
        // console.log(mp);
        
        for (let item of A) {
            if (mp.has(item)) {
                res.push([item, mp.get(item)]);
                // res[item] = mp.get(item);     
            }
        }

       res.sort((a, b) => a[0] - b[0]);
        
        return res;
        
    }
}