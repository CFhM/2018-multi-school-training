import os
import sys

def template(filepath):
    with open(filepath, 'w') as f:
        f.write('\
#include <bits/stdc++.h>\n\
using namespace std;\n\n\
typedef long long ll;\n\
typedef vector<int> vi;\n\
#define make_pair mp\n\
#define push_back pb\n\n\
const int mod = 1e9 + 7;\n\
const double pi = acos(-1.0);\n\
const int maxn = 1e5 + 5;\n')


def main():
    try:
        contest_dir_path = 'Round ' + sys.argv[1]
        problem_num = int(sys.argv[2])
    except IndexError:
        print 'Usage: python create_round.py <contest_round> <problem_number>\n \
               create a folder named \'Round <contest_round>\' contains <problem_number> serialized empty cpp files\n \
               you can also call template function to add your own headers to your cpp file.\n'
        return -1
    else:
        if not os.path.exists(contest_dir_path):
            os.mkdir(contest_dir_path)
            for i in range(1, problem_num + 1):
                filename = str(1000 + i) + '.cpp'
                open(os.path.join(contest_dir_path, filename), 'w')
                template(os.path.join(contest_dir_path, filename))


if __name__ == '__main__':
    main()