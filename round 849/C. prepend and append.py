t = int(input())

for i in range(t):
    n = int(input())
    s = input()

    l, r = 0, n-1
    while l < r and s[l] != s[r]:
            l += 1
            r -= 1
        
    print(r - l + 1)
