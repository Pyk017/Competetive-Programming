import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)) {
            int len = in.nextInt();
            String arrayString = in.nextLine();

            String[] inputs = arrayString.split(" ");
            int[] arr = new int[len];

            for (int i = 0; i < len; i++) {
                arr[i] = Integer.parseInt(inputs[i]);
            }

            ArrayList<Integer> result = valueEqualToIndex(arr, len);

            for (Integer x: result) {
                System.out.print(x + " ");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static ArrayList<Integer> valueEqualToIndex(int[] arr, int n) {
        ArrayList<Integer> result = new ArrayList<Integer>();

        for(int i = 0; i < n; i++) {
            if (arr[i] == (i + 1)) {
                Integer y = new Integer(arr[i]);
                result.add(y);
            }
        }

        return result;
    }
}