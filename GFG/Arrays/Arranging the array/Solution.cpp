void rearrange(int[] arr, int n) {
    vector<int> temp;

    for (int i=0; i<n; i++) {
        if (arr[i] < 0) temp.push_back(arr[i]);
    }

    for (int i=0; i<n; i++) {
        if (arr[i] >= 0) temp.push_back(arr[i]);
    }

    for (int i=0; i < n; i++) {
        arr[i] = temp[i];
    }
}

int main() {

    int n;
    cin >> n;
    int arr[n];

    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long j = 0;

    rearrange(arr, n);

    for (int i=0; i<n; i++) cout << arr[i] << " ";

    cout << endl;

    return 0;
}