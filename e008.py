#Project Euler #8: Largest product in a series

Count = int(input())

for j in range(Count):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input()
    output = int(0)
    temp = int(1)
    for i in range(n - k):
        for h in range(k):
            temp = temp * int(num[i+h])
        #print(temp)
        if (temp > output):
            output = temp
        temp = int(1)
    print(output)
