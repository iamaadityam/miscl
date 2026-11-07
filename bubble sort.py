lst = input()
lst = list(map(int, lst.split()))

def bubblesort(lst):
    for j in range(len(lst)):
        for i in range(1, len(lst)):
            if lst[i-1]>lst[i]:
                lst[i-1],lst[i] = lst[i],lst[i-1]
    return lst
print(bubblesort(lst))