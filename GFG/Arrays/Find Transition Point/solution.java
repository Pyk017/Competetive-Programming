import java.util.*;

class Sorted_Array {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            GfG obj = new GfG();
            System.out.println(obj.transitionPoint(arr, n));
        
    }
}

class GfG {
    int transitionPoint(int arr[], int n) {
        // code here
        int left=0, right=n-1;
    int mid = 0;
    
    if (arr[0] == 1) {
        return 0;
    }
    
    if (arr[n - 1] == 0) {
        return -1;
    }
    
    while(left <= right) {
        mid = (int)Math.floor((left + right) / 2);
        
        if (arr[mid] == 1 && arr[mid - 1] == 0) {
            return mid;
        }
        
        if (arr[mid] == 1) {
            right = mid - 1;
        } 
        
        if (arr[mid] == 0) {
            left = mid + 1;
        }
        
    }
    
    return -1;
    }
}