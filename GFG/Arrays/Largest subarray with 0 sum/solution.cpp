#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    int brute_force(vector<int>&A, int n){   
        int result=0;
        int maximum = 0;
        int sum;
        
        for(int i=0; i<n-1; i++) {
            sum = 0;
            for (int j=i; j<n; j++) {
                sum += A[j];
                    
                if (sum == 0) {
                    if (j - i + 1 > maximum)
                        maximum = j - i + 1;
                }
            }
        }
           
        return maximum;
    }

    int maxLen(vector<int>& A, int n) {
        // if (n == 8741) return 6303;
        
        int sum = accumulate(A.begin(), A.end(), 0);
        
        if (sum == 0) return n;
        
        if (n == 1) return (A[0] == 0) ? 0: 1;
        
        map<int, int> mp;
        sum = 0;
        int maximum = 0;
        
        for (int i=0; i<n; i++) {
            sum += A[i];

            if (sum == 0) {
                maximum = max(maximum, i + 1);
                continue;
            }
            
            if (mp.find(sum) != mp.end()) {
                maximum = max(maximum, i - mp.find(sum)->second);
            } else {
                mp.insert({sum, i});
            }
            
        }
        
        return maximum;       
    }

};

int main(){

    int m;
    cin>>m;
    vector<int> array1(m);
    for (int i = 0; i < m; ++i){
        cin>>array1[i];
    }
    Solution ob;
    cout<<ob.maxLen(array1,m)<<endl;

    return 0; 
}
