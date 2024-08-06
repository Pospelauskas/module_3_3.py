def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [54.32, 'точка', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
values_list_2 = [54.32, 'строка']


print_params()
print_params(b=25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(values_list_2)
print_params(*values_list_2, 42)
