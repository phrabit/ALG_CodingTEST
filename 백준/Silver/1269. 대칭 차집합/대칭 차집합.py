n, m = map(int, input().split())

A_li = list(map(int, input().split()))
B_li = list(map(int, input().split()))

A = dict()
B = dict()

cnt1 = 0
cnt2 = 0

for i in A_li:
    A[i] = A.get(i, 0) + 1
for i in B_li:
    A[i] = A.get(i, 0) - 1
for key,value in A.items():
    if value == 1:
        cnt1 += 1

for i in B_li:
    B[i] = B.get(i, 0) + 1
for i in A_li:
    B[i] = B.get(i, 0) - 1
for key,value in B.items():
    if value == 1:
        cnt2 += 1

print(cnt1 + cnt2)