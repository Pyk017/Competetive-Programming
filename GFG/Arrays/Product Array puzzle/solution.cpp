#include<bits/stdc++.h>
using namespace std;
class Solution{
  public:
    // nums: given vector
    // return the Product vector P that hold product except self at each index
    vector<long long int> productExceptSelf(vector<long long int>& nums, int n) {
      
       
       long long int product = 1;
       int countZero = 0;
       long long int zeroProd = 0;
       for (int i = 0; i<n; i++) {
            if(nums[i] == 0) {
                countZero += 1;
            } else {
                product *= nums[i];	    
            }
       }

       if(countZero > 1) {
            product = 0;
       }
       
       if (countZero == 1) {
           zeroProd = product;
           product = 0;
       }
       
       for(int i=0; i<n; i++) {
           if (nums[i] == 0 && countZero == 1) {
              nums[i] = zeroProd;
           }
           else if(countZero > 1) {
               nums[i] = 0;
           }
           
           else {
                nums[i] = product / nums[i];   
           }
            
       }
    
       return nums;

    }

    vector<long long int> withoutDivision(vector<long long int>& nums, int n) {
        if (n == 1) {
            nums[0] = 1;
            return nums;
        }

        vector<long long int> leftArr(n);
        vector<long long int> rightArr(n);
        int i=0;

        leftArr[0] = nums[0];
        rightArr[n - 1] = nums[n - 1];

        for (int i=1; i<n-1; i++) {
            leftArr[i] = leftArr[i - 1] * nums[i];
            rightArr[n - i - 1] = rightArr[n - i] * nums[n - i - 1];
        }

        leftArr[n - 1] = leftArr[i] * nums[n - 1];
        rightArr[0] = rightArr[n - i - 1] * nums[0];

        for (int i=0; i<n; i++) {
            if (i == 0) {
                nums[i] = rightArr[i + 1];
            } else if(i == n - 1) {
                nums[i] = leftArr[i - 1];
            } else {
                nums[i] = leftArr[i - 1] * rightArr[i + 1];
            }
        }


        return nums;

    }

};



int main()
 {
    int n;  // size of the array
    cin>>n;
    vector<long long int> arr(n),vec(n);
    
    for(int i=0;i<n;i++)    // input the array
    {
        cin>>arr[i];
    }
    Solution obj;
    vec = obj.productExceptSelf(arr,n);   // function call
    
    for(int i=0;i<n;i++)    // print the output
    {
        cout << vec[i] << " ";
    }
    cout<<endl;

	return 0;
}  // } Driver Code Ends