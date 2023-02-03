T = int(input())

#TC: O(3n) => O(n)
#SC: O(2n) + O(2n) => for distinct lists and sets

for t in range(T):
    n = int(input())
    s = input()
    distinct_left, left_set = [1]*n, set()
    distinct_right, right_set = [1]*n, set()
    right_set.add(s[-1])
    left_set.add(s[0])
    #left pass
    for i in range(1, n):
        if s[i] in left_set:
            distinct_left[i] = distinct_left[i-1]
        else:
            left_set.add(s[i])
            distinct_left[i] = distinct_left[i-1]+1
    
    #right pass
    for i in range(n-2, -1, -1):
        if s[i] in right_set:
            distinct_right[i] = distinct_right[i+1]
        else:
            right_set.add(s[i])
            distinct_right[i] = distinct_right[i+1]+1
    
    ans = 2
    
    for i in range(n-1):
        ans = max(ans, distinct_left[i] + distinct_right[i+1])
    print(ans)
