#Find list of all palindromes
palindrome = []

for i in range(100,1000):
    for j in range(100,1000):
        a = i * j
        if (str(a) == str(a)[::-1]) and a not in palindrome:
            palindrome.append(a)
palindrome.sort()
lenght = len(palindrome)

#How many inputs?
count = int(input())

#Find largest element less then N
for j in range(count):
    N = int(input())
    for i in range(lenght+1):
        if (palindrome[i] >= N):
            print(palindrome[i - 1])
            break
