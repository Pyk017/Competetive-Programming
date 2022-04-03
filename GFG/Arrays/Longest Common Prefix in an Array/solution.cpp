#include<bits/stdc++.h>
using namespace std;

class Solution{
  public:
    
    string longestCommonPrefix (string arr[], int N){
        
        if (N == 1) return arr[0];
        
        string first = arr[0];
        int mini = INT_MAX;
        string ans;
        int i, m;
        
        for(int j = 1; j < N; j++) {
            
            string word = arr[j];
            m = word.length();
            i = 0;
            
            while (i < m) {
                if (i >= first.length()) break;
                
                if (word[i] != first[i]) break;
                
                i += 1;
                
            }
            
            if (i == 0) return "-1";
            
            if ( i <= mini) {
                ans = word.substr(0, i);
                mini = i;
            }
            
            
        }
        
        return ans;
    
    }
};


int main(){

    int n; cin >> n;
    string arr[n];
    for (int i = 0; i < n; ++i)
        cin >> arr[i];
    
    Solution ob;
    cout << ob.longestCommonPrefix (arr, n) << endl;
    
}
