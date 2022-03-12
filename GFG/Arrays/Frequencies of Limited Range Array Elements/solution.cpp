#include<bits/stdc++.h>
using namespace std; 

class Solution{
    public:
    void frequencyCount(vector<int>& arr,int N, int P)
    { 
        for(int i = 0; i < N; i++) {
            if(arr[i] > N)
                arr[i] = 0;
        }
        
        for(int i = 0; i < N; i++) {
            if(arr[i]%(N+1) > 0)
                arr[(arr[i]%(N+1))-1] += (N+1);
        }
        
        for(int i = 0; i < N; i++) {
            arr[i] /= (N+1);
        }
    }
};


int main() 
{ 
	    
	int N, P;
	//size of array
	cin >> N; 

	vector<int> arr(N);

	//adding elements to the vector
	for(int i = 0; i < N ; i++){
	    cin >> arr[i]; 
	}
	cin >> P;
	Solution ob;
	//calling frequncycount() function
	ob.frequencyCount(arr, N, P); 

	//printing array elements
	for (int i = 0; i < N ; i++) 
		cout << arr[i] << " ";
	cout << endl;

	return 0; 
	}
