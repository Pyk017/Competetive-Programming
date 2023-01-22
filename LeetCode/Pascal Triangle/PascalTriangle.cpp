#include<bits/stdc++.h>

using namespace std;

vector<vector<int>> generate(int numRows){
	vector<vector<int>> m(numRows);

	for(int i=0; i<numRows; i++){
		m[i].resize(i + 1);
		m[i][0] = m[i][i] = 1;

		for(int j = 1; j<i; j++)
			m[i][j] = m[i - 1][j - 1] + m[i - 1][j];
	}
	return m;
}

void print(vector<vector<int>> v){
	for(auto ptr = v.begin(); ptr < v.end(); ptr++){
		for(int j = *ptr; j < *ptr; j++){
			cout << j << " ";
		}
		cout << endl;	
	}
}


int main(){
	int n;
	cin >> n;
	vector<vector<int>> res = generate(n);
	print(res)
}