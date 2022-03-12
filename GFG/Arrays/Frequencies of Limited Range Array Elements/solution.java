import java.io.*;
import java.util.*;

class GFG {
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine().trim()); 
        int arr[] = new int[N];
        String inputLine[] = br.readLine().trim().split(" ");

        //adding elements to the array
        for(int i = 0 ; i < N; i++){
            arr[i]=Integer.parseInt(inputLine[i]); 
        }
        int P= Integer.parseInt(br.readLine().trim());
        //calling frequncycount() function
        Solution ob = new Solution();
        ob.frequencyCount(arr, N, P); 
        
        //printing array elements
        for(int i = 0; i < N ; i++)
            System.out.print(arr[i] + " " );
        System.out.println();
    
    }
}

class Solution{
    //Function to count the frequency of all elements from 1 to N in the array.
    public static void frequencyCount(int arr[], int N, int P)
    {
        int []array=new int[N];
       int value=0;
       for(int i=0;i<N;i++ )
       {
           value =arr[i];
           if(value<=N){
               array[value-1]++;                     
           }
       }
       
       for(int i=0; i<N; i++) 
            System.out.println(array[i]);
       
       for(int i=0;i<N;i++)
       {
           arr[i]=array[i];
       }
    }

    public static void solution2(int arr[], int N, int P)
    {
       for(int i = 0; i < N; i++) {
            if(arr[i] > N)
                arr[i] = 0;
        }
        
        for(int i = 0; i < N; i++) {
            if(arr[i]%(N+1) > 0)
                arr[(arr[i]%(N+1))-1] += (N+1);
        }
        
        for(int i = 0; i < N; i++) {
            arr[i] /= (N+1);
        }
    }

}
