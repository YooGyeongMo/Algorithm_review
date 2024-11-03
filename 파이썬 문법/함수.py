def add(a,b):
    return a+b

print(add(3,6))

def add(a,b):
    print(f"함수의 결과 : {a+b}")

add(3,6)

def add(a,b):
    print(f"a는 {a}, b는 {b}")

add(b=5,a=2)


a = 0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

print((lambda a, b: a + b)(3,7))

