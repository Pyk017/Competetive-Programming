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
