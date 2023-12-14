# Практическая работа по Основам Программирования №3
## Требования к выполнению заданий
1. На оценку 3 балла
   - [x] Реализовать программу в соответствии с заданием
2. На оценку 4 балла
   - [x] Добавить проверку входных аргументов и вывод сообщений об ошибках
   (используя исключения)
   - [x] Подготовить 4 – 5 примеров в виде функций с  
   осмысленными названиями, демонстрирующих возможности  
   программы, в том числе варианты сообщений об ошибках
3. На оценку 5 баллов
   - [x] Добавить меню для выбора действия
   - [x] Добавить строку документации к основной функции
   - [x] Зациклить программу для повторного запроса ввода,  
   предусмотреть вариант завершения программы
## Вариант №3
### Задание варианта 
Написать функцию, реализующую алгоритм сортировки выбором.  
**Входные значения:** список длиной *n*  
**Выходные значения:** отсортированный список длиной *n*

### Описание алгоритма сортировки выбором
1. В неотсортированном массиве ищется локальный минимум
2. Найденный минимум меняется местами с первым элементом в массиве 
3. Это повторяется до тех пор, пока массив не будет отсортирован

![Сортировка выбором](https://github.com/art-io/op3-docs/assets/123387786/8612ea42-7144-46b7-892f-5b729d9dd52d)

**Время работы алгоритма:**  
*t = O(n<sup>2</sup>)*  
Время работы алгоритма сортировки выбором одинаково и в худшем, и в лучшем случае.

[Подробнее про алгоритмы сортировки выбором](https://habr.com/ru/articles/422085/)

### Описание программы
В программе представлены функции интерфейса *main*, *initialize_program* и *end_program*,  
функция *selection_sort* отвечающая за сам алгоритм сортировки выбором, а также  
вспомогательная функция *get_float_input*, получающая число с плавающей запятой от пользователя

Функция *main* отвечает за зацикливание программы и завершение программы.  
Она обращается ко функциям *initialize_program*, *end_program* и *selection_sort*

Функция initialize_program отвечает за инициализацию программы пользовательскими данными.  
Она представляет собой два цикла:
Первый цикл является по сути входной точкой программы, в которой пользователь может  
начать ввод данных либо выйти из неё
```python
while True:
  inp = str(input())
  if inp == "1":
      print(welcome_msg)
      break
  if inp == "2":
      return False
  print(entry_msg)
```
Второй цикл позволяет пользователю заполнить массив, попутно предотвращая  
ошибочный ввод  
```python
while True:
   inp = get_float_input()
   if not isinstance(inp, float):
     if inp == "start":
         if len(arr) > 1:
             return arr
         print(error_msg2)
         continue
     print(error_msg1)
     continue
   print(success_msg)
   arr.append(inp)
```

Функция end_program отвечает за завершающую часть программы и требует от  
пользователя совершить какое-либо действие (получить результат работы программы,  
запустить программу заново или выйти из неё).  
Она состоит из небольшой менюшки и цикла, предотвращающего ошибочный ввод:  
```python
while True:
   inp = str(input())
   match (inp):
      case "1":
          print(result)
      case "2":
          break
      case "3":
          return False
      case _:
          print(end_msg)
return True
```  

Функция selection_sort представляет собой сам алгоритм сортировки, работающий  
с пользовательским массивом данных arr
```python
for i in range(len(arr) - 1):
  minimum = arr[i]
  index = i
  for j in range(i + 1, len(arr)):
      if minimum > arr[j]:
          minimum = arr[j]
          index = j
  if index != i:
      temp = arr[i]
      arr[i] = arr[index]
      arr[index] = temp
return arr
```
