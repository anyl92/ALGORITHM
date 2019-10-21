# 정렬되어있지 않은 경우
def SequentialSearch(a, n, key):
    # a는 검색할 리스트, n은 길이인덱스?, key는 찾을 값
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1

# 정렬되어 있는 경우
def SequentialSearch2(a, n, key):
    i = 0
    i += 1
    while i < n and a[i] < key:  # key보다 검색할 값이 작을 때
        i += 1
    if i < n and a[i] == key:  # key와 같지 않으면
        return i
    else:                      # key보다 검색할 값이 크게 됨
        return -1