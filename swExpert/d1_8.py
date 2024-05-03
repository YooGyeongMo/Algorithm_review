N = input()
#대문자 A = 65 소문자 a = 97 print(ord('B')) 하면 아스키 코드 뱉음 ord()

for i in N:
    if i == N[-1]:
        print(ord(i) - 64, end='')
        #맨뒤에 인덱스는 띄어쓰기 X
    else:
        print(ord(i) - 64, end=' ')
        #중간값들은 다 띄어쓰기 O