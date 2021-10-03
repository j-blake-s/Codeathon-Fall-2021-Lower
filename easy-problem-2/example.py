# "Shift Sift"

arr = [i for i in range(1,6)]

sum = 0

def print_pretty(arr):
    print('[',end ="")
    for i in arr:
        if(arr.index(i) == len(arr)-1):
            print("{}]".format(i))
        else:
            print(i,end = ",")
        
buffer = ""
shift_right = True;
while len(arr) > 0:
    for i in arr:
        sum += i
    print(buffer,end="")
    buffer +=" "
    print_pretty(arr)
    if(shift_right):
        shift_right = False
        arr.pop();
    else:
        shift_right = True
        arr.pop(0)

print("sum is: {}".format(sum))
