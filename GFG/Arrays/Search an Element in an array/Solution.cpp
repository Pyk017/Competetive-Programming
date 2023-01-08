class Solution {
    public: 
        int search(int[] arr, int N, int X) {
            for(int i=0; i<N; i++) {
                if (arr[i] == X) return i;
            }
            return -1;
        }
}


int main() {

    int n;
    cin >> n;
    int a[n];
    
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }

    int x;
    cin >> x;

    Solution ob;
    cout << ob.search(a, n, x) << endl;

    return 0;
}