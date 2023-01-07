#include<bits/stdc++.h>
using namespace std;

class Solution{
public:
      void reverseInGroups(vector<long long>& arr, int n, int k){
        int i = 0;
        while (i < n) {
            
            int start = i;
            int end = min(i + k -1, n - 1);
            
            while (start < end) {
                swap(arr[start++], arr[end--]);
            }
            
            i += k;
        }
    }
};


int main() {
    int n;
        cin >> n; 
        vector<long long> arr; 
        int k;
        cin >> k; 

        for(long long i = 0; i<n; i++)
        {
            long long x;
            cin >> x; 
            arr.push_back(x); 
        }
        Solution ob;
        ob.reverseInGroups(arr, n, k);
        
        for(long long i = 0; i<n; i++){
            cout << arr[i] << " "; 
        }
        cout << endl;
    return 0;
}

