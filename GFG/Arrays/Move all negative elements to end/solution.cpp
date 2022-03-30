// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
    public:
    void segregateElements(int arr[],int n){
        int i = 0;
        int temp = 0;
        int j = 0;
        
        while (i < n && arr[i] >= 0) {
            i += 1;
        }
        
        // cout << i << endl;
        
        while ( i < n ) {
            temp = i - 1;
            if (arr[i] >= 0) {
                j = arr[i];
                arr[i] = arr[temp];
                arr[temp] = j;
            }
            
            while (temp >= 0 && arr[temp] >= 0 && arr[temp - 1] < 0) {
                j = arr[temp];
                arr[temp] = arr[temp - 1];
                arr[temp - 1] = j;
                temp -= 1;
            }
            
            i += 1;
        }
    }

    void solution2(int arr[],int n){
        int temp=0,j=0,pos=0,i=0;
        
        vector<int> neg;
        
        while(j < n) {
            if (arr[j] < 0) {
                neg.push_back(arr[j]);
            }
            j += 1;
        }
        
        while(i < n && arr[i] >= 0) {
            i += 1;
        }
        
        // cout << i << endl;
        
        pos = i;
        
        while(i < n) {
            if (arr[i] >= 0) {
                temp = arr[pos];
                arr[pos] = arr[i];
                arr[i] = temp;
                pos += 1;
            }    
            
            i += 1;
        }
        
        // cout << pos << endl;
        i = 0;
        while (pos < n) {
            arr[pos] = neg[i];
            pos += 1;
            i += 1;
        }
        
    }

};

// { Driver Code Starts.
int main() {
	// your code goes here
	int n;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
	cin>>a[i];
	Solution ob;
	ob.segregateElements(a,n);
	
    for(int i=0;i<n;i++)
    cout<<a[i]<<" ";
	cout<<endl;

}
  // } Driver Code Ends