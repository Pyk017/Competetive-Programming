// { Driver Code Starts
//Initial Template for Java


import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputLine;
        int n = Integer.parseInt(br.readLine().trim());
        int[] arr = new int[n];
        inputLine = br.readLine().trim().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputLine[i]);
        }

        int ans = new Solution().findMaximum(arr, n);
        System.out.println(ans);
        
    }
}



class Solution {
    int findMaximum(int[] arr, int n) {
        int i = 0;
        
        while(i < n - 1 && arr[i] < arr[i + 1]) i++;
        return arr[i];
    }
}