# 튜플은 한 번 선언된 값은 변경할 수 없다.
# 리스트는 [] 튜플은 ( )

# 튜플 자료형은 그래프 사용시 자주 이용
# 다익스트라 최단 경로 알고리즘
# 우선순위 큐에 한 번 들어간 값은 변경되지 않는다.

# 본인의 알고리즘이 잘못 작동되어 튜플의 값을 변경 즉, 변경하면 안되는 값이 변경되고 있는지 체크 가능하다.
a = (1, 2, 3, 4)
print(a)

a[3] = 2
