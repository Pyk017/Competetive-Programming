#include <iostream>
using namespace std;
class Solution{
    public:
    int equilibriumPoint(long long a[], int n) {
    
        // Your code here
        int sumLeft = 0;
        
        for (int i=0; i<n; i++) {
            sumLeft += a[i];
        }
        
        int sumRight = 0;
        int i = n - 1;
        
        while ( i >= 0) {
            sumLeft -= a[i];
            
            if (sumLeft == sumRight) {
                return i + 1;
            }
            
            sumRight += a[i];
            i -= 1;
            
        }
        
        return -1;
        
    }

};


int main() {

    long long n;
        
    //taking input n
    cin >> n;
    long long a[n];

    //adding elements to the array
    for (long long i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    Solution ob;

    //calling equilibriumPoint() function
    cout << ob.equilibriumPoint(a, n) << endl;
    
    return 0;
}