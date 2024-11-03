# while 문
i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)

# while 문
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)

result = 0

for i in range(1,10):
    result += i
print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(f"{i+1}번째 학생은 합격 입니다.")

scores = [90, 85, 77, 65, 97]
chat_list = {2,4}

for i in range(5):
    if i+1 in chat_list:
        continue
    if scores[i] >= 80:
        print(f"{i+1}번째 학생은 합격 입니다.")

for i in range(2, 10):
    for j in range(1,10):
        print(f"{i} X {j} = {i*j}")
print()
