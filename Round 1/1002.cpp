#include <bits/stdc++.h>
using namespace std;

const int maxn = 1e5 + 5;

struct Seq {
    int left, right;
} s[maxn];

char str[maxn];

int main() {
    int T;
    scanf("%d", &T);
    while (T--) {
        int n, ans = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%s", str);
            int len = strlen(str);
            s[i].left = s[i].right = 0;
            for (int j = 0; j < len; ++j) {
                if (str[j] == '(') {
                    s[i].left++;
                } else {
                    if (s[i].left > 0) {
                        s[i].left--;
                        ans += 2;
                    } else {
                        s[i].right++;
                    }
                }
            }
        }

        sort(s, s + n, [&](Seq &a, Seq &b) {
            if (a.left >= a.right) {
                if (b.left >= b.right) {
                    return a.right < b.right;
                } else {
                    return true;
                }
            } else {
                if (b.left >= b.right) {
                    return false;
                } else {
                    return a.left > b.left;
                }
            } 
        });

        int l = s[0].left;
        for (int i = 1; i < n; ++i) {
            int length = min(s[i].right, l);
            ans += length * 2;
            (l -= length) += s[i].left;
        }

        printf("%d\n", ans);
    }

    return 0;
}