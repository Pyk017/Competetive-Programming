// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;
class Solution{

    public:
     int max_path_sum(int A[], int B[], int l1, int l2){
          int res=0;
       int i=0,j=0;
       int asum=0,bsum=0;
       while(i<l1 && j<l2){
           if(A[i]==B[j]){                           
               asum+=A[i++];
               bsum+=B[j++];
               res+=max(asum,bsum);             
               asum=0;
               bsum=0;
           }
           if(A[i]<B[j])
               asum+=A[i++];
           if(A[i]>B[j])
               bsum+=B[j++];
       }
       while(i<l1){
           asum+=A[i++];
       }
       while(j<l2){
           bsum+=B[j++];
       }
       res+=max(asum,bsum);
       return res;

    }
};


int main(){

    int N,M;
    cin>>N>>M;
    fflush(stdin);
    int a[N],b[M];
    for(int i=0;i<N;i++)
        cin>>a[i];
    for(int i=0;i<M;i++)
        cin>>b[i];
    Solution obj;
    int result = obj.max_path_sum(a,b,N,M);
    cout<<result<<endl;
    
}