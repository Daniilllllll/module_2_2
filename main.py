first = int(input("Число: "))
second = int(input("Число: "))
third = int(input("Число: "))

if first == second == third:
    print('3')
elif first == third or first == second or second == third:
    print('2')
else:
    print('0')
