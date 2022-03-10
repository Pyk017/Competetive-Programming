#include <bits/stdc++.h>
using namespace std;

class Solution{
public:
    int remove_duplicate(int A[],int n){
        int i=0, j=0;
        int count = 0;
        
        while(i<n) {
            
            while (i < n - 1 && A[i] == A[i + 1]) i++;
            
            i += 1;
            j += 1;
            
            if (j < n && i < n) {
                A[j] = A[i];
            }
            
            count += 1;
        }
        
        return count;
    }
};


int main()
{

    int N;
    cin>>N;
    int a[N];
    for(int i=0;i<N;i++)
    {
        cin>>a[i];
    }
    Solution ob;
    int n = ob.remove_duplicate(a,N);

    for(int i=0;i<n;i++)
        cout<<a[i]<<" ";
    cout<<endl;
    
}