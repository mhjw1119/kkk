# 문자열 표현
print('Hello, World!')  # Hello, World!
print(type('Hello, World!'))  # str

# 중첩 따옴표
print(
    '문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.'
)  # 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
print(
    "문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다."
)  # 문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.

# Escape sequence
print('철수야 \'안녕\'')
print('이 다음은 엔터\n입니다.')


# String Interpolation "f-string"
bugs = 'roaches'
counts = 13
area = 'living room'

print(f'Debugging {bugs} {counts} {area}')


# 문자열의 시퀀스 특징
my_str = 'hello'
# 1. 인덱싱
print(my_str[1])  # e

# 2. 슬라이싱
print(my_str[2:4])  # ll
print(my_str[:3])  # hel
print(my_str[3:])  # lo
print(my_str[0:5:2])  # hlo
print(my_str[::-1])  # olleh

# 3. 길이
print(len(my_str))  # 5

# 4. 문자열은 불변
# TypeError: 'str' object does not support item assignment
my_str[1] = 'z'

# 재할당 (문자열을 바꾼 것이 아님)
my_str = 'hzllo'
