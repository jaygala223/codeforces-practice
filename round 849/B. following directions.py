t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    ans = "NO"
    row, col = 0, 0
    for c in s:
        if c == 'L':
            row -= 1
        elif c == 'R':
            row += 1
        elif c == 'U':
            col += 1
        else:
            col -= 1
        if row == 1 and col == 1:
            ans = "YES"
    
    if ans == "YES":
        print("YES")
    else:
        print("NO")