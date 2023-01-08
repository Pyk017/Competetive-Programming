class Solution{   
    static int search(int arr[], int N, int X)
    {
        
        for (int i = 0; i < N; i++) {
            if (arr[i] == X) return i;
        }
        
        return -1;
        
    } 

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] st = in.nextLine().trim().split(" ");

        int arr[] = new int[n];

        for(int i=0; i<n; i++) {
            arr[i] = Integer.parseInt(st[i]);
        }

        int x = in.nextInt();

        Solution obj = new Solution();

        System.out.println(obj.search(arr, n, x));
    }  
}