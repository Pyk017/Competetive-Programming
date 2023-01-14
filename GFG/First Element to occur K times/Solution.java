import java.util.*;

class Solution
{
    public int firstElementKTime(int[] a, int n, int k) { 
        Map<Integer, Integer> mp = new HashMap<Integer, Integer>();
        
        for(int i=0; i<n; i++) {
            if (mp.containsKey(a[i])) {
                mp.put(a[i], mp.get(a[i]) + 1);
            } else {
                mp.put(a[i], 1);
            }
            
            if (mp.get(a[i]) == k) return a[i];
        }
        
        return -1;
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String inputLine[] = in.nextLine().trim().split(" ");
        int n = Integer.parseInt(inputLine[0]);
        int k = Integer.parseInt(inputLine[1]);
        int[] arr = new int[n];

        inputLine = in.nextLine().trim().split(" ");

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputLine[i]);
        }

        Solution obj = new Solution();

        System.out.println(obj.firstElementKTime(arr, n, m));
    }

}