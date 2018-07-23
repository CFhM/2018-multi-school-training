#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n;
        scanf("%d", &n);
        if (n % 3 == 0) {
            printf("%lld\n", 1LL * n * n * n / 27LL);
        } else if (n % 4 == 0) {
            printf("%lld\n", 1LL * n * n * n / 32LL);
        } else {
            puts("-1");
        }
    }

    return 0;
}