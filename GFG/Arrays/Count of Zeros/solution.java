
import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }

            int ans = new Solution().countZeroes(arr, n);
            System.out.println(ans);
        
    }
}

class Solution {
    int countZeroes(int[] arr, int n) {
        if (arr[0] == 0) return n;
    
        for(int i = n - 1; i>= 0; i--) {
            if (arr[i] == 1) {
                return n - (i + 1);
            }
        }
        
        return 0;
    }

}
