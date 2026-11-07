def linear(target):
    for i in range(n):
        if lst[i] == target:
            print(i)
            return True
    print("-1")
    return False

def binary(lst, target, offset=0):
    if len(lst) == 0:
        print(-1)
        return False
    mid = len(lst) // 2
    if lst[mid] > target:
        return binary(lst[:mid], target, offset)
    elif lst[mid] < target:
        return binary(lst[mid+1:], target, offset+mid+1)
    else:
        print(offset + mid)
        return True

n = int(input())
lst = list(map(int, input().split()))
target = int(input())
linear(target)
binary(lst, target)