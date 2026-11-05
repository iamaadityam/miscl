def linear(target):
    for i in range(n):
        if lst[i] == target:
            print(i)
            return True
    print("-1")
    return False

def binary(lst, target):
    mid = len(lst) // 2
    if len(lst) == 0:
        return False
    if lst[mid] > target:
        lst = lst[:mid]
        binary(lst, target)
    if lst[mid] < target:
        lst = lst[mid:]
        binary(lst, target)
    if lst[mid] == target:
        print(len(lst))
        return True
        
n = int(input())
lst = input()
lst = list(map(int, lst.split()))
target = int(input())
linear(target)
binary(lst, target)