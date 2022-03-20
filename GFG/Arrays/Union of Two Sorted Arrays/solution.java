import java.util.*;
import java.io.*;
import java.lang.*;

class Main
{
    public static void main(String args[])throws IOException
    {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        
        String st[] = read.readLine().trim().split(" ");
        int N = Integer.parseInt(st[0]);
        int M = Integer.parseInt(st[1]);
        
        int arr1[] = new int[N];
        int arr2[] = new int[M];
        
        st = read.readLine().trim().split(" ");
        for(int i = 0; i < N; i++)
          arr1[i] = Integer.parseInt(st[i]);
        
        st = read.readLine().trim().split(" ");  
        for(int i = 0; i< M; i++)
          arr2[i] = Integer.parseInt(st[i]);
        
        Solution obj = new Solution();
        ArrayList<Integer> res = new ArrayList<Integer>();
        res = obj.findUnion(arr1, arr2, N, M);
        for(int i = 0;i<res.size();i++)
            System.out.print(res.get(i) + " ");
        System.out.println(); 
        
    }
}



class Solution
{
    //Function to return a list containing the union of the two arrays.
    public static ArrayList<Integer> findUnion(int arr1[], int arr2[], int n, int m)
    {
        SortedMap<Integer, Integer> sm = new TreeMap<Integer, Integer>();
        ArrayList<Integer> answer = new ArrayList<Integer>();
        
        int size = Math.max(n, m);
        
        for(int i=0; i<size; i++) {
            if (i < n) {
                sm.put(new Integer(arr1[i]), new Integer(1));
            }
            
            if (i < m) {
                sm.put(new Integer(arr2[i]), new Integer(1));
            }
        }
        
        for (Map.Entry mapElement : sm.entrySet()) {
            int key = (int)mapElement.getKey();
            answer.add(key);
        }
        
        return answer;
        
    }
}



