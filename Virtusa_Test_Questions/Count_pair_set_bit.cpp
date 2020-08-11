#include <bits/stdc++.h> 
using namespace std; 
  
// Function to return the 
// count of Pairs 
int countPairs(int arr[], int N) 
{ 
    // Get the maximum element 
    int maxm = *max_element(arr, arr + N); 
  
    int i, k; 
    // Array to store count of bits 
    // of all elements upto maxm 
    int bitscount[maxm + 1] = { 0 }; 
  
    // Store the set bits 
    // for powers of 2 
    for (i = 1; i <= maxm; i *= 2) 
        bitscount[i] = 1; 
    // Compute the set bits for 
    // the remaining elements 
    for (i = 1; i <= maxm; i++) { 
        if (bitscount[i] == 1) 
            k = i; 
        if (bitscount[i] == 0) { 
            bitscount[i] 
                = bitscount[k] 
                  + bitscount[i - k]; 
        } 
    } 
  
    // Store the frequency 
    // of respective counts 
    // of set bits 
    map<int, int> setbits; 
    for (int i = 0; i < N; i++) { 
        setbits[bitscount[arr[i]]]++; 
    } 
  
    int ans = 0; 
    for (auto it : setbits) { 
        ans += it.second 
               * (it.second - 1) / 2; 
    } 
  
    return ans; 
} 
  
int main() 
{ 
    int N;
    cin >> N; 
    // int arr[] = { 1, 2, 3, 4, 5, 6, 7, 
    //               8, 9, 10, 11, 12 }; 
    int arr[N];
    for(int i=0; i<N; i++){
        cin >> arr[i];
    }

    cout << countPairs(arr, N); 
  
    return 0; 
} 