# 2018-multi-school-training

## create new round

run script as

``` powershell
python create_round.py <round_name> <problem_num>
```

then you will get a folder named 'Round <round_name>', with <problem_num> cpp files named as 1001.cpp, 1002.cpp, ... 

call `template` function to preprocess your every cpp file with a header.

As a sample:

```cpp
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

```

## Some acm-checking-answer tricks

please read

[ACM比赛常用技巧](https://zhuanlan.zhihu.com/p/33080292)

## for any question

contact CFhM_R@outlook.com or

open an issue