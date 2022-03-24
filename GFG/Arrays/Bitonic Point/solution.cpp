// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;


 // } Driver Code Ends
//User function template for C++
class Solution{
public:
	
	int findMaximum(int arr[], int n) {
	    int i=0;
	    while(i < n - 1) {
	        if (arr[i] > arr[i + 1]) {
	            return arr[i]; 
	        }
	        i += 1;
	    }
	    
        return arr[n - 1];
	}

    int solution2(int arr[], int n) {
        if (n == 1) return 0;

        int left = 0, right = n - 1, mid = 0;

        while(left < right) {
            mid = left + (right - left) / 2;

            if (arr[mid] > arr[mid + 1]) {
                right = mid;
            }
            else {
                left = mid + 1;
            }
        }

        return arr[left];
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
    auto ans = ob.findMaximum(arr, n);
    cout << ans << "\n";
   
    return 0;
}