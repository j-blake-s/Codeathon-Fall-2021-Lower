from collections import defaultdict
n = int(input())
points = defaultdict(int)
for _ in range(n):
    left, right = input().split("->")
    points[left] += 1
    points[right] += 1
print(all(j == 2 for j in points.values()))
