

def countw(listd, total):
    arr = [[None for x in range(total + 1)] for y in range(len(listd))]
    for i in range(total + 1):
        arr[0][i] = 1

    for i in range(len(listd)):
        arr[i][0] = 1

    for i in range(1, len(listd)):
        for j in range(1, total + 1):
            arr[i][j] = arr[i - 1][j] + \
                (0 if j - listd[i] < 0 else arr[i][j - listd[i]])

    return arr[len(listd) - 1][total]
