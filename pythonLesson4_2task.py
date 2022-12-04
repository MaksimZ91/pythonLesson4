#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите значение числа N: "))

def factor(num):
  count = 2
  ls = []
  while count <= num:  
    if num % count == 0:
        ls.append(count)
        num = num / count
        count = 2 
    else: count +=1
  return ls 
print(factor(N) )  









   