# a = input()
# a = int(a, 16)

# for i in range(1,16):
#     result = a * i
#     i = "%X"%i
#     result ="%X"%result
#     print("{}*{}={}".format("%X"%a,i,result),end='\n')

a = int(input(),16)

for i in range(1,16):
    result = a * i
    print(f"{a:X}*{i:X}={result:X}")