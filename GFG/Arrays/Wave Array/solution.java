import java.io.*;
import java.util.*;

class GFG {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int n = Integer.parseInt(br.readLine().trim());// taking size of array
	    int arr[] = new int[n]; // declaring array of size n
	    String inputLine[] = br.readLine().trim().split(" ");
	    for(int i=0; i<n; i++){
	        arr[i]=Integer.parseInt(inputLine[i]); // input elements of array
	    }
	    
	    Solution obj = new Solution();
	    
	    
	    obj.convertToWave(arr, n);
	    
	    StringBuffer sb = new StringBuffer(); 
        for (int i = 0; i < n; i++) 
            sb.append(arr[i] + " "); 
            
	    System.out.println(sb); // print array
	
	}
}



class Solution{
    public static void convertToWave(int arr[], int n){
        
        int temp;
        
        for (int i=0; i<n-1; i+=2) {
            temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
        
    }
    
}
