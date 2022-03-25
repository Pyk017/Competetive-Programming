class Solution{
    binarysearch(arr,n,k){
        let [left, mid, right] = [0, 0, n - 1];
        
        while (left <= right) {
            
            mid = Math.floor(left + (right - left) / 2);
            // console.log(mid);
            if (arr[mid] == k) {
                return mid;
            } else if (arr[mid] < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
}