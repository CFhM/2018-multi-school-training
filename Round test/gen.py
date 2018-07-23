import random

with open('in.txt', 'w') as f:
    n = random.randint(1, 10)
    f.write('%d\n' %(n))
    for i in range(n):
        f.write('%d ' %(random.randint(1, 10)))
    f.write('\n')