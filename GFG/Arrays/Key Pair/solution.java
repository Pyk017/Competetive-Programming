import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] inputLine;
        inputLine = br.readLine().trim().split(" ");
        int n = Integer.parseInt(inputLine[0]);
        int x = Integer.parseInt(inputLine[1]);
        int[] arr = new int[n];
        inputLine = br.readLine().trim().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputLine[i]);
        }

        boolean ans = new Solution().hasArrayTwoCandidates(arr, n, x);
        System.out.println(ans ? "Yes" : "No");
        
    }
}

class Solution {
    boolean hasArrayTwoCandidates(int arr[], int n, int x) {
        // code here
        HashMap<Integer, Integer> map = new HashMap<>();
        int temp = 0;
        
        for(int i=0; i<n; i++) {
            temp = x - arr[i];
            
            if(map.containsKey(arr[i])) {
                return true;
            } else {
                map.put(temp, arr[i]);
            }
        }
        
        return false;
    }
}