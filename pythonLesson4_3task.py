# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

ls = [1, 1, 2, 3, 4, 4, 4, 7, 7, 9, 2, 5]
def task3(ls):
  result = []
  _setA = set(ls)
  ls = sorted(ls) 
  for i in range(len(ls)-1):
    result.append(ls[i]) if ls[i] == ls[i+1] else ""
  _setB = set(result) 
  return list( _setA - _setB)
 
print(task3(ls))
  
   
    

