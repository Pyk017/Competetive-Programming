#include<bits/stdc++.h>
using namespace std;
class Solution{
    public:
    void convertToWave(vector<int>& arr, int n){
         
        int temp;
        
        for (int i=0; i<n-1; i+=2) {
            temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
        
    }
};


int main()
{
    cin>>n; //input size of array
    vector<int> a(n); //declare vector of size n
    for(int i=0;i<n;i++)
        cin>>a[i]; //input elements of array
    Solution ob;
    ob.convertToWave(a, n);

    for(int i=0;i<n;i++)
        cout<<a[i]<<" "; //print array
        
    cout<<endl;
    
}