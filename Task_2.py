# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if

n = int(input('Введите число N: '))
k_n = int(input('Введите число E: '))
summ = 0
for i in range(1, n + 1):
    summ = summ + i
