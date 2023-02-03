n, k, l, c, d, p, nl, np = (input().split())
ans = 1e9

ans = min(ans, (int(k)*int(l)) // int(nl), (int(c)*int(d)), int(p) // int(np))

print(ans // int(n))