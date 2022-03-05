#include <bits/stdc++.h>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

class Solution {

	public:
		vector<int> subarraySum(int arr[], int n, long long s){
		 	vector<int> result;
	        int currentSum = arr[0], start = 0;
	        
	        for (int i=1; i<n + 1; i++) {
	            while(currentSum > s && start < i - 1) {
	                currentSum -= arr[start];
	                start += 1;
	            }
	            
	            if (currentSum == s) {
	                result.push_back(start + 1);
	                result.push_back(i);
	                return result;
	            }
	            
	            if (i < n){
	                currentSum += arr[i];
	            }
	            
	        }
	        
	        result.push_back(-1);
	        return result;

		}
};


int main() {

	int n;
	long long s;
	cin >> n >> s;
	int arr[n];
	
	for(int i=0; i<n; i++){
		cin >> arr[i];
	}

	Solution ob;
	vector<int> res;
	res = ob.subarraySum(arr, n, s);

	for(int i=0; i<res.size(); i++) {
		cout << res[i] << " ";
	}
	cout << endl;

	return 0;
}
