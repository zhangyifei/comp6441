def insert_sort(numberlist):
    size = len(numberlist)
    for i in range(size-1,0,-1):
        for j in range(i-1,-1,-1):
            if numberlist[i] > numberlist[j]:
                numberlist[i], numberlist[j] = numberlist[j], numberlist[i]

    print(numberlist)