class Solution {
    // Function to return the count of the number of elements in
    // the intersection of two arrays.
    NumberofElementsInIntersection(a, b, n, m) {
        let s1 = new Set(a);
        let s2 = new Set();
        let count = 0;
        
        for (let i=0; i<m; i++) {
            if (s1.has(b[i]) && !s2.has(b[i])) {
                count += 1;
                s2.add(b[i]);
            }
        }
        
        return count;
    }
}