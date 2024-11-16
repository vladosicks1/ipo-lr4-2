len = int(input("Введите длину cписка: ")) # определение длины списка

numbers=[0]*len # создание списка определенной длины

for i in range (0,len): # заполнение списка
    numbers[i] = int(input("Введите число: ")) 

numbers_2=[0]*len # создание нового списка

for i in range(0,len):
    numbers_2[i] = pow(numbers[i],2) # заполнение нового списка квадратами чисел первого списка

print(numbers_2)