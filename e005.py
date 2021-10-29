#Define helper array

arr = [1,2,3,2,5,1,7,2,3,1,
       11,1,13,1,1,2,17,1,19,1,
       1,1,23,1,5,1,3,1,29,1,
       31,2,1,1,1,1,37,1,1,1]

#Input
count = int(input())

for j in range(count):
    output = 1
    N = int(input())
    for i in range(N):
        output = output * arr[i]
    print(output)
