from collections import deque
n = int(input())
nums = [int(x) for x in input().split()]
total = sum(nums)
nums = deque(nums)
answer = total
MOD = 1000
DEBUG = True
if DEBUG: print("[", *nums, "]", "-> sum =", answer)
answer = answer % MOD
if DEBUG: print("remaining after bagging", answer)

while nums:
    nums.rotate()
    total -= nums.popleft()
    answer += total
    if DEBUG and len(nums):
        print("[", *nums, "]", "-> sum + remaining =", answer)
    answer = answer % MOD
    if DEBUG:
        print("remaining after bagging:", answer)
    if len(nums):
        total -= nums.popleft()
        answer += total
        if DEBUG and len(nums) > 0:
            print("[", *nums, "]", "-> sum + remaining =", answer)
    answer = answer % MOD
    if DEBUG:
        print("remaining after bagging:", answer)
if answer > 2140000000:
    assert False
print(answer)


