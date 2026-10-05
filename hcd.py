n = int(input())
m = int(input())
def hcd(n,m):
    if m ==0:
        return n
    else:
        return hcd(m,n%m)
print(hcd(n,m))
