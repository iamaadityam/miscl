def tower_of_hanoi(n, src, aux, dest):
    if n == 1:
        print(src, "to", dest)
        return
    tower_of_hanoi(n-1, src, dest, aux)
    print(src, "to", aux)
    tower_of_hanoi(n-1, aux, src, dest)