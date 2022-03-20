#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    // Function to return the count of the number of elements in
    // the intersection of two arrays.
    int NumberofElementsInIntersection(int a[], int b[], int n, int m) {
        int count = 0;
        set<int> s1;
        set<int> s2;
    
        
        for (int i=0; i<n; i++) {
            s1.insert(a[i]);
        }
        
        
        for (int j=0; j<m; j++) {
            if (s1.find(b[j]) != s1.end() && s2.find(b[j]) == s2.end()) {
                count += 1;
                s2.insert(b[j]);
            }
        }
        
        return count;
    }
};


int main() {
    int n, m;
    cin >> n >> m;
    int a[n], b[m];
    for (int i = 0; i < n; i++) cin >> a[i];

    for (int i = 0; i < m; i++) cin >> b[i];
    Solution ob;
    cout << ob.NumberofElementsInIntersection(a, b, n, m) << endl;
    
    return 0;
}  // } Driver Code Ends