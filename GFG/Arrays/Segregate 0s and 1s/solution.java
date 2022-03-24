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
        new Solution().segregate0and1(arr, n);
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}


class Solution {
    void segregate0and1(int[] arr, int n) {
        int i=0, a=0;
        int temp = 0;
        
        while (arr[i++] == 0);
        
        a = i - 1;
        
        for(int j = i; j < n; j++) {
            if (arr[j] == 0) {
                temp = arr[j];
                arr[j] = arr[a];
                arr[a] = temp;
                a += 1;
            }
        }
    }

}
