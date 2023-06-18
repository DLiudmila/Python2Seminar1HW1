# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник
# разносторонним, равнобедренным или равносторонним

a = int(input('Введите сторону А: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))

if a + b > c and a + c > b and b + c > a: #существовует
    if a != b and a != c and b != c:
        print("Треугольник разносторонний.")
    elif a == b == c:
        print("Треугольник равносторонний.")
    else:
        print("Треугольник равнобедренный.")
else:
    print("Треугольник с такими сторонами не существует.")