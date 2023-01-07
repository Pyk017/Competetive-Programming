class Solution{
    public static boolean check(long A[],long B[],int N)
    {
        Map<Long, Long> map = new HashMap<Long, Long>();
        
        for (int i=0; i<N; i++) {
            if (map.containsKey(A[i])) {
                map.put(A[i], map.get(A[i]) + 1);
            } else {
                map.put(A[i], 1l);
            }
        }
        
        for (int i=0; i<N; i++) {
            if (!map.containsKey(B[i]) || map.get(B[i]) == 0) return false;
            
            map.put(B[i], map.get(B[i]) - 1);
        }
        
        return true;
        
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        long arr[] = new long[n];
        long brr[] = new long[n];

         for (int i=0; i<n; i++) {
            arr[i] = in.nextLong();
         }

         for (int i=0; i<n; i++) {
            brr[i] = in.nextLong();
         }

         Solution ob = new Solution();
         System.out.println(ob.check(arr, brr, n) == true ? "1": "0");

    }

}