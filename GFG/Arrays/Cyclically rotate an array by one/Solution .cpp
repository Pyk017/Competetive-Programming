#include<bits/stdc++.h>
using namespace std;

void rotate(int arr[], int n) {   
    int i = n - 1;
    int temp = arr[i];
    
    while (i > 0) {
        arr[i] = arr[i - 1];
        i -= 1;
    }
    arr[0] = temp;
    
}


int main() {
    int n;
    cin >> n;
    int a[n], i;

    for (i = 0;  i < n; i++) {
        cin >> a[i];
    }

    rotate(a, n);

    for (i = 0; i < n; i++) {
        cout << a[i] << " ";
    }

    cout << endl;
}