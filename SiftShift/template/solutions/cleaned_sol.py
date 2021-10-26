from collections import deque
n = int(input())
nums = [int(x) for x in input().split()]
total = sum(nums)
nums = deque(nums)
answer = total
MOD = 1000
answer = answer % MOD

while nums:
    nums.rotate()
    total -= nums.popleft()
    answer += total
    answer = answer % MOD
    if len(nums):
        total -= nums.popleft()
        answer += total
    answer = answer % MOD
if answer > 2140000000:
    assert False
print(answer)


