row, col = 0, 0

for i in range(5):
    n = input().split()
    # print(n)
    for j in range(5):
        if n[j] == '1' and n[j] != '0':
            row, col = i, j
    
# print(row, col)
print(abs(2-row) + abs(2-col))