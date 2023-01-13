import java.util.*;

class Solution {
    public int Maximize(int[] arr, int n) {
        Arrays.sort(arr);

        long result = 0;

        for(long i = 0; i < n; i++) {
            result += arr[(int)i] * i;
            result = result % 1000000007;
        }

        return (int)result%1000000007;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int inputStrings[] = in.nextLine().trim().split(" ");

        int arr[] = new int[n];

        for (int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(inputStrings[i]);
        }

        Solution ob = new Solution();
        int result = ob.Maximize(arr, n);

        System.out.println(result);
    }

}