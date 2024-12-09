print ('Введите последовательно 3 числа:')
first = int(input('Первое '))
second = int(input('Второе '))
third = int(input('Третье '))
if first == second and first == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print('0')