import java.io.*;
import java.util.*;

class Solution
{
    public static void sort012(int arr[], int n)
    {
        int i = 0;
        while((i < n) && arr[i] == 0){
            i += 1;
        }
        
        int j = i;
        
        while (j < n) {
            while((j < n) && (arr[j] != 0)){
                j += 1;
            }
            
            if (j < n) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i += 1;
                j += 1;
            }
        }
        
        
        
        
        int k = 0;
        while ((k < n) && (arr[k] == 0)) {
            k += 1;
        }
        
        i = k;
        
        while((i < n) && (arr[i] == 0)){
            i += 1;
        }
        
        j = i;
        
        while (j < n) {
            while((j < n) && (arr[j] != 1)){
                j += 1;
            }
            
            if (j < n) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i += 1;
                j += 1;
            }
        }
    }
}


class GFG {
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim()); //Inputting the testcases
        while(t-->0){
            int n = Integer.parseInt(br.readLine().trim());
            int arr[] = new int[n];
            String inputLine[] = br.readLine().trim().split(" ");
            for(int i=0; i<n; i++){
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            Solution ob=new Solution();
            ob.sort012(arr, n);
            StringBuffer str = new StringBuffer();
            for(int i=0; i<n; i++){
                str.append(arr[i]+" ");
            }
            System.out.println(str);
        }
    }
}

  