class Solution {
    public: 
        vector<int> valueEqualToIndex(int arr[], int n) {
            vector<int> result;

            for(int i = 0; i < n; i++){
                if (i + 1 == arr[i]) {
                    result.push_back(arr[i]);
                }
            }

            return result;
        }
}

int main() {
    int n, i;
    cin >> n;

    int arr[n];

    for(int i = 0; i < n; i++) cin >> arr[i];

    Solution ob; 
    auto ans = ob.valueEqualToIndex(arr, n);

    if (ans.empty()) {
        cout << "Not Found";
    } else {
        for (int x: ans) cout << x << " ";
    }
     cout << "\n";

    return 0;
}