#include<bits/stdc++.h>

using namespace std;

int maxProfit(vector<int> prices){
	int max_profit = 0;
	int min_price = INT_MAX;
	for(int i=0; i<prices.size(); i++){
		min_price = min(min_price, prices[i]);
		max_profit = max(max_profit, prices[i] - max_profit);
	}
	return max_profit;
}

int main(){
	int n;
	cin >> n;
	vector<int> v[n];
	for(int i=0; i<n; i++){
		cin >> v[i];
	}
	int result = maxProfit(v);
	cout << result << endl;
	return 0;
}