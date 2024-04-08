T = int(input())

for _ in range(T):
    stk = [] # stack 생성
    isVPS = True
    for char in input(): # char로 나눔 string 을
        if char == '(':
            stk.append(char) # push
            print(char)
        else:
            if stk: # 아직 stk에 남아있으면
                stk.pop() # 팝
                print(char)
            else: # 없으면 false
                isVPS = False
    if len(stk):
        isVPS = False

    print("YES" if isVPS else "NO")
    #[true_value] if [condition] else [false_value] // 파이썬 지원
