def solution(s):
    li = list(map(int, s.split()))
    max_num = max(li)
    min_num = min(li)
    return f"{min_num} {max_num}"