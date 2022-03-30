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

        new Solution().rearrange(arr, n);
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
        
    }
}


class Solution {
    void rearrange(int arr[], int n) {
        ArrayList<Integer> positive = new ArrayList<Integer>(); 
        ArrayList<Integer> negative = new ArrayList<Integer>(); 
        
        for(int i=0; i<n; i++) {
            if (arr[i] >= 0) {
                positive.add(arr[i]);
            } else {
                negative.add(arr[i]);
            }
        }
        
        int i=0, j=0, k=0;
	    int N = positive.size();
	    int M = negative.size();
	    
	    while (i < N && j < M) {
	        if (k % 2 == 0) {
	            arr[k] = positive.get(i);
	            i += 1;
	        } else {
	            arr[k] = negative.get(j);
	            j += 1;
	        }
	        k += 1;
	    }
	    
	    while(i < N) {
	        arr[k] = positive.get(i);
	        i += 1;
	        k += 1;
	    }
	    
	    while (j < M) {
	        arr[k] = negative.get(j);
	        j += 1;
	        k += 1;
	    }
        
        
    }
}