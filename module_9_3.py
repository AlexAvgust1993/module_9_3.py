first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(len(f) - len(s))
                for f, s in zip(first, second)
                if len(f) != len(s))


second_result = (len(first[i]) == len(second[i])
                 for i in range(min(len(first), len(second))))


print(list(first_result))
print(list(second_result))









# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 100 for x in my_numbers)
# print(result)
#
# for elem in result:
#     print(elem)



# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 1000 for x in my_numbers)
#
# for elem in result:
#     print(elem)
#
# print('Ещё разок')
#
# for elem in result:
#     print(elem)



# import time
#
# start_time = time.time()
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = (x ** 3000 for x in my_numbers)
# print(result)
#
# for i in result:
#     print(i)
#
#
# finish_time = time.time()
# print(f'Время в миллисекундах: {(finish_time-start_time)*1000}')


# list_1 = [1, 5, 9, 29, 4]
# list_2 = [5, 2, 9, 1, 2]
#
# ran = range(10, 30)
# zp = zip(list_1, list_2)
# mp = map(str, list_1)
#
# print(ran, zp, mp)
#
# print(list(ran))
# print(list(zp))
# print(list(mp))







