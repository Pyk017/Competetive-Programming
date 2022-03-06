class Solution {
  transitionPoint(arr, n) {
    if (arr[0] == 1) {
        return 0;
    }
    
    if (arr[n - 1] == 0) return -1;
    
    let [left, right] = [0, n - 1];
    let mid = 0;
    
    while (left <= right) {
        mid = Math.floor((left + right) / 2);
        
        if (arr[mid] == 1 && arr[mid - 1] == 0) return mid;
        
        if (arr[mid] == 1) right = mid - 1;
        
        if (arr[mid] == 0) left = mid + 1;
    }
    
    return -1;
  }
}