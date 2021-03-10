#include<bits/stdc++.h>

using namespace std;

void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int x = (m + n) - 1;
        int i=m - 1, j = n - 1;
        while ((i >= 0) && (j >= 0)){
            if(nums1[i] <= nums2[j]){
                nums1[x] = nums2[j];
                x -= 1;
                j -= 1;
            }
            else if(nums1[i] > nums2[j]){
                nums1[x] = nums1[i];
                x -= 1;
                i -= 1;
            }
        }
        while(i >= 0){
            nums1[x] = nums1[i];
            x -= 1;
            i -= 1;
        }
        while(j >= 0){
            nums1[x] = nums2[j];
            j -= 1;
            x -= 1;
        }
    }



int main(){
    int n;
    cin >> n;

    return 0;
}