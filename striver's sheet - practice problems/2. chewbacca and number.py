#https://codeforces.com/contest/514/problem/A

n = list(str(input()))

for i in range(len(n)):
    if i == 0 and n[i] == '9':
        continue
    if n[i] in ['5','6','7','8','9']:
        num = int(n[i])
        n[i] = str(9 - num)
x = "".join(n)
print(int(x))