#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    //arr1,arr2 : the arrays
    // n, m: size of arrays
    //Function to return a list containing the union of the two arrays. 
    vector<int> findUnion(int arr1[], int arr2[], int n, int m)
    {
        vector<int> answer;
        map<int, int> mp;
        int size = max(n, m);
        
        for(int i=0; i<size; i++) {
            if (i < n) {
                mp[arr1[i]]++;
            }
            if (i < m) {
                mp[arr2[i]]++;
            }
        }
    	
    	for(auto pair: mp) 
    	    answer.push_back(pair.first);

    	return answer;
    }
};



int main() {
	
    int N, M;
    cin >>N >> M;
    
    int arr1[N];
    int arr2[M];
    
    for(int i = 0;i<N;i++){
        cin >> arr1[i];
    }
    
    for(int i = 0;i<M;i++){
        cin >> arr2[i];
    }
    Solution ob;
    vector<int> ans = ob.findUnion(arr1,arr2, N, M);
    for(int i: ans)cout<<i<<' ';
    cout << endl;
	
	return 0;
}