// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*; 

class GFG{
    public static void main(String args[]) throws IOException { 
        Scanner sc = new Scanner(System.in);
        
    	int n = sc.nextInt();
    	int[] array = new int[n];
    	for (int i=0; i<n ; i++ ) {
    		array[i] = sc.nextInt();
    	}
        Solution ob = new Solution();
        long[] ans = new long[n];
        ans = ob.productExceptSelf(array, n); 

       	for (int i = 0; i < n; i++) { 
			System.out.print(ans[i]+" ");
		} 
        System.out.println();
        
    } 
} 
  

// } Driver Code Ends


//User function Template for Java


class Solution 
{ 
	public static long[] productExceptSelf(int nums[], int n) 
	{ 
	    long nums2[] = new long[n];
        if (n == 1) {
            nums2[0] = 1;
            return nums2;
        }

        long[] leftArr = new long[n];
        long[] rightArr = new long[n];
        int i=0;

        leftArr[0] = nums[0];
        rightArr[n - 1] = nums[n - 1];

        for (i=1; i<n-1; i++) {
            leftArr[i] = leftArr[i - 1] * nums[i];
            rightArr[n - i - 1] = rightArr[n - i] * nums[n - i - 1];
        }

        leftArr[n - 1] = leftArr[i] * nums[n - 1];
        rightArr[0] = rightArr[n - i - 1] * nums[0];
    
        
        for (i=0; i<n; i++) {
            if (i == 0) {
                nums2[i] = rightArr[i + 1];
            } else if(i == n - 1) {
                nums2[i] = leftArr[i - 1];
            } else {
                nums2[i] = leftArr[i - 1] * rightArr[i + 1];
            }
        }


        return nums2;
	} 
} 
