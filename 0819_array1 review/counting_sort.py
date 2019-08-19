def Counting_Sort(A, B, k):
    A = [0, 4, 1, 3, 1, 2, 4, 1]
    B = [0] * len(A)  # 정렬될 배열
    C = [0] * k  # 카운트 배열

    for i in range(0, len(B)):
        C[A[i]] += 1  # C = A의 원소 수 인덱스에 값을 1씩 증가
    for i in range(1, len(C)):
        C[i] += C[i-1]  # C의 인덱스값을 차례로 누적시킴
    for i in range(len(B)-1, -1, -1):
        # A원소의 카운팅/누적 갯수에서 -1을 뺀 값을 B의 인덱스로 A원소값 추가
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1  # A원소의 카운팅 누적된 갯수에서 1씩 감소시킴