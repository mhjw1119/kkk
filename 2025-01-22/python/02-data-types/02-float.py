# 실수 자료형
d = 3.14
e = -2.7

# 지수 표현
# 314 ∗ 0.01
number = 314e-2

print(number)  # 3.14
print(type(number))  # float

# 유한 정밀도
print(2 / 3)  # 0.6666666666666666
print(5 / 3)  # 1.6666666666666667

# 부동소수점 에러
# 해결 전
a = 3.2 - 3.1
b = 1.2 - 1.1

print(a)  # 0.10000000000000009
print(b)  # 0.09999999999999987
print(a == b)  # False

# 해결 후
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)  # 0.1
print(b)  # 0.1
print(a == b)  # True
