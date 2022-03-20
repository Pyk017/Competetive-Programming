import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {

        // Taking input using class Scanner
        Scanner sc = new Scanner(System.in);
    
        int n = sc.nextInt();

        // creating a new array of size n
        int arr[] = new int[n];

        // inserting elements to the array
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Solution ob = new Solution();
        // calling firstRepeated method
        // and printing the result
        System.out.println(ob.firstRepeated(arr, n));
        
    }
}

class Solution {
    // Function to return the position of the first repeating element.
    public static int firstRepeated(int[] arr, int n) {
        int current = n + 1;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for(int i=0; i<n; i++) {
            if (map.containsKey(arr[i])) {
                current = Math.min(current, map.get(arr[i]));
            } else {
                map.put(arr[i], i);
            }
        }
        
        if (current == n + 1) return -1;
        
        return current + 1;
    }
}
