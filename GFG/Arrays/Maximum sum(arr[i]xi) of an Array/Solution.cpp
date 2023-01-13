#include <bits/stdc++.h>
using namespace std;

class Solution {
    public: 
        int Maximize(int[] a, int n) {
            sort(a, a + n);

            long long result = 0;
            int mod = 1e9 + 7;

            for(int i = 0; i < n; i++) {
                result = (result + ((long)a[i] * i)) % mod;
            }

            return (int)result%mod;
        }
}

int main() {

    int n;
    cin >> n;
    int a[n];
    for (int i=0; i<n; i++)
        cin >> a[i];

    Solution ob;
    cout << ob.Maximize(a, n) << endl;
    
    return 0;
}