S = input()

arr = [-1] * 26

for i in range(len(S)):
    target = ord(S[i]) - ord('a')
    if arr[target] == -1:
        arr[target] = i

for i in arr:
    print(int(i),end = " ")




S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')