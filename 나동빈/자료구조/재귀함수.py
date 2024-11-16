# def recursive_function():
#     print('재귀 함수를 호출합니다.')
#     recursive_function()
#
# recursive_function()

def recursive_function2(i):
    if i == 100:
        return
    print(i,'번째 재귀함수에서',i+1,'번째 재귀함수를 호출합니다.')
    recursive_function2(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function2(1)