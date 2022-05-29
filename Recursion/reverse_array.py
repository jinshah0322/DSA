# Practice - https://bit.ly/3yHCsYL
def reverseArrayhelper(arr, i, j):
    if(i >= j):
        return arr
    a = arr[i]
    arr[i] = arr[j]
    arr[j] = a
    return reverseArrayhelper(arr, i+1, j-1)


def reverseArray(arr, m):
    return reverseArrayhelper(arr, m+1, len(arr)-1)


t = int(input())
while t > 0:
    n, m = map(int, input().split())
    l = input()
    l = l.split()
    print(reverseArray(l, m))
    t -= 1
