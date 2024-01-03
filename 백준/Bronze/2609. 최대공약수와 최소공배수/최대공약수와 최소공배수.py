m,n = map(int, input().split())

def gcd(m, n):
    if m%n == 0:
        return n
    else:
        return gcd(n, m%n)

gcd = gcd(m,n)
lcm = gcd*(m//gcd)*(n//gcd)

print(gcd)
print(lcm)

