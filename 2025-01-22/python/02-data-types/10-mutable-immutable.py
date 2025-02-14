# immutable (불변)
my_str = 'hello'
my_str[0] = 'z'  # TypeError: 'str' object does not support item assignment

# mutable (가변)
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]
