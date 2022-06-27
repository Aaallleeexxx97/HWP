# # Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.
# # Если нужно поменять многочлен запустите Task33
# path = 'polinom.txt'
# f = open(path, 'r')
# data = f.read().split()
# f.close()

# print(data)

# path_one = 'polinom_1.txt'
# f_one = open(path_one, 'r')
# data_one = f_one.read().split()
# f.close()
# print(data_one)

# result = []
# sum = 0
# duplicate = 0

# if len(data) > len(data_one):
#     for i in range(0, len(data)-1):
#         if 'x' in data[i] or data[i] == '=':
#             for j in range(0, len(data_one)-1):
#                 if data[i] == data_one[j]:
#                     sum = str(int(data[i-1])+int(data_one[j-1]))
#                     result.append(sum + data_one[j])
#                     duplicate = 1
#                 else:
#                     uniqum = 1
#             if uniqum == 1 and duplicate == 0:
#                 result.append(data[i-1] + data[i])
#                 uniqum = 0
#             duplicate = 0   
# else:
#     for i in range(0, len(data_one)-1):
#         if 'x' in data_one[i] or data_one[i] == '=':
#             for j in range(0, len(data)-1):
#                 if data_one[i] == data[j]:
#                     sum = str(int(data_one[i-1])+int(data[j-1]))
#                     result.append(sum + data[j])
#                     duplicate = 1
#                 else:
#                     uniqum = 1
#             if uniqum == 1 and duplicate == 0:
#                 result.append(data_one[i-1] + data_one[i])
#                 uniqum = 0
#             duplicate = 0

# list= ' + '.join(result) + '0'
# with open('polynom_sum.txt', 'w') as sum:
#     sum.writelines(list)
# print(list)


# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом" 
# Вариант 1 Человек с человеком

# total = 50
# while total!=0:
#     a = int(input('Ход первого игрока от 1 до 6 конфет: '))
#     total -= a
#     print(f'Осталось конфет: {total}')
#     if total == 0:
#         print('Первый игрок проиграл!')
#         break
#     b = int(input('Ход второго игрока от 1 до 6 конфет: '))
#     total -= b
#     print(f'Осталось конфет: {total}')
#     if total == 0:
#         print('Второй игрок проиграл!')

# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах

# from encodings.utf_8 import encode

# path = 'input_data.txt'
# f = open(path, 'r', encoding='utf-8')
# data = list(f.read())
# f.close()

# def coding(list):
#     info = open('out_data.txt', 'a', encoding='utf-8')
#     cout = 1
#     for i in range(0, len(list)-1):
#         if list[i] == list[i + 1]:
#             cout += 1
#         else:
#             info.writelines(str(cout))
#             info.writelines(list[i])
#             cout = 1

#     info.writelines(str(cout))
#     info.writelines(list[-1] + '\n')
#     info.close()


# def decoding(list):
#     info = open('out_data.txt', 'a', encoding='utf-8')
#     for i in range(0,len(list)-1,2):
#         new_str = int(list[i]) * list[i+1]
#         info.writelines(new_str)
#     info.writelines('\n')
#     info.close()

# choice = int(input('Введите цифру 1 для кодирования или 2 для декодирования ' ))

# if choice == 1:
#     coding(data)
# elif choice == 2:
#     decoding(data)
# else:
#     print('Введены неверные данные!')
