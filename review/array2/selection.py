# 정렬시킨 후 k번째를 selection
def select(list, k):
    for i in range(0, k):
        minidx = i
        for j in range(i+1, len(list)):
            if list[minidx] > list[j]:
                minidx = j
        list[i], list[minidx] = list[minidx], list[i]
    return list[k-1]

def SelectionSort(a):  # [64, 25, 10, 22, 11]
    for i in range(len(a)-1):  # 0-4
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:  # 10 > 22
                min = j  # 10
        a[i], a[min] = a[min], a[i]