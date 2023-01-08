#include<bits/stdc++.h>

using namespace std;

vector<int> find(int arr[], int n, int x) {
    int start = -1, end = -1;

    vector<int> result;

    for(int i=0; i<n; i++) {
        if (arr[i] == x) {
            start = i;
            break;
        }
    }

    for(int j = n - 1; j>=0; j--) {
        if (arr[j] == x) {
            end = j;
            break;
        }
    }

    result.push_back(start);    
    result.push_back(end);

    return result;   
} 


int main() {
    int n;
    cin >> n;
    int x;
    cin >> x;

    int a[n];

    for (int i=0; i<n; i++) {
        cin >> a[i];
    }

    vector<int> res;

    res = find(a, n, x);

    cout << res[0] << " " << res[1] << endl;

    return 0;
}