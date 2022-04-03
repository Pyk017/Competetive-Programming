import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(read.readLine().trim());
        String arr[] = read.readLine().trim().split(" ");

        Solution ob = new Solution();
        System.out.println(ob.longestCommonPrefix(arr, n));
    }
}


class Solution{
    String longestCommonPrefix(String arr[], int n){
        if (n == 1) return arr[0];
        
        int mini = Integer.MAX_VALUE;
        String ans = "";
        int i, m;
        
        char[] first = arr[0].toCharArray();
        
        for(int j = 1; j < n; j++) {
            char[] word = arr[j].toCharArray();
            m = word.length;
            i = 0;
            
            while ( i < m ) {
                if (i >= first.length) break;
                
                if (word[i] != first[i]) break;
                
                i += 1;
            }
            
            if (i == 0) return "-1";
            
            if ( i <= mini ) {
                ans = arr[j].substring(0, i).toString();
                mini = i;
            }
            
        }
        
        return ans;
    }
}