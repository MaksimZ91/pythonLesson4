# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
# Вывод: 3.14
# Ввод: 0.001
# Вывод: 3.141

import math

accur = len(input("Введите желаемую точность: ").split(".")[1])
pi = float(str(math.pi)[:accur + 2])
print(pi)

#print(round(math.pi, accur))
