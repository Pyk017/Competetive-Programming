// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

 // } Driver Code Ends
class Solution{
    public:
    //Function to find the maximum money the thief can get.
    int FindMaxSum(int arr[], int n){

    	int inc=0, exc = 0, temp;

    	for(int i=0; i<n; i++) {
    		temp = inc;
    		inc=arr[i] + exc;
    		exc = max(temp, exc);
    	}

    	return max(inc, exc);
    }
};

// { Driver Code Starts.
int main()
{
    
	int n;
	cin>>n;
	int a[n];
	
	//inserting money of each house in the array
	for(int i=0;i<n;++i)
		cin>>a[i];
	Solution ob;
	//calling function FindMaxSum()
	cout<<ob.FindMaxSum(a,n)<<endl;
	
	return 0;
}
  // } Driver Code Ends