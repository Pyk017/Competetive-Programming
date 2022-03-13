#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    void rotateArr(int arr[], int d, int n){
        int temp[d];
        
        for(int i=0; i<d; i++) {
            temp[i] = arr[i];
        }
        
        for (int i=0; i<(n - d); i++) {
            arr[i] = arr[i + d];
        }
        
        int diff = n - d;
        
        for(int k = 0; k < d; k++) {
            arr[k + diff] = temp[k];
        }
        
        
    }
};


int main() {
    int n, d;
    
    //input n and d
    cin >> n >> d;
    
    int arr[n];
    
    //inserting elements in the array
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
    Solution ob;
    //calling rotateArr() function
    ob.rotateArr(arr, d,n);
    
    //printing the elements of the array
    for(int i =0;i<n;i++){
        cout << arr[i] << " ";
    }
    cout << endl;
    
    return 0;
}