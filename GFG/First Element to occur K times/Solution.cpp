class Solution {
    public:
        int firstElementKTimes(int[] a, int n, int k) {
            map<int, int> mp;

            for(int i = 0; i < n; i++) {
                if (mp.count(a[i]) > 0) {
                    mp[a[i]] += 1;
                } else {
                    mp[a[i]] = 1;
                }

                if (mp[a[i]] == k) return a[i];
            }

            return -1;
        }
}

int main() {

    int n, k;
    cin >> n >> k;
    int a[n];
    for(int i=0; i<n; i++) {
        cin >> a[i];
    }

    Solution ob;

    cout << ob.firstElementKTimes(a, n, k) << endl;

    return 0;
}