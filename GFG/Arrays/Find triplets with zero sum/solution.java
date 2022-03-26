// { Driver Code Starts
import java.util.*;
class Triplets{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[] a=new int[n];
		for(int i=0;i<n;i++){
			a[i]=sc.nextInt();
		}
		Solution g=new Solution();
		if(g.findTriplets(a,n))
			System.out.println("1");
		else
			System.out.println("0");
		
	}
}

class Solution{
	public boolean findTriplets(int arr[] , int n){
	    Arrays.sort(arr);
        int i = 0;
        int k = i + 1;
        int j = n - 1;
        int temp = 0;

        for (i=0; i < n - 2; i++) {
            k = i + 1;
            j = n - 1;
            while (k < j) {
                temp = arr[i] + arr[k] + arr[j];
                if (temp == 0){
                    return true;
                } else if (temp < 0) {
                    k += 1;
                } else {
                    j -= 1;
                }
            }
            
        }

        return false;
        //add code here.
    }
}