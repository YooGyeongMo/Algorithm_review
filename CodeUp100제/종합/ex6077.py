n = int(input())

# result = 0
#
# for i in range(1,n+1):
#     if(i%2==0):
#         result += i
#
# print(result)

result = 0
i = 1
while(i<n+1):
    if(i%2==0):
        result +=i
    i+=1

print(result)