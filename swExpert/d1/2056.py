# N = input()
#
# num_list = [digits for digits in N]
#
# year = (num_list[0:4])
# month = (num_list[4:6])
# day = (num_list[-3:-1])
#
# print(month)


T = int(input())

for test_case in range(1,T+1):
    num_list = input()
    y = num_list[0:4]
    m = num_list[4:6]
    d = num_list[6:]
    if(int(m) in [1,3,5,7,8,10,12] and (0<int(d)<32)):
        print(f"#{test_case} {y}/{m}/{d}")
    elif(int(m) in [4,6,9,11] and (0<int(d)<31)):
        print(f"#{test_case} {y}/{m}/{d}")
    elif(int(m)==2 and 0<int(d)<29):
        print(f"#{test_case} {y}/{m}/{d}")
    else:
        print(f"#{test_case} -1")

