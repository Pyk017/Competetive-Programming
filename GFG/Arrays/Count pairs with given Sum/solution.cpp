#include <bits/stdc++.h>
using namespace std;

class Solution{   
public:
    int getPairsCount(int arr[], int n, int k) {
        int sum = 0;
        int count = 0;
        
        for(int i=0; i<n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] + arr[j] == k) {
                    count += 1;
                }
            }
        }
        
        return count;
    }
};



int main() {

    int n, k;
    cin >> n >> k;
    int arr[n];

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    Solution ob;
    auto ans = ob.getPairsCount(arr, n, k);
    cout << ans << "\n";

    
    return 0;
} 