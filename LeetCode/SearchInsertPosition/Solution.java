class Solution {
    public static void searchInsert(int arr[], int n) {
        int start = 0; 
        int end = n - 1;
        int mid = 0;

        while (start <= end) {
            mid = Math.floor((start + end) / 2);

            if (arr[mid] == target) return mid;

            if (arr[mid] > target) {
                end = mid - 1;
            } 

            if (arr[mid] < target) {
                start = mid + 1;
            }
        }

        return mid;
    }
}