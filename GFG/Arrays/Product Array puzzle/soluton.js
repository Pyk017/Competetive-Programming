class Solution {
    productExceptSelf(nums,n){
      if (n == 1) {
          nums[0] = 1;
          return nums;
      }
      
        let leftArr = Array(n).fill(0);
        let rightArr = Array(n).fill(0);
        let i = 0;
        
        leftArr[0] = nums[0];
        rightArr[n - 1] = nums[n - 1];
        
        for (i=1; i<n-1; i++) {
            leftArr[i] = leftArr[i - 1] * nums[i];
            rightArr[n - i - 1] = rightArr[n - i] * nums[n - i - 1];
        }

        leftArr[n - 1] = leftArr[i] * nums[n - 1];
        rightArr[0] = rightArr[n - i - 1] * nums[0];
        
        
        for (i=0; i<n; i++) {
            if (i === 0) {
                nums[i] = rightArr[i + 1];
            } else if(i == n - 1) {
                nums[i] = leftArr[i - 1];
            } else {
                nums[i] = leftArr[i - 1] * rightArr[i + 1];
            }
        }


        return nums;
      
    }
}