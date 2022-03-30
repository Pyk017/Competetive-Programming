#include <bits/stdc++.h>
using namespace std;

class Solution{
public:

	void rearrange(int arr[], int n) {
	    vector<int> positive;
	    vector<int> negative;
	    
	    for(int i=0; i<n; i++) {
	        if (arr[i] >= 0) {
	            positive.push_back(arr[i]);
	        } else {
	            negative.push_back(arr[i]);
	        }
	    }
	    
	    int i=0, j=0, k=0;
	    int N = positive.size();
	    int M = negative.size();
	    
	    while (i < N and j < M) {
	        if (k % 2 == 0) {
	            arr[k] = positive[i];
	            i += 1;
	        } else {
	            arr[k] = negative[j];
	            j += 1;
	        }
	        k += 1;
	    }
	    
	    while(i < N) {
	        arr[k] = positive[i];
	        i += 1;
	        k += 1;
	    }
	    
	    while (j < M) {
	        arr[k] = negative[j];
	        j += 1;
	        k += 1;
	    }
	    
	    
	}
};


int main() {
    int n, i;
    cin >> n;
    int arr[n];
    for (i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution ob;
    ob.rearrange(arr, n);
    for (i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << "\n";
 
    return 0;
}