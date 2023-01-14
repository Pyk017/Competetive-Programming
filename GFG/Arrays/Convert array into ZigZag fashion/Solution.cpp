class Solution {
    public:
    void zigZag(int[] arr, int n) {
        for(int i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) {
                swap(arr[i - 1], arr[i]);
            }

            i += 1;
            if (i >= n) break;

            if (arr[i - 1] < arr[i]) {
                swap(arr[i - 1], arr[i]);
            }
        }
    }
} 


bool isZigZag(int[] arr, int n) {
    int f = 1;
    for(int i = 1; i < n; i++) {
        if (f) {
            if (arr[i - 1] > arr[i]) return 0;
        } else {
            if (arr[i - 1] < arr[i]) return 0;
        }
        f = f ^ 1;
    }
    return 1;
}

int main() {

    int n;
    cin >> n;
    int arr[n];

    for(int i = 1; i < n; i++) {
        cin >> arr[i];
    }

    Solution ob;
    ob.zigZag(arr, n);

    bool check = 1;
    check = isZigZag(arr, n);

    if (check) {
        cout << "1" << endl;
    } else {
        cout << "0" << endl;
    }
    
    return 0;
}
