// { Driver Code Starts
//Initial Template for Java
import java.io.*;
import java.util.*;


class GFG {
	public static void main (String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			    
	    int n = Integer.parseInt(br.readLine());
	    int arr[] = new int[n];
	    
	    
	    String line = br.readLine();
	    String[] elements = line.trim().split(" ");
	    
	    for(int index = 0;index < n; index++){
	        arr[index] = Integer.parseInt(elements[index]);
	    }
	    
	    Check obj = new Check();
	    
	    System.out.println(obj.firstNonRepeating(arr,n));
		
	}
}


class Check{
    
    public int firstNonRepeating(int arr[], int n) { 
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for(int i = 0; i < n; i++) {
            
            if (map.get(arr[i]) == null) {
                map.put(arr[i], 1);
            } else {
                map.put(arr[i], map.get(arr[i]) + 1);
            }
            
        }
        
        // System.out.println(map);
        
        for(int i=0; i<n; i++) {
            if (map.get(arr[i]) == 1) {
                return arr[i];
            } 
        }
        
        return 0;
    }  
    
}

