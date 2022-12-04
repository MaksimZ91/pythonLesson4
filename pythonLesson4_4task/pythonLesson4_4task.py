# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

k = int(input("Введите значение числа N: "))
str = ""
path =  "./pythonLesson4_4task/task4_result.txt"
import random

def write(dat):
  with open(path, "a") as data:
      data.write(dat) 
def task4(k):
  while k >= 0:
    koef = random.randint(1,100)
    if k == 0:    
      str = f"{koef} = 0"
      write(str)
    elif k == 1:
      str = f"{koef}X + "
      write(str)
    else: 
      str = f"{koef}X^{k} + "
      write(str)     
    k -= 1      

task4(k)
   






 





 


