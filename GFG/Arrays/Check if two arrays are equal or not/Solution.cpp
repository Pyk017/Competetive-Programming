#include<bits/stdc++.h>
#include<map>
using namespace std;

#define ll long long

class Solution{
    public:
    bool check(vector<ll> A, vector<ll> B, int N) {
        map<int, int> mp;
        for (int i=0; i<N; i++) {
            if (mp.count(A[i]) > 0) {
                mp[A[i]] += 1;
            } else {
                mp[A[i]] = 1;
            }
        }
        
        for (int i=0; i<N; i++) {
            if(mp.count(B[i]) == 0 || mp[B[i]] == 0) return false;
            
            mp[B[i]] -= 1;
        }
        
        return true;
    }
};


int main() {
    int n;
    cin>>n;
    
    vector<ll> arr(n,0), brr(n,0);
    
    for(ll i=0;i<n;i++)
        cin >> arr[i];
    
    for(ll i=0;i<n;i++)
        cin >> brr[i];
    
    Solution ob;
    cout << ob.check(arr,brr,n) << "\n";
    return 0;
}