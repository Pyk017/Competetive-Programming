// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{

	public:
	int findSwapValues(int A[], int n, int B[], int m){
        int sum_a = 0, sum_b = 0;
        
        sort(A, A + n);
        sort(B, B + m);
        
        for(int i=0; i<n; i++) {
            sum_a +=  A[i];
        }
        
        for(int j=0; j<m; j++) {
            sum_b +=  B[j];
        }
        
        // cout << sum_a << " " << sum_b << endl;
        
        int x=0, y=0;
        int mid = 0;
        int i = 0, j = 0;
        
        while (i < n && j < m) {
            x = sum_a - A[i] + B[j];
            y = sum_b - B[j] + A[i];
            
            if (x == y) return 1;
            
            else if( x > y ) i++;
            
            else j++;
        }
        
        return -1;
        
	}
 

};

// { Driver Code Starts.

int main() {
	int n,m;
    cin>>n>>m;
    int a[n];
    int b[m];
    for(int i=0;i<n;i++)
        cin>>a[i];
    for(int i=0;i<m;i++)
        cin>>b[i];
    

    Solution ob;
    cout <<  ob.findSwapValues(a, n, b, m);
    cout << "\n";
	     
    
    return 0;
}
