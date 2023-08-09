def solution(n):
    bin_cnt = bin(n)[2:].count('1')
    num = n+1
    while True:
        num_cnt = bin(num)[2:].count('1')
        if num_cnt==bin_cnt:
            return num;
        else:
            num += 1
        