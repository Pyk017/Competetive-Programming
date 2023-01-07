import java.util.*;
class Solution {
    void reverseInGroups(ArrayList<Integer> arr, int n, int k) {
        int i = 0;
        while (i < n) {
            int start = i;
            int end = Math.min(i + k - 1, n - 1);
            while (start < end) Collections.swap(arr, start++, end--);
            i += k;
        }
    }

    public static void main(String[] args) {
        try (Scanner in = new Scanner(System.in)){
            String inputLine1[] = in.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine1[0]);
            int k = Integer.parseInt(inputLine1[1]);
            
            ArrayList<Integer> arr = new ArrayList<>();            
            String inputLine2[] = in.readLine().trim().split(" ");
            for(int i=0; i<n; i++){
                arr.add(Integer.parseInt(inputLine2[i]));
            }
            
            Solution obj = new Solution();
            obj.reverseInGroups(arr, n, k);
            
            StringBuffer str = new StringBuffer();
            for(int i=0; i<n; i++){
                str.append(arr.get(i) + " ");
            }
            System.out.println(str);

        } catch(Exception e) {
            e.printStackTrace();
        }
    }

}