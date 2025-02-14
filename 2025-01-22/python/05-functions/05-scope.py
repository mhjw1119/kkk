# Scope 예시
def func():
    num = 20
    print('local', num)  # local 20

func()

print('global', num)  # NameError: name 'num' is not defined


# LEGB Rule 퀴즈
a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  #

    local(500)
    print(a, b, c)  #


enclosed()

print(a, b)  #
