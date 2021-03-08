#include<bits/stdc++.h>
using namespace std;

int searchInsert(vector<int>& nums, int target) {
        int low=0, high = nums.size() - 1;
        while (low <= high){
            int mid = low + (high - low)/2;
            if(nums[mid] == target) return mid;
            else if (target > nums[mid]) low = mid + 1;
            else high = mid - 1;
        }
        return low;
        
    }


int main(){
	int n, target, temp;
	cin >> n;
	std::vector<int> v;
	for(int i=0; i<n; i++){
		cin >> temp;
		v.push_back(temp);
	}
	cin >> target;
	int result = searchInsert(v, target)
	cout << result << endl;
	return 0;
}