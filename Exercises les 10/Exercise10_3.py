##8_3A
# a=3
# def f(y):
#     global a
#     a=9
#     return 2*y + a
# print(a)
#
##antwoord is B
#
##8_3B
# x = 1
# y = 4
#
#
# def fun():
#     x = 2
#     global y
#     y = 3
#     print(y, end=' ')
# fun()
# print(y, end=' ')
#
##antwoord is D
##8_3C
# x = 2
# y = 5
#
#
# def fun():
#     y = 3
#     global x
#     x = 1
#     print(x*y, end=' ')
#     return x*y
#
# x = fun()
# print(x*y, end=' ')
#
##antwoord is A
##8_3D
# a=3
#
#
# def fun1():
#     global a
#     print("a:", a, end=' ')
#     b = 7
#     a = 0
#     return b
#
#
# def fun2(y):
#     a = y + fun1()
#     b = 7
#     a += 1
#     return a
#
#
# a = 9
# fun2(5)
# print("a:", a)
#
#antwoord is C
##8_3E
# x = 1
# y = 4
#
#
# def doe1():
#     global x
#
#
#     y = 7
#     x = 0
#     return y
#
#
# def doe2():
#     x = doe1()
#     x += 1
#     return x
#
#
# x = doe1()
# print(x)
#
#antwoord is C
##8_3G
x = 1
y = 3


def doe1():
    global x
    y = 4
    x = 0
    return x + y


def doe2():
    x = doe1()
    x += 2
    return x


doe2()
print(x)
##Antwoord is A