def BinarySearch(a, key):
    start = 0
    end = len(a)-1
    while start != end:
        mid = (start + end) // 2
        if a[mid] == key:
            return True
        elif a[mid] > key:
            end = mid -1
        else:
            start = mid +1
    return False

# 재귀
def BinarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return BinarySearch2(a, low, mid-1, key)
        elif a[mid] < key:
            return BinarySearch2(a, mid+1, high, key)