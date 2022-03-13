import java.util.*;
import java.io.*;
import java.lang.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
    
        String str=br.readLine();
		String[] starr=str.split(" ");
		
		//input n and d
	    int n=Integer.parseInt(starr[0]);
		int d= Integer.parseInt(starr[1]);
		
        int[] arr=new int[n];
		String str1=br.readLine();
		String[] starr1=str1.split(" ");
		
		//inserting elements in the array
		for(int j=0;j<n;j++)
		{
		  arr[j]= Integer.parseInt(starr1[j]);
		}
		
		//calling rotateArr() function
        new Solution().rotateArr(arr, d, n);
		StringBuffer sb=new StringBuffer();
		
		//printing the elements of the array
        for(int t1=0;t1<n;t1++)
            sb.append(arr[t1]+" ");
        System.out.println(sb);
     
    }
}


class Solution{
    static void rotateArr(int arr[], int d, int n)
    {
        int[] temp = new int[d];
        
        for(int i=0; i<d; i++) {
            temp[i] = arr[i];
        }
        
        for (int i=0; i<(n - d); i++) {
            arr[i] = arr[i + d];
        }
        
        int diff = n - d;
        
        for(int k = 0; k < d; k++) {
            arr[k + diff] = temp[k];
        }
    }
}