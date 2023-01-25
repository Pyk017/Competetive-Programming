#include<bits/stdc++.h>

using namespace std;

bool containsDuplicate(vector<int> nums){
	return nums.size() > set<int>(nums.begin(), nums.end()).size();
}

int main(){
	int n;
	cin >> n;
	vector<int> v[n];
	for(int i=0; i<n; i++)
		cin >> v[n];

	bool result = containsDuplicate(v);
	cout << result << endl;
	return 0;
}