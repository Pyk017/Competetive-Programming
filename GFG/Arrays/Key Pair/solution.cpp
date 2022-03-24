// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Solution{
public:	
	// Function to check if array has 2 elements
	// whose sum is equal to the given value
	bool hasArrayTwoCandidates(int arr[], int n, int x) {
	    unordered_map<int, int> mp;
	  
	    for (int i=0; i<n; i++) {
	        mp[arr[i]] = i;
	    }
	    
	    for(int i=0; i<n; i++) {
	        if (mp.find(x - arr[i]) != mp.end()) {
	            if (mp[x - arr[i]] != i)
	                return true;
	        }
	    }
	    
	    return false;
	}

	bool keyPairMethod2(int arr[], int n, int x) {
		unordered_map<int, int> mp;

		int temp = 0;

		for (int i=0; i<n; i++) {
			temp = x - arr[i];

			if (mp.find(arr[i]) != mp.end()) {
				return true;
			} else {
				mp[temp] = arr[i];
			}
		}

		return false;
	}
};

int main() {
    
    int n, x;
    cin >> n >> x;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    Solution ob;
    auto ans = ob.hasArrayTwoCandidates(arr, n, x);
    cout << (ans ? "Yes\n" : "No\n");
    
    return 0;
}
