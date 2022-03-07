import java.io.*;
import java.util.*;

public class GFG {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputLine;
        inputLine = br.readLine().trim().split(" ");
        int n = Integer.parseInt(inputLine[0]);
        int k = Integer.parseInt(inputLine[1]);
        int[] arr = new int[n];
        inputLine = br.readLine().trim().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputLine[i]);
        }
        int ans = new Solution().getPairsCount(arr, n, k);
        System.out.println(ans);
    
    }
}

class Solution {
    int getPairsCount(int[] arr, int n, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        int count = 0;
        int temp = 0;
        
        for (Integer i : arr) {
            Integer j = map.get(i);
            map.put(i, (j == null) ? 1 : j + 1);
        }
        
        for(int i=0; i<n; i++) {
            temp = k - arr[i];
            
            if (map.containsKey(temp)) {
                map.put(arr[i], map.get(arr[i]) - 1);
                count += map.get(temp);
            }
        }
        
        return count;
        
    }
}
