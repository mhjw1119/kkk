# 복합 연산자
y = 10
y -= 4
# y = y - 4
print(y)  # 6

z = 7
z *= 2
print(z)  # 14

w = 15
w /= 4
print(w)  # 3.75

q = 20
q //= 3
print(q)  # 6


# 비교 연산자
print(3 > 6)  # False

# == 비교 연산자
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False

# is 비교 연산자
# SyntaxWarning: "is" with a literal. Did you mean "=="?
print(1 is True)  # False
print(2 is 2.0)  # False

# 왜 is 대신 ==를 사용해야 하나?
print(1 is True)  # False
print(2 is 2.0)  # False
print(1 == True)  # True
print(2 == 2.0)  # True

# is 연산자는 언제 사용하는가?
x = None

# 권장
if x is None:
    print('x는 None입니다.')

# 비권장
if x == None:
    print('x는 None입니다.')


# 싱글턴 객체
x = True
y = True

# True, False, None은 실제로 같은 객체를 가리킨다.
print(x is y)  # True
print(True is True)  # True
print(False is False)  # True
print(None is None)  # True

# 추가 예시: 리스트나 객체 비교
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (두 리스트의 값은 동일)
print(a is b)  # False (서로 다른 리스트 객체)

# b가 a를 그대로 참조하도록 할 경우
b = a
print(a is b)  # True (같은 객체를 가리키므로 True)


# 논리 연산자
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print(not 0)  # True


# 논리 연산자 & 비교 연산자
num = 15
result = (num > 10) and (num % 2 == 0)
print(result)  # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result)  # True
