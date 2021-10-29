#Sum square difference

T = int(input())

for j in range(T):
    N = int(input())
    Sum_squares = int(N*(N+1)*(2*N+1)/6)
    Squared_sum = int(N*(N+1)/2)

    Squared_sum = Squared_sum**2
    output = Squared_sum - Sum_squares
    print(output)
