#include <bits/stdc++.h>
using namespace std;

int transitionPoint(int arr[], int n);

int main() {
    int n;
    cin >> n;
    int a[n], i;
    for (i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << transitionPoint(a, n) << endl;
    return 0;
}

int transitionPoint(int arr[], int n) {
    int left=0, right=n-1;
    int mid = 0;
    
    if (arr[0] == 1) {
        return 0;
    }
    
    if (n == 1 && arr[0] == 0) {
        return -1;
    }
    
    while(left < right) {
        mid = int((left + right) / 2);
        // cout << mid << endl;
        
        if (arr[mid] == 1 && arr[mid - 1] == 0) {
            return mid;
        } 
        
        if (arr[mid] == 0 && arr[mid + 1] == 1) {
            return mid + 1;
        }
        
        if (arr[mid] == 0  && arr[mid + 1] == 0) {
            left = mid + 1;
        }
        
        
        else {
            right = mid - 1;
        }
        
    }
    
    return -1;
}