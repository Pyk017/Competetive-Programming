import java.util.Scanner;

public class Solution {
     public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {

            int len = in.nextInt();
            in.nextLine();
            String line = in.nextLine();
            String[] inputString = line.trim().split(" ");
            int[] arr = new int[len];

            for(int i = 0; i < len; i++) {
                arr[i] = Integer.parseInt(inputArray[i]);
            }

            int result = palinArray(arr, len);

            System.out.println(result);
            
        } catch (Exception e)  {
            e.printStackTrace();
        }
     }

    public static int palinArray(int[] a, int n) {
        for (int i=0; i<n; i++) {
            if (!isPalindrome(a[i])) return 1;
        }

        return 0;
    }

    public static boolean isPalindrome(int num) {
        int temp = num;
        int result = 0;
        int rem;

        while (num > 0) {
            rem = num % 10;
            result = (result * 10) + rem;
            num = (int) Math.floor(num / 10);
        }

        return result == temp;
    }
}