import java.io.*;
import java.util.*;

public class GFG {

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
        Solution ob = new Solution();
        int ans[] = ob.sumClosest(arr, x);
        for (Integer val: ans) 
            System.out.print(val+" "); 
        System.out.println();
        
    }
}


class Solution {
    int[] sumClosest(int[] arr, int x) {
        int[] result = new int[2];
        int closest = Integer.MAX_VALUE;
        int i = 0, j = arr.length - 1;
        int temp = 0;
        
        while ( i < j ) {
            temp = x - (arr[i] + arr[j]);
            
            if (Math.abs(temp) < closest) {
                closest = Math.abs(temp);
                result[0] = arr[i];
                result[1] = arr[j];
            }
            
            if (temp < 0) {
                j -= 1;
            } else {
                i += 1;
            }
        }
        
        return result;
                           
        
    }
}