#include<bits/stdc++.h>
using namespace std;

// int series(int n){
//     if(n % 2 == 0)
//         return (n -2) / 2;
//     return n - 1;
// }

int numDecodings(string s) {
         int prev = 1, cur = 1;
        

         for (int i = 0; i < s.size(); ++i) {
             int next = [&] {
                 if (s[i] == '0') 
                     return i > 0 && (s[i-1] == '1' || s[i-1] == '2') ? prev : 0;
                 else
                     return i > 0 && ((s[i] <= '9' && s[i-1] == '1') || (s[i] <= '6' && s[i-1] == '2')) ? prev + cur : cur;
             }();
            
             prev = cur, cur = next;

         }
        
         return cur;
     }








int main(){
    string s;
    cin >> s;
    cout << numDecodings(s) << endl;
    // cout << "Enter a number :- " << " ";
    // cin >> n;
    // int res = series(n);
    // cout << res << endl;
    return 0;
}