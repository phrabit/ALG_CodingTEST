str = input()

zero_cnt = 0
one_cnt = 0

tmp = str[0]
if tmp == "0":
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(1, len(str)):
    if tmp != str[i] and str[i] == "1":
        one_cnt += 1
        tmp = "1"
    elif tmp != str[i] and str[i] == "0":
        zero_cnt += 1
        tmp = "0"

print(one_cnt) if one_cnt < zero_cnt else print(zero_cnt)

