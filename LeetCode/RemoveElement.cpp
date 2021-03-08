#include<bits/stdc++.h>

using namespace std;

int removeElement(vector<int>& nums, int val) {
        int j = 0;
        for(int i=0; i<nums.size(); i++){
            if (nums[i] != val){
                nums[j++] = nums[i];
            }
        }
        return j;
}

int main(){
	int n;
	cin >> n;
	std::vector<int> v;
	int temp;
	for(int i=0; i<n; i++){
		cin >> temp;
		v.push_back(temp);
	}
	int value;
	cin >> value;
	int result = removeElement(v, value);
	cout << result<< endl;
	return 0;
}