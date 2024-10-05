a = int(input())

# for i in range(1,a+1):
#     ill = i%10
#     if((ill%3==0) and (ill!=0)):
#         print("X",end=' ')
#     else:
#         print(i,end=' ')

for i in range(1,a+1):
    ill = i%10
    if ill in [3,6,9]:
        print("X",end= ' ')
    else:
        print(i,end=' ')