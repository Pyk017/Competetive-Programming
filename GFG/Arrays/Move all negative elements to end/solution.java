// { Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main(String[] args) throws IOException
	{
        BufferedReader br =
        new BufferedReader(new InputStreamReader(System.in));
    
        int n = Integer.parseInt(br.readLine().trim());
        int a[] = new int[(int)(n)];
        String inputLine[] = br.readLine().trim().split(" ");
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(inputLine[i]);
        }
        
        Solution obj = new Solution();
        obj.segregateElements(a, n);
        
        for(int i=0;i<n;i++)
        System.out.print(a[i]+" ");
        
        System.out.println();
    
	}
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    
    public void segregateElements(int arr[], int n)
    {
        // Your code goes here
        ArrayList<Integer> pos = new ArrayList<Integer>();
        ArrayList<Integer> neg = new ArrayList<Integer>();
        
        for(int i=0; i<n; i++) {
            if (arr[i] >= 0) {
                pos.add(arr[i]);
            } else {
                neg.add(arr[i]);
            }
        }
        
        int x=0,y=0;
        
        while(x < pos.size()) {
            arr[x] = (int)pos.get(x);
            x += 1;
        }
        
        // System.out.println(x);
        y = x;
        int j = 0;
        
        while(j < neg.size()) {
            arr[y] = (int)neg.get(j);
            y += 1;
            j += 1;
        }
        
    }
}