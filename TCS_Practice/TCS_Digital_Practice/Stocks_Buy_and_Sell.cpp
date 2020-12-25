#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void stocks(int arr[], int n){
    if(n == 1)
        return;
        
    int i = 0;
    int buy = 0, sell=0;
    bool flag = false;
    while(i < n - 1){
        while((i < n - 1) && arr[i + 1] <= arr[i])
            i += 1;
        
        if(i == n - 1){
            if(!flag)
                cout << "No Profit" << " ";
            return ;
        }
        
        buy = i;
        i += 1;
        
        while((i < n) && arr[i] >= arr[i - 1])
            i += 1;
            
        sell = i - 1;
        
        cout << "(" << buy << " " << sell << ")" << " ";
        flag = true;
    }
    
}


int main() {
	int t;
	cin >> t;
	while(t--){
	    int n;
	    cin >> n;
	    int arr[n];
	    for(int i=0; i<n; i++)
	        cin >> arr[i];
	        
	    stocks(arr, n);
	    cout << endl;
	}
	return 0;
}