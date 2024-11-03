x = 15

if x >= 90:
    print("A")
elif 80 <= x:
    print("B")
elif 70 <= x:
    print("C")
else:
    print("F")

# not, and, or

# x in 리스트
# x not in 문자열


score = 85

if score >= 80: result = "Success"
else: result = "Fail"
print(result)

result = "Success" if score >= 80 else "Fail"
print(result)

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# result = []
# for i in a:
#     if i not in remove_set:
#         result.append(i)
#
# print(result)

result = [i for i in a if i not in remove_set]
print(result)