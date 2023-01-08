import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        String[] inputStrings = in.nextLine().trim().split(" ");

        int arr[] = new int[n];

        for(int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputStrings[i]);
        }

        Solution solution = new Solution();
        solution.rotate(arr, n);

        StringBuilder output = new StringBuilder();
        for(int i = 0; i < n; i++) {
            output.append(arr[i] + " ");
        }
        System.out.println(output);

    }

    public void rotate(int[] arr, int n) {
        int i = n - 1;
        int temp = arr[i];

        while (i > 0) {
            arr[i] = arr[i - 1];
            i -= 1;
        }

        arr[0] = temp;
    }
}