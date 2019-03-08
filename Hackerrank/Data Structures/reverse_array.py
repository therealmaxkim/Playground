def reverseArray(a):
    for i in range(0, len(a)//2):
        a[i], a[len(a)-1-i] = a[len(a)-1-i], a[i]
    return a
