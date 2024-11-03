# 키와 값을 쌍으로 가지는 데이터

# 리스트나 튜플은 순차적으로 저장한다는 특징.

# 사전 자료형은 내부적으로 해시테이블을 사용하므로 O(1) 시간

# 리스트보다 훨씬 빠름

data = dict()
data['사과'] = "apple"
data['바나나'] = 'banana'
data['망고'] = 'mango'
data['사과'] = "appler"
print(data)

#키만 뽑아낼때는 keys()함수 사용
#값만 뽑아낼때는 values() 사용

#키만 뽑아낸 리스트
key_list = data.keys()
#값만 뽑아낸 리스트
value_list = data.values()

print(key_list)
print(value_list)

for key in key_list:
    print(key)
