class Solution{
    isSubset(a1, a2, n, m){
        let mp = new Map();
        
        for (let x of a1) {
            mp.set(x, 1);
        }
        
        
        for (let y of a2) {
            if (!mp.has(y)) {
                return "No";
            }
        }
        
        return "Yes";
        
    }
}