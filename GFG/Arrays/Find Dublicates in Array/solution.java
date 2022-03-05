// { Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            Solution g = new Solution();
            ArrayList<Integer> ans = g.duplicates(a, n);
            for (Integer val : ans) System.out.print(val + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


class Solution {
    public static ArrayList<Integer> duplicates(int arr[], int n) {
        int[] temp = new int[n];
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        for(int i=0; i<n; i++) {
            temp[arr[i]] += 1;
        }
        
        for(int i=0; i<n; i++) {
            if (temp[i] > 1) {
                result.add(i);
            }
        }
        
        if (result.size() == 0){
            result.add(-1);
            return result;
        }
        
        return result;
        
    }
}
