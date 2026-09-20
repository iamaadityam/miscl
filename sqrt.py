N = int(input(""))
up = N
low = 0

mean = (up+low)/2
while abs(mean**2 - N)> 0.000001:
    if mean**2-N > 0:
        up = mean
        mean = (up+low)/2

    elif mean**2-N < 0:
        low = mean
        mean = (up+low)/2
        
print(mean)