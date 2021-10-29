#Project Euler #9: Special Pythagorean triplet

#find all triplets < 3000
triples = []

for i in range(1, 3000):
    for j in range(i, 3000):
        c = i**2 + j**2
        if ((int(c**(1/2)))**2 == c):
            triples.append((i,j,int(c**(1/2))))

#start checkint N = a+b+c

T = int(input())

for i in range(T):
    N = int(input())
    output = int(-1)
    for (a,b,c) in triples:
        if (a + b + c == N):
            if (a*b*c > output):
                output = a*b*c
    print(output)
