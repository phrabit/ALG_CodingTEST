n = int(input())

flag = True
cnt = 0

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            cnt+=1
            break;
print(n-cnt)