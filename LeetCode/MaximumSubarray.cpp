#include<bits/stdc++.h>

using namespace std;

int maxSubArray(vector<int>& nums) {
        int global_max = nums[0];
        int curr_max = nums[0];
        for(int i=1; i<nums.size(); i++){
            if(nums[i] > curr_max + nums[i]) curr_max = nums[i];
            else curr_max = curr_max + nums[i];
            
            if(global_max < curr_max) global_max = curr_max;
        }
        return global_max;
    }

int main(){
	int n;
	cin >> n;
	std::vector<int> v[n];
	for(int i=0; i<n; i++){
		cin >> v[i];
	}
	int result = maxSubArray(v);
	cout << result << endl;
	return 0;
}