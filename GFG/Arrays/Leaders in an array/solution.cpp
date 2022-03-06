#include <bits/stdc++.h>
using namespace std;

class Solution{
    //Function to find the leaders in the array.
    public:
    vector<int> leaders(int a[], int n){
        // Code here
        vector<int> result;
        int temp = a[n - 1];
        int j = n - 2;
        result.push_back(temp);
        
        while(j >= 0) {
            if (a[j] >= temp) {
                result.push_back(a[j]);
                temp = a[j];
            }
            j -= 1;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};

int main()
{
  cin >> n;//total size of array
    
    int a[n];
    
    //inserting elements in the array
    for(long long i =0;i<n;i++){
        cin >> a[i];
    }
    Solution obj;
    //calling leaders() function
    vector<int> v = obj.leaders(a, n);
    
    //printing elements of the vector
    for(auto it = v.begin();it!=v.end();it++){
        cout << *it << " ";
    }
    
    cout << endl;

   
}