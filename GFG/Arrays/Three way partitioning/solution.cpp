#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

class Solution{   
public:
    //Function to partition the array around the range such 
    //that array is divided into three parts.
    void threeWayPartition(vector<int>& array,int a, int b){
        // code here 
        int n = array.size();
        int temp, j=0;
        
        for (int i=0; i<n; i++) {
            if (array[i] < a) {
                temp = array[j];
                array[j] = array[i];
                array[i] = temp;
                j += 1;
            }
        }
        
        
        for (int i=j; i<n; i++) {
            if (array[i] >= a && array[i] <= b) {
                temp = array[j];
                array[j] = array[i];
                array[i] = temp;
                j += 1;
            }
        }
    
        for (int i=j; i<n; i++) {
            if (array[i] > b) {
                temp = array[j];
                array[j] = array[i];
                array[i] = temp;
                j += 1;
            }
        }
        
    }

    void betterSolution(vector<int>& array,int a, int b) {
        int n = array.size();
        int start = 0;
        int end = n - 1;
        int i=0, temp=0;

        while (i <= end) {
            if (array[i] < a) {
                temp = array[start];
                array[start] = array[i];
                array[i] = temp;
                start += 1;
                i += 1;
            } 
            else if (array[i] > b) {
                temp = array[end];
                array[end] = array[i];
                array[i] = temp;
                end -= 1;
            }
            else {
                i += 1;
            }
        }

    }

};

// { Driver Code Starts.

int main() {
    int N;
    cin>>N;
    
    vector<int> array(N);
    unordered_map<int,int> ump;
    
    for(int i=0;i<N;i++){
        cin>>array[i];
        ump[array[i]]++;
    }
    
    int a,b;
    cin>>a>>b;
    
    vector<int> original = array;

    int k1=0,k2=0,k3=0;
    int kk1=0;int kk2=0;int kk3=0;
    
    for(int i=0; i<N; i++)
    {
        if(original[i]>b)
            k3++;
        else if(original[i]<=b and original[i]>=a)
            k2++;
        else if(original[i]<b)
            k1++;
    }
    
    Solution ob;
    ob.threeWayPartition(array,a,b);
  
    for(int i=0;i<k1;i++)
    {
        if(array[i]<b)
        kk1++;
    }
    
    for(int i=k1;i<k1+k2;i++)
    {
        if(array[i]<=b and array[i]>=a)
        kk2++;
        
    }
    
    for(int i=k1+k2;i<k1+k2+k3;i++)
    {
        if(array[i]>b)
        kk3++;
    }
    bool ok = 0;
    if(k1==kk1 and k2 ==kk2 and k3 == kk3)
        ok = 1;
    
    for(int i=0;i<array.size();i++)
        ump[array[i]]--;
    
    for(int i=0;i<array.size();i++)
        if(ump[array[i]]!=0)
            ok=0;
    
    if(ok)
        cout<<1<<endl;
    else
        cout<<0<<endl;
        
    
    return 0;
}
  // } Driver Code Ends



