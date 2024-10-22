N = input().strip()

for alpabet in N:
    num = ord(alpabet) - 64
    print(num,end=' ')


N = input()
#대문자 A = 65 소문자 a = 97 print(ord('B')) 하면 아스키 코드 뱉음 ord()

for i in N:
    if i == N[-1]:
        print(ord(i) - 64, end='')
    else:
        print(ord(i) - 64, end=' ')
