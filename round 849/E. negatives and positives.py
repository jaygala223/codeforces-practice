T = int(input())



for t in range(T):
    n = int(input())
    arr = []
    inp = input().split()
    for item in inp:
        arr.append(int(item))
    # print(arr)

    total = sum(arr)

    memo = {}

    def func(ind, curr):
        if ind == n-1:
            return curr
        # if (ind, curr) in memo:
        #     return memo[(ind, curr)]

        #operate
        arr[ind], arr[ind+1] = -arr[ind], -arr[ind+1]
        
        op = func(ind+1, sum(arr))
        
        arr[ind], arr[ind+1] = -arr[ind], -arr[ind+1]
        
        #dont operate
        non_op = func(ind+1, curr)
        
        # memo[(ind, curr)] = max(op, non_op)
        # return memo[(ind, curr)]
        return max(op, non_op)
    
    print(func(0, total))