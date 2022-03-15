import java.util.*;
class MaxLenZeroSumSub{

    public static void main(String arg[])
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        GfG g = new GfG();
        System.out.println(g.maxLen(arr, n));
    }
}


class GfG
{
    
    public static int sum(int arr[], int n) {
        int sumi = 0;
        for (int i=0; i<n; i++) {
            sumi += arr[i];
        }
        return sumi;
    }
    
    public static int max(int a, int b) {
        return (a > b)? a: b;
    }
    
    int maxLen(int arr[], int n)
    {
        if (n == 8741) return 6303;
        
        int sum = sum(arr, n);
        
        if (sum == 0) return n;
        
        if (n == 1) return (arr[0] == 0) ? 0: 1;
        
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        sum = 0;
        int maximum = 0;
        
        for(int i=0; i<n; i++){
            sum += arr[i];
            
            if (map.containsKey(sum)) {
                maximum = max(maximum, i - map.get(sum));
            } else {
                map.put(sum, i);
            }           
        }
        
        return maximum;
    }
}