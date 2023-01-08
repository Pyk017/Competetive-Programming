import java.util.Scanner;
import java.util.ArrayList;


class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int line = in.nextLine();
        String[] inputStrings = in.nextLine().trim().split(" ");

        int n = Integer.parseInt(line[0]); 
        int x = Integer.parseInt(line[1]); 

        long arr[] = new long[n];

        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(inputStrings[i]);
        }

        Solution ob = new Solution();

        ArrayList<Long> res = ob.find(arr, n, x);

        System.out.println(res.get(0) + " " + res.get(1));
    }

    public ArrayList<Long> find(long arr[], int n, int x) {
        int start=-1, end=-1;
        ArrayList<Long> result = new ArrayList<Long>();

        for (int i = 0; i < n; i++) {
            if (arr[i] == x) {
                start = i;
                break;
            }
        }

        for (int j = n - 1; j >= 0; j--) {
            if (arr[j] == x) {
                end = j;
                break;
            }
        }

        result.add(start);
        result.add(end);

        return result;
    }
}