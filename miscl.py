lls = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lls.append([name, score])
lowest = lls[0][1]
for i in range(len(lls)):
    if lls[i][1] > lowest:
        lowest = lls[i][1]
        j = i
        print(lls[j][0])