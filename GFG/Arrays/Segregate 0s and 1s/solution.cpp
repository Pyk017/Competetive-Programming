#include <bits/stdc++.h>
using namespace std;

class Solution{   
public:
    void segregate0and1(int arr[], int n) {
        int i=0, a=0;
        int temp = 0;
        
        while (arr[i++] == 0);
        
        a = i - 1;
        
        for(int j = i; j < n; j++) {
            if (arr[j] == 0) {
                temp = arr[j];
                arr[j] = arr[a];
                arr[a] = temp;
                a += 1;
            }
        }
        
        
    }
};


int main() {    
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution ob;
    ob.segregate0and1(arr, n);
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
    return 0;
}