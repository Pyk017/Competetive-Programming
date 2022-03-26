#include<bits/stdc++.h>
#include<stdlib.h>
#include<iostream>
using namespace std;

class Solution{
  public:
    //Function to find triplets with zero sum.
    bool findTriplets(int arr[], int n){ 
        sort(arr, arr + n);
        int i = 0;
        int k = i + 1;
        int j = n - 1;
        int temp = 0;

        for (int i=0; i < n - 2; i++) {
            k = i + 1;
            j = n - 1;
            while (k < j) {
                temp = arr[i] + arr[k] + arr[j];
                if (temp == 0){
                    return true;
                } else if (temp < 0) {
                    k += 1;
                } else {
                    j -= 1;
                }
            }
            
        }

        return false;
    
    }
};

int main(){
    
    int n;
    cin>>n;
    int arr[n]={0};
    for(int i=0;i<n;i++)
        cin>>arr[i];
    Solution obj;
    if(obj.findTriplets(arr, n))
        cout<<"1"<<endl;
    else 
        cout<<"0"<<endl;

    return 0;
}