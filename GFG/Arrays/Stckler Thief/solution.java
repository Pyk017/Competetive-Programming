// { Driver Code Starts
import java.util.*;
import java.io.*;

class GFG
 {
	public static void main (String[] args)
	 {
	  
	  //taking input using Scanner class
	  Scanner sc = new Scanner(System.in);
	      
      //taking count of houses
      int n = sc.nextInt();
      int arr[] = new int[n];
      
      //inserting money present in 
      //each house in the array
      for(int i = 0; i<n; ++i)
           arr[i] = sc.nextInt();
	      
	      //calling method FindMaxSum() of class solve
      System.out.println(new Solution().FindMaxSum(arr, n));
	 
   }
}


class Solution
{
    //Function to find the maximum money the thief can get.
    public int FindMaxSum(int arr[], int n)
    {
        int inc=0, exc = 0, temp;

    	for(int i=0; i<n; i++) {
    		temp = inc;
    		inc=arr[i] + exc;
    		exc = Math.max(temp, exc);
    	}

    	return Math.max(inc, exc);
    }
}