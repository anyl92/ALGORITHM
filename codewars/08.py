# def increment_string(strng):
#     f = False
#     numslice = strslice = slicenum = strsum = lencheck = ''
#     li = list(strng)
#     number = list(map(str, list(range(0, 10))))

#     try:
#         if len(strng) > 20:
#             strslice = strng[:-3]
#             strng = strng[-3:len(strng)]
#         if type(int(strng)) == int:
#             if strng[-1] == '9':
#                 lencheck = int(strng)+1
#                 while len(strng) != len(str(lencheck)):
#                     lencheck = '0' + str(lencheck)
#                     return strslice+lencheck
#             return str(int(strng)+1)
#     except:
#         for i in strng:
#             for j in number:
#                 if i == j:
#                     slicenum = strng.index(i)
#                     f = True
#                 if f:
#                     break
#             if f:
#                 break
        
#         if slicenum:
#             numslice = strng[slicenum:]  # 001
#             strslice += strng[:slicenum]
#             strsum += str(int(numslice)+1)  # 2
#             if numslice == len(numslice) * '9':
#                 return strslice + strsum
#             while len(numslice) != len(strsum):
#                 strsum = '0' + strsum
#             return strslice + strsum
#         else:
#             return strng+'1'

"""
스트링 뒤에서부터 하나씩 보며 숫자인지 비교함 dz
숫자이면 다른 스트링에 저장함 dz
나머지 남은거만 또 다른 스트링에 저장함 dz
숫자 안나오면 브레이크로 나가고 dz
없으면 없는대로 비워둠 dz
숫자만뽑은거 인트처리해서 +1하고 자릿수맞춰서 리턴 
맨뒤가 문자이면 다문자임 걍바로 문자뒤에 +1해서 리턴ㅇㅋ
"""

def increment_string(strng):
    count = 0
    numslice = strslice = lencheck = ''  # 숫자자른거, 문자자른거, 문자합치거, 길이체크
    reverse_str = list(strng[::-1])  # 입력값 리버스해서 리스트로
    number = list(map(str, list(range(0, 10))))  # 숫자비교할 스트링

    if strng=='' or reverse_str[0] not in number:
        return strng+'1'

    for c in reverse_str:  # 스트링 문자 하나씩 돈다
        if c in number:  # 문자가 숫자이면
            numslice = c + numslice  # 숫자를 앞에서부터 끼워넣고 숫자만 저장
            count += 1  # 넣을때마다 카운트
        else:
            break  # 숫자 안나오면 포문 브레이크    
    strslice = strng[:len(strng)-count]  # 전체길이-카운트수 까지 슬라이싱해서 문자만 저장

    if numslice == '9'*(len(numslice)):
        lencheck = str(int(numslice) + 1)  # 인트로 +1계산후 다시 스트링
        return strslice+lencheck
    else:
        lencheck = str(int(numslice) + 1)
        while len(numslice) != len(lencheck):
            lencheck = '0' + lencheck
        return strslice+lencheck

print(increment_string("foobar001"))
#print(increment_string("Go`[2B\\20<l930>J\\p7`us'(cm083346569000965919"))


def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


def increment_string(strng):
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')
    
    # get the part of strng that was stripped
    ints = strng[len(stripped):]
    
    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)
    
        # add 1 to ints
        new_ints = 1 + int(ints)
    
        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)
    
        return stripped + new_ints