#두 개의 라이브러리는 클래스이므로 객체르 초기화한 이후에 리스트로 반환한다.

data = ["A","B","C"]

from itertools import permutations
#모든 경우의 수를 구함.
result = list(permutations(data,2))
print(result)

from itertools import combinations
#조합을 구함
result = list(combinations(data,2))
print(result)

from itertools import product
# 모든 순열을 구하지만 중복허용
result = list(product(data,repeat=2))
print(result)

from itertools import combinations_with_replacement
#조합을 구하지만 중복허용
result = list(combinations_with_replacement(data,2))
print(result)