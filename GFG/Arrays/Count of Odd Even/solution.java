import java.util.*;
import java.lang.*;
import java.io.*;
class GFG{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine().trim());
        String[] S = br.readLine().trim().split(" ");
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(S[i]);
        }
        Solution obj = new Solution();
        obj.countOddEven(arr, n);
        
    }
}


class Solution{
    public void countOddEven(int[] arr, int n){
        int countOdd = 0, countEven = 0;
        
        for(int i=0; i < n; i++) {
            if (arr[i] % 2 == 1) {
                countOdd += 1;
            } else {
                countEven += 1;
            }
        }
        
        System.out.println(countOdd + " " + countEven);

    }
}