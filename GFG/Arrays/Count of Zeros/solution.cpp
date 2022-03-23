#include <bits/stdc++.h>
using namespace std;
class Solution{   
public:
    int countZeroes(int arr[], int n) {
        if (arr[0] == 0) return n;
    
        for(int i = n - 1; i>= 0; i--) {
            if (arr[i] == 1) {
                return n - (i + 1);
            }
        }
        
        return 0;
    }
};


int main() {
    
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution ob;
    auto ans = ob.countZeroes(arr, n);
    cout << ans << "\n";
    
    return 0;
}
