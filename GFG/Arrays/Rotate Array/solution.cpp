#include<bits/stdc++.h>
using namespace std;

class Solution{
    public:
    
    void rotateArr(int arr[], int d, int n){
        int temp;
    
        for (int i=0; i<n; i++) {
            temp = arr[i];
            arr[i] = arr[(i + d) % n];
            arr[(i + d) % n] = arr[n - d];
            arr[n - d] = temp;
        }
        
        // for(int i=0; i<n; i++) {
        //     cout << arr[i] << " ";
        // }
        // cout << endl;
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
