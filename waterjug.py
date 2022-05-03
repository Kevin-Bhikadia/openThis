# wj

from math import gcd


n = 3
m = 5
d = 4


def pour(fromCap, toCap, d):
    # fromv=0
    tov = 0
    step = 1

    fromv = fromCap

    while(fromv != d and tov != d):
        temp = min(fromv, toCap-tov)
        tov = tov+temp
        fromv = fromv-temp

        step = step+1

        if(fromv == d or tov == d):
            break

        if fromv == 0:
            fromv = fromCap
            step += 1
        if tov == toCap:
            tov = 0
            step += 1
    return step


def minSteps(n, m, d):
    if m < n:
        m, n = n, m
    if d > m:
        return -1
    if (d % gcd(n, m)) != 0:
        return -1

    return min(pour(n, m, d), pour(m, n, d))


print(minSteps(n, m, d))
