arr = [8,5,3,20,2,6,1]
l = len(arr)
def min(m):
    k = m[0]
    for el in m:
        if el < k:
            k = el
    return k
print(min(arr))
def average(f):
    s = 0
    for el in f:
        s += el
    return s / len(f)
print(average(arr))
