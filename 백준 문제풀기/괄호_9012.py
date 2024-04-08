T = int(input())

for _ in range(T):
   stk = []
   isVPS = True
   for char in input():
       if char == '(': # ( 나오면 push 해야함
           stk.append(char)
       else: #닫는 괄호 나오면 실행 pop
           if stk:
               stk.pop()
           else:
               isVPS = False
               break
   if stk:
       isVPS = False

   print('YES' if isVPS else 'NO')