#재귀 함수

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if target == array[mid]:
        return mid
    elif array[mid] > target:
        return binary_search(array, target,start, mid-1)
    else:
        return binary_search(array, target, mid+1,end)

#원소 갯수 n, 구하는 값 target
n, target = list(map(int, input().split())) #list로 저장하는 이유 map은 한번 입력받으면 한번만 사용가능한 list이기 때문에 list로 하면 반복사용 가능.

array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)


# 반복문

def binary_search_ex2(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if target == array[mid]:
            return mid
        elif array[mid] > target:
            return binary_search_ex2(array, target, start, mid-1)
        else:
            return binary_search_ex2(array, target, mid+1,end)
    return None

n , target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search_ex2(array,target,0,n-1)

if target == None:
    print("원소를 찾을 수 없습니다.")
else:
    print(result+1)

# 라이브러리 사용
# 오름차순으로 정렬되었을 때 사용가능
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x)) # x가 리스트에 들어가야할 처음 등장한 인덱스
print(bisect_right(a,x)) # x가 리스트에 들어가야할 마지막 인덱스 다음.


#데이터 갯수 찾기할 때

def count_value_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

print(count_value_range(a,4,4))
print(count_value_range(a,-1,3)) #해당 값 사이 갯수
