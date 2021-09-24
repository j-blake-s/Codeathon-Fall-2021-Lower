# "Shift Sift"

arr = [i for i in range(10)]

sum = 0

right = True;
while len(arr) > 0:
    for i in arr:
        sum += i
        print(i)
    if(right):
        right = False
        arr.pop(0);
    else:
        right = True
        arr.pop()

print("sum is: {}".format(sum))
