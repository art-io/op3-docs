"""Практическая по ОП, Вариант №3"""


def get_float_input():
    """Получает на вход число с плавающей точкой\n
    Основная цель функции - ловить ошибку ValueError,
    чтобы работа программы продолжалась\n
    Возвращает любое значение введённое пользователем"""
    inp = input()
    try:
        inp = float(inp)
        return inp
    except ValueError:
        return inp


def initialize_program():
    """Инициализирует программу заполняя список числами\n
    Функция представляет собой набор циклов, предотвращающих
    неверный ввод пользователя
    Возвращает False если пользователь захочет завершить программу или
    массив чисел если пользователь его заполнил"""
    arr = []

    entry_msg = "1 - Начать ввод чисел\n2 - Выход"
    welcome_msg = "Приступайте к вводу чисел. \
Вводите числа по одному, а затем введите start для \
запуска программы."
    print(entry_msg)
    while True:
        inp = str(input())
        if inp == "1":
            print(welcome_msg)
            break
        if inp == "2":
            return False
        print(entry_msg)

    success_msg = "Принято."
    error_msg1 = "Введите корректное числовое значение."
    error_msg2 = "Введите хотя бы 2 числа."
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


def end_program(result: str) -> bool:
    """Последний этап работы программы\n
    Предоставляет пользователю возможность получить
    результат работы программы, а также возможность
    запустить её заново или завершить её работу\n
    Возвращает True если необходимо продолжить выполнение
    программы и False если необходимо завершить выполнение
    программы
    """
    end_msg = "1 - Показать отсортированный массив\n\
2 - Запустить программу заново\n\
3 - Закрыть программу"

    print("Программа завершила работу.")
    print(end_msg)
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


def selection_sort(arr: list) -> list:
    """Сортировка массива выбором\n
    Проходит по массиву раз за разом, каждый
    раз меняя местами наименьшее значение и первое
    нетронутое алгоритмом значение в массиве\n
    Если в массиве меньше двух элементов, сгенерируется
    исключение IndexError\n
    Возвращает отсортированный по возрастанию массив, например:\n
    Входной массив [5, 4, 99, 20]
    Возвращаемый массив: [4, 5, 20, 99]\n"""
    if len(arr) < 2:
        raise IndexError("Недостаточно объектов в массиве")
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


def main():
    """Основная часть программы\n
    Представляет собой бесконечный цикл
    перезапускающий программу до тех пор пока
    пользователь не введёт команду выхода"""
    while True:
        arr = initialize_program()
        if arr is False:
            return
        result = selection_sort(arr)
        next_action = end_program(result)
        if next_action is False:
            return


if __name__ == "__main__":
    main()
