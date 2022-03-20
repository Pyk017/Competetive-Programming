// { Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
// User function template in C++

class Solution {
  public:
    // Function to return the position of the first repeating element.
    int firstRepeated(int arr[], int n) {
        int current = n + 1;
        unordered_map<int, int> mp;
        
        for (int i=0; i<n; i++) {
            if (mp.find(arr[i]) != mp.end() ) {
                current = min(current, mp[arr[i]]);
            } else {
                mp[arr[i]] = i;
            }
        }

        if (current == n + 1) {
            return -1;
        }
        
        return current + 1;
    }
};

int main() {

    int n;
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; ++i) cin >> arr[i];
    Solution ob;
    cout << ob.firstRepeated(arr, n) << "\n";

    return 0;
}