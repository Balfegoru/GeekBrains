#  Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

#  Найдите количество и выведите его.

# """
# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `list_1` и `k`

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `list_1` и `k` для проверки
# """

list_1 = [1, 2, 3, 4, 5,3,2,1,3]
k = 3

# Введите ваше решение ниже
counter = 0

for i in list_1:
    if k == i:
        counter+=1
print(counter)

