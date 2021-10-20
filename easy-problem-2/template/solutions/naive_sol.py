n = int(input())
nums = [int(x) for x in input().split()]
total = sum(nums)
while len(nums):
    nums.pop(-1)
    total += sum(nums)
    if len(nums):
        nums.pop(0)
        total += sum(nums)
print(total)


