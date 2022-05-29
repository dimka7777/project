top5 = 'Первые 5 мест на соревнованиях: 1. иванов 2. петров 3. сидоров 4. орлов 5. соколов'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
result = 'Поздравляем {} с успехом!'.format(top3.upper())
print(result)

# friends = ['Max', 'Leo', 'Kate']
# print(friends)
# print(len(friends))
#
# friends.append('Ron')
# print(friends)
# print(len(friends))
#
# print(friends.pop())
# print(friends)
#
# friends.clear()
# print(friends)
#
# friends = ['Max', 'Leo', 'Kate']
# friends.remove('Kate')
# print(friends)
#
# del friends[0]
# print(friends)

# hero = 'Superman'
# if hero.find('man') != -1:
#     print('Есть')
# if 'man' in hero:
#     print('Есть')
#
# goals = ['стать гуру языка python', 'здоровье', 'накормить кота']
#
# if 'здоровье' in goals:
#     print('Всё хорошо')


# print('Соревнования по PYTHON')
# num_mem = input('Введите количество участников:')
# while not num_mem.isnumeric():
#     print("Вы ввели не число!")
#     num_mem = input('Введите количество участников:')
#
# list_mem = []
# int_num_mem = int(num_mem)
# while int_num_mem >= 1:
#     list_mem.append(input("Кто занял {} место?:".format(int_num_mem)))
#     int_num_mem -= 1
# list_mem.reverse()
# print("В соревновании участвовали:",sorted(list_mem))
# list_first_3 = list_mem[:3]
# print("Победители:{} Поздравляем!".format(list_first_3))

# friends = ['Last','Mate','Tate']
# friends.reverse()
# for friend in friends:
#     friend = reversed(friend)
#     for letter in friend:
#         print(letter)

#
# for i in range(1,1000,2):
#     print(i)

# friend = {
#     'name': 'Max',
#     'age': 23
# }
#
# print(friend)
# print(friend['age'])
# friend['has_car']=True
# print(friend)
#
# cities = {'Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow'}
# print(type(cities))
# cities.add('Tom')
# print(cities)
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# my_list_3 = []
# # Решение 1
# for item in my_list_2:
#     for i in range(len(my_list_1)):
#         if item == my_list_1[i]:
#             my_list_3.append(i)
# my_list_3.reverse()
# for i in my_list_3:
#     del my_list_1[int(i)]
# print(my_list_1)
# # # Решение 2
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# my_list_1 = set(my_list_1)
# my_list_2 = set(my_list_2)
# my_list_3 = my_list_1 - my_list_2
# my_list_3 = list(my_list_3)
# print(my_list_3)
# # Решение 3 (не моё)
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# for i in my_list_2:
#     while i in my_list_1:
#         my_list_1.remove(i)
# print(my_list_1)

# # Решение 4 (не моё)
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]
# for i in my_list_1[:]:
#     if i in my_list_2:
#         my_list_1.remove(i)
# print(my_list_1)

# data = "02.11.2013"
# day, month, year = data.split('.')
# day_list = {
#     '00': 'нет дня',
#     '01': 'первое',
#     '02': 'второе',
#     '03': 'третье',
#     '05': 'четвёртое',
#     '06': 'четвёртое',
#     '07': 'четвёртое',
#     '08': 'четвёртое',
#     '09': 'четвёртое',
#     '10': 'четвёртое',
#     '11': 'четвёртое',
#     '12': 'четвёртое',
#     '13': 'четвёртое',
#     '14': 'четвёртое',
#     '15': 'четвёртое',
#     '16': 'четвёртое',
#     '17': 'четвёртое',
#     '18': 'четвёртое',
#     '19': 'четвёртое',
#     '20': 'двадцать',
#     '21': 'четвёртое',
#     '22': 'четвёртое',
#     '23': 'четвёртое',
#     '24': 'четвёртое',
#     '25': 'четвёртое',
#     '26': 'четвёртое',
#     '27': 'четвёртое',
#     '28': 'двадцать восьмое',
#     '29': 'двадцать девятое',
#     '30': 'тридцатое',
#     '31': 'тридцать первое'
# }
# month_list = {
#     '01': 'января',
#     '02': 'февраля',
#     '03': 'марта',
#     '04': 'августа',
#     '05': 'мая',
#     '06': 'июня',
#     '07': 'июля',
#     '08': 'августа',
#     '09': 'сентября',
#     '10': 'октября',
#     '11': 'ноября',
#     '12': 'декабря'
# }
# result = f'{day_list[day]} {month_list[month]} {year} года!'
# print(result)
# print(day_list[day], month_list[month], year, 'года!')

# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# my_list_2 = []
#
# for i in my_list_1:
#     if my_list_1.count(i) == 1:
#         my_list_2.append(i)
# print(my_list_2)
