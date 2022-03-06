// { Driver Code Starts
import java.io.*;
import java.util.*;

class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
            
            //taking input n
            int n = Integer.parseInt(br.readLine().trim());
            long arr[] = new long[n];
            String inputLine[] = br.readLine().trim().split(" ");
            
            //adding elements to the array
            for (int i = 0; i < n; i++) {
                arr[i] = Long.parseLong(inputLine[i]);
            }

            Solution ob = new Solution();
            
            //calling equilibriumPoint() function
            System.out.println(ob.equilibriumPoint(arr, n));
        
    }
}

class Solution {

    
    // a: input array
    // n: size of array
    // Function to find equilibrium point in the array.
    public static int equilibriumPoint(long a[], int n) {

        // Your code here
        int sumLeft = 0;
        
        for (int i=0; i<n; i++) {
            sumLeft += a[i];
        }
        
        int sumRight = 0;
        int i = n - 1;
        
        while ( i >= 0) {
            sumLeft -= a[i];
            
            if (sumLeft == sumRight) {
                return i + 1;
            }
            
            sumRight += a[i];
            i -= 1;
            
        }
        
        return -1;
        
    }
}
