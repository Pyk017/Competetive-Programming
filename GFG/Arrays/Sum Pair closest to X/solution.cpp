#include <bits/stdc++.h>
using namespace std;

class Solution{   
public:
    vector<int> sumClosest(vector<int>arr, int x){
        int closest = INT_MAX;
        
        vector<int> close(2);
        int n = arr.size();
        int temp;
        
        int i = 0, j = n - 1;
        
        while (i < j) {
            temp = x - (arr[i] + arr[j]);
            
            if (abs(temp) < closest) {
                closest = abs(temp);
                close[0] = arr[i];
                close[1] = arr[j];
            }
            
            if (temp > 0) {
                i += 1;
            } 
            else if (temp < 0) {
                j -= 1;
            }
            else {
                close[0] = arr[i];
                close[1] = arr[j];
                return close;
            }
        }
        
        return close;
    }
};


int main() {
    int n, x;
    cin >> n >> x;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution ob;
    auto ans = ob.sumClosest(arr, x);
    cout << ans[0] << " " << ans[1] << "\n";
    
    return 0;
}