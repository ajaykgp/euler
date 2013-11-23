
import math


def pfact(n):
    flist = []
    factor = None
    fpower = None

    if n % 2 == 0:
        factor = 2
        fpower = 0
        while n % 2 == 0:
            fpower += 1
            n /= 2
        flist.append((factor, fpower))

    if n % 3 == 0:
        factor = 3
        fpower = 0
        while n % 3 == 0:
            fpower += 1
            n /= 3
        flist.append((factor, fpower))

    factor = 5

    while factor <= math.sqrt(n):
        if n % factor == 0:
            fpower = 0
            while n % factor == 0:
                fpower += 1
                n /= factor
            flist.append((factor, fpower))

        if n % (factor + 2) == 0:
            fpower = 0
            while n % (factor + 2) == 0:
                fpower += 1
                n /= (factor + 2)
            flist.append((factor + 2, fpower))

        factor += 6

    if n > 1:
        flist.append((n, 1))

    # print flist
    return flist


def ephi(n):
    phinum = 1
    flist = pfact(n)

    for i in range(len(flist)):
        phifact = math.pow(flist[i][0], flist[i][1] - 1) * (flist[i][0] - 1)
        phinum *= phifact

    return phinum


def countfraction(n):
    count = 0
    for i in range(2, n + 1):
        count += ephi(i)
    return count

# pfact(60085147514378)

print int(countfraction(1000000))
