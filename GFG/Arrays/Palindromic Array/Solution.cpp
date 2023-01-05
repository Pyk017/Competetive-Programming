#include<iostream>
#include<string.h>
#include<cmath>

using namespace std;

class Solution {
    public: 
        int PalinArray(int[] a, int n) {
            for (int i=0; i<n; i++) {
                if (!isPalindrome(a[i])) return 0;
            }
            return 1;
        }

        bool isPalindrome(int num) {
            int temp = num;
            int result = 0;
            int rem;

            while (num > 0) {
                 rem = num % 10;
                 result = (result * 10) + rem;
                 num = (int) floor(num / 10);
            }

            return result == temp;
        } 
}

int main() {

    int n;
    cin >> n;

    int arr[n];

    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    Solution obj;
    cout << obj.PalinArray(arr, n) << endl;

    return 0;
}