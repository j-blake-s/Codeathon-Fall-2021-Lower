t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    smallest = nums[0]
    best_profit = -400_001
    for i in range(1, n):
        best_profit = max(best_profit, nums[i] - smallest)
        if smallest > nums[i]:
            smallest = min(smallest, nums[i])
        else:
            best_profit = max(best_profit, nums[i] - smallest)
    print(best_profit)