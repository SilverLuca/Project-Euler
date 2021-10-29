#Project Euler #7: 10001st prime
n = int(200000)

boolar = [0]*2 + [1]*(n-2)

sqrtn = int(n**(1/2)) + 1

for i in range(sqrtn):
    if boolar[i]:
        j = i**2 - i
        while (j := j + i) < n:
            boolar[j] = 0
ret = []

for (idx, i) in enumerate(boolar):
    if i:
        ret.append(idx)

T = int(input())

for j in range(T):
    N = int(input())
    print(ret[N - 1])
