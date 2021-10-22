from collections import defaultdict
cases = int(input())
for _ in range(cases):
    n = int(input())
    points = defaultdict(int)
    seen = set()
    for _ in range(n):
        left, right = input().split(" ")
        cur = tuple(sorted([left, right]))
        assert cur not in seen
        seen.add(cur)
        points[left] += 1
        points[right] += 1
    print(all(j == 2 for j in points.values()))
    # print(points.values())
    # print([j for j in points if points[j] == 3])
