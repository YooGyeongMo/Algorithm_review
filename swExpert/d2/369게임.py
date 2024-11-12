N = int(input())

# data_list =[str(i) for i in range(1,N+1)]
# result_list = []
#
#
# for string in data_list:
#     clap_count = 0
#
#     for char in string:
#         if char in '369':
#             clap_count += 1
#
#     if clap_count > 0:
#         result_list.append("-" * clap_count)
#     else:
#         result_list.append(string)
#
# print(" ".join(result_list))


for i in range(1, N+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        clap_count = str(i).count('3') + str(i).count('6') + str(i).count('9')
        print("-"* clap_count, end=" ")
    else:
        print(i,end=" ")