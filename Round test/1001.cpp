#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
#define make_pair mp
#define push_back pb

const int mod = 1e9 + 7;
const double pi = acos(-1.0);
const int maxn = 1e5 + 5;
// head

int main() {
    cout << "acm is funny!" << endl;
    int n; cin >> n;
    int sum = 0;
    for (int i = 0; i < n; ++i) {
        int a; cin >> a;
        cout << a << endl;
        sum += a;
    }
    cout << sum << endl;
    return 0;
}