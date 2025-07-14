def insertion_sort(a: list[int]) -> list:
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while(i>=0 and a[i]>key):
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
    return a

def insertion_sort_flipped(a: list[int]) -> list:
    j = len(a) - 2
    while j >= 0:
        key = a[j]
        i = j + 1
        while(i < len(a) and a[i] < key):
            a[i-1] = a[i]
            i = i + 1
        a[i-1] = key
        j = j - 1
    return a


        
