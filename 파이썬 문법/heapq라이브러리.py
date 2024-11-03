#우선순위 큐 기능, 다익스트라 구현 시
# 원소를 힙에 넣었다가 빼는것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# 최소 힙 자료구조의 최상단 원소는 '가장 작은 원소'이기 때문이다.

import heapq

def heapsort(iterable):
    h = []
    result = []
    #모든 원소를 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) # 마지막 노드에 들어가고 부모노드와 비교해서 최종적으로는 루트까지가서 min heap으로 최소값이 맨 꼭대기로 올라감.
    for _ in range(len(h)):
        result.append(heapq.heappop(h)) #루트 부터 팝
    return result

print(heapsort([5,6,7,1,0,3,4]))

def max_heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h,-value) #max heap -를 붙이면 -큰값일 수록 가장 작은값이 되기에 맨위로
    for _ in range(len(h)):
        result.append(-heapq.heappop(h)) # -를 붙인것을 -를 붙이면 양수가 된다.
    return result

print(max_heapsort([5,6,7,1,0,3,4]))

