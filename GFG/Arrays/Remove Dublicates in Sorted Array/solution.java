import java.io.*;
import java.util.*;

public class GFG {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int a[] = new int[N];
        for(int i=0; i<N; i++)
            a[i] = sc.nextInt();
        
        Solution g = new Solution();
        int n = g.remove_duplicate(a,N);
        
        for(int i=0; i<n; i++)
            System.out.print(a[i]+" ");
        System.out.println();
        T--;
    
    }
}

class Solution {
    int remove_duplicate(int A[],int n){
        int i=0, j=0;
        int count = 0;
        
        while(i<n) {
            
            while (i < n - 1 && A[i] == A[i + 1]) i++;
            
            i += 1;
            j += 1;
            
            if (j < n && i < n) {
                A[j] = A[i];
            }
            
            count += 1;
        }
        
        return count;
    }
}