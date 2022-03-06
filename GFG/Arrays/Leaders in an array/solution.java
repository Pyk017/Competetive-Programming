// { Driver Code Starts
import java.io.*;
import java.util.*;

class Array {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		    
		    //input size of array
		    int n = Integer.parseInt(br.readLine().trim());
		    int arr[] = new int[n];
		    String inputLine[] = br.readLine().trim().split(" ");
		    
		    //inserting elements in the array
		    for(int i=0; i<n; i++){
		        arr[i] = Integer.parseInt(inputLine[i]);
		    }
		    
		    Solution obj = new Solution();
		    
		    StringBuffer str = new StringBuffer();
		    ArrayList<Integer> res = new ArrayList<Integer>();
		  
		    //calling leaders() function
		    res = obj.leaders(arr, n);
		    
		    //appending result to a String
		    for(int i=0; i<res.size(); i++){
		        str.append(res.get(i)+" ");
		    }
		    
		    //printing the String
		    System.out.println(str);
		
		
	}
}


class Solution{
    //Function to find the leaders in the array.
    static ArrayList<Integer> leaders(int a[], int n){
        // Your code here
        ArrayList<Integer> result = new ArrayList<Integer>();
        int temp = a[n - 1];
        int j = n - 2;
        result.add(temp);
        
        while(j >= 0) {
            if (a[j] >= temp) {
                result.add(a[j]);
                temp = a[j];
            }
            j -= 1;
        }
        Collections.reverse(result);
        return result;
    }
}
