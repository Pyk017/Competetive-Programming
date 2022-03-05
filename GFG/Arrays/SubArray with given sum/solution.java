// { Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class Main{
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            int n = sc.nextInt();
            int s = sc.nextInt();

            int[] m = new int[n];
            for (int j = 0; j < n; j++) {
                m[j] = sc.nextInt();
            }
            
            Solution obj = new Solution();
            ArrayList<Integer> res = obj.subarraySum(m, n, s);
            for(int ii = 0;ii<res.size();ii++)
                System.out.print(res.get(ii) + " ");
            System.out.println();
        }
    }

}// } Driver Code Ends


class Solution
{
    //Function to find a continuous sub-array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) 
    {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int currentSum = arr[0], start = 0;
	        
        for (int i=1; i<n + 1; i++) {
            while(currentSum > s && start < i - 1) {
                currentSum -= arr[start];
                start += 1;
            }
            
            if (currentSum == s) {
                result.add(start + 1);
                result.add(i);
                return result;
            }
            
            if (i < n){
                currentSum += arr[i];
            }
            
        }
	        
	        result.add(-1);
	        return result;
    }
}