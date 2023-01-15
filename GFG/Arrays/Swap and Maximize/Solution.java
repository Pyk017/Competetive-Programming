import java.util.*;
import java.lang.Math;

class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] line = in.nextLine().trim().split(" ")

        int[] arr = new int[n];

        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(line[i]);
        }

        Solution sol = new Solution();

        int result = sol.maxSum(arr, n);

        System.out.println(result);

    }

    public int maxSum(int[] arr, int n) {
        int i=0, j=n-1;

        Arrays.sort(arr); 

        long long int result = 0;
        
        bool flag = true;


        while (i < j) {
            if (flag) {
                result += abs(a[i] - a[j]);
                i++;
            } else {
                result += abs(a[i] - a[j]);
                j--;
            }

            flag = !flag;
        }

        result += Math.abs(a[j] - a[0]);

        return result;
    }
}