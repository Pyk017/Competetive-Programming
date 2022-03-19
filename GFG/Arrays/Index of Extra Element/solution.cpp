// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
  public:
    int findExtra(int a[], int b[], int n) {
        // add code here.
        int m = n - 1;
        for(int i=0; i<n; i++) {
            
            if(a[i] != b[i]) return i;
            
            
            if (a[n - i - 1] != b[m - i - 1]) {
                return n - i - 1;
            }
        }
    }
};

// { Driver Code Starts.
int main() {    
    int n;
    cin >> n;
    int a[n], b[n - 1];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < n - 1; i++) {
        cin >> b[i];
    }
    Solution obj;
    cout << obj.findExtra(a, b, n) << endl;

}  // } Driver Code Ends