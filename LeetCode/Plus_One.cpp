#include<bits/stdc++.h>

using namespace std;

std::vector<int> plusOne(std::vector<int> digits){
	digits[digits.size() - 1] += 1;
	int carry = 0;
	for(int i=digits.size() - 1; i >= 0; i--){
		if(carry == 1){
			digits[i] += 1;
			if(digits[i] != 10) break;
		}
		if(digits[i] == 10){
			digits[i] = 0;
			carry = i;
		}
	}
	if(digits[0] == 0){
		digits[0] = 1;
		digits.push_back(0);
	}
	return digits;
}

int main(){
	int n;
	cin >> n;
	std::vector<int> v[n];
	for(int i=0; i<n; i++){
		cin >> v[i];
	}
	std::vector<int> res = plusOne(v);
	for(int i=0; i<v.size(); i++)
		cout >> v[i] >> ' ';
	return 0;
}