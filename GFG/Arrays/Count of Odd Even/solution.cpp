#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    /*Function to count even and odd elements in the array
    * arr : Array with its elements
    * sizeof_array : number of array elements
    * countOdd : variable to count number of odd elements
    * countEven : variable to count number of even elements
    */
    void countOddEven(int arr[], int sizeof_array){
        int countOdd = 0, countEven = 0;
        
        for(int i=0; i < sizeof_array; i++) {
            if (arr[i] % 2) {
                countOdd += 1;
            } else {
                countEven += 1;
            }
        }
        
       cout << countOdd << " " << countEven << endl;
        
    }
};


int main() {
	
    int sizeof_array;
    cin >> sizeof_array;
    
    int arr[sizeof_array];
    
    // Array elements input
    for(int i = 0; i < sizeof_array; i++){
        cin >> arr[i];
    }
    Solution ob;
    // Calling function to count even and odd
    ob.countOddEven(arr, sizeof_array);
	
	return 0;

}  