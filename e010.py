#Project Euler #10: Summation of primes

#Size of sieve
n = int(200000)

#the great sieve
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

#the rest

T = int(input())

for j in range(T):
    output = int(0)
    N = int(input())
    idx = 0
    while (ret[idx] <= N):
        output += ret[idx]
        idx += 1
    print(output)
    
