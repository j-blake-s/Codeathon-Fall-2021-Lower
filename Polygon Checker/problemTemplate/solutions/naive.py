n = int(input())
points = []
for _ in range(n):
    left, right = input().split("->")
    points.append(left)
    points.append(right)
print(all(points.count(points[i]) == 2 for i in range(n)))