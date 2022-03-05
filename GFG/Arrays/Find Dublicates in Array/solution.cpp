// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
  public:
    vector<int> duplicates(int arr[], int n) {
        
        vector<int> result;
        
        int temp[n] = {0};
        
        for(int i=0; i<n; i++) {
            temp[arr[i]] += 1;
        }
        
        
        for(int i=0; i<n; i++) {
            if (temp[i] > 1) {
                result.push_back(i);
            }
        }
        
        if (result.empty()){
          result.push_back(-1);
          return result;
        } 
        
        return result;
    }
};


// { Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t-- > 0) {
        int n;
        cin >> n;
        int a[n];
        for (int i = 0; i < n; i++) cin >> a[i];
        Solution obj;
        vector<int> ans = obj.duplicates(a, n);
        for (int i : ans) cout << i << ' ';
        cout << endl;
    }
    return 0;
}
  // } Driver Code Ends