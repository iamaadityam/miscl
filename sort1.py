n = int(input())
lst = input()
lst = list(map(int, lst.split()))
def linear(n):
    for i in range(len(lst)):
        if lst[i] == n:
            print(i)
            return True
    return False
print(linear(n))