import sys

s = sys.stdin.readline().rstrip()

res = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        tmp = s[i:j+1]
        res.add(tmp)

print(len(res))