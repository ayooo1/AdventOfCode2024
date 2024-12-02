file = open('Day 2\input.txt','r')

def check(arr):
    
    inc = arr[1] - arr[0] > 0

    if double_check(arr[1:]):
        return 1
    if double_check(arr[:-1]):
        return 1

    for i in range(1,len(arr)):
        if 3 >= abs(arr[i] - arr[i-1]) > 0:
            if arr[i] - arr[i-1] < 0 and inc:
                if double_check(arr[:i] + arr[i+1:]) or double_check(arr[:i-1] + arr[i:]):
                    return 1
                else:
                    return 0
            if arr[i] - arr[i-1] > 0 and not inc:
                if double_check(arr[:i] + arr[i+1:]) or double_check(arr[:i-1] + arr[i:]):
                    return 1
                else:
                    return 0
        else:
            if double_check(arr[:i] + arr[i+1:]) or double_check(arr[:i-1] + arr[i:]):
                return 1
            else:
                return 0


    return 1

def double_check(arr):
    inc = arr[1] - arr[0] > 0
    for i in range(1,len(arr)):
        if 3 >= abs(arr[i] - arr[i-1]) > 0:
            if arr[i] - arr[i-1] < 0 and inc:
                return 0
            if arr[i] - arr[i-1] > 0 and not inc:
                return 0
        else:
            return 0


    return 1

ans = 0
for line in file.readlines():
    ans += check([int(x) for x in line.split()])

print(ans)