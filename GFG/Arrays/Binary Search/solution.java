import java.io.*;
import java.util.*;

public class GFG {
    public static void main (String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
         
        int key =sc.nextInt();
        Solution g = new Solution();
        System.out.println(g.binarysearch(arr,n,key));
         
    }
}


class Solution {
    int binarysearch(int arr[], int n, int k){
        int left = 0, right = n - 1;
        int mid = 0;
        
        while(left <= right) {
            mid = left + (right - left) / 2;
            if (arr[mid] == k) {
                return mid;
            } else if (arr[mid] < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
}