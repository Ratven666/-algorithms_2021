"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
import timeit


def bubble_sort_up(unsort_lst):
    """Выполняет самую простую сортировку пузырьком по возрастанию"""
    temp_lst = unsort_lst.copy()
    for i in range(len(temp_lst)):
        for j in range(len(temp_lst) - 1):
            if temp_lst[j] > temp_lst[j + 1]:
                temp_lst[j], temp_lst[j + 1] = temp_lst[j + 1], temp_lst[j]
    return temp_lst


def bubble_sort_down(unsort_lst):
    """Выполняет самую простую сортировку пузырьком по убыванию"""
    temp_lst = unsort_lst.copy()
    for i in range(len(unsort_lst)):
        for j in range(len(unsort_lst) - 1):
            if temp_lst[j] < temp_lst[j + 1]:
                temp_lst[j], temp_lst[j + 1] = temp_lst[j + 1], temp_lst[j]
    return temp_lst


def bubble_sort_down_with_marker(unsort_lst):
    """Выполняет сортировку пузырьком по убыванию с проверкой отсортированности массива"""
    temp_lst = unsort_lst.copy()
    for i in range(len(temp_lst)):
        sort_flag = True
        for j in range(len(temp_lst) - 1):
            if temp_lst[j] < temp_lst[j + 1]:
                sort_flag = False
                temp_lst[j], temp_lst[j + 1] = temp_lst[j + 1], temp_lst[j]
        if sort_flag is True:
            break
    return temp_lst


def bubble_sort_down_opt(unsort_lst):
    """Выполняет самую простую сортировку пузырьком по убыванию"""
    temp_lst = unsort_lst.copy()
    start_idx = 0
    stop_idx = len(temp_lst)
    for i in range(stop_idx):
        sort_flag = True
        for j in range(start_idx, stop_idx - 1):
            if temp_lst[j] < temp_lst[j + 1]:
                sort_flag = False
                temp_lst[j], temp_lst[j + 1] = temp_lst[j + 1], temp_lst[j]
        if sort_flag is True:
            break
        stop_idx -= 1
    return temp_lst


orig_list = [randint(-100, 100) for _ in range(10)]
print("Оригинальный массив")
print(orig_list)
print("Массив отсортированный по возрастанию")
print(bubble_sort_up(orig_list[:]))
print("Массив отсортированный по убыанию")
print(bubble_sort_down(orig_list[:]))
print("Массив отсортированный по убыанию с маркером")
print(bubble_sort_down_with_marker(orig_list[:]))
print("Массив отсортированный по убыанию с марером и оптимизацие проходов")
print(bubble_sort_down_opt(orig_list[:]))

# замеры 10
print("=" * 25, "Массив 10 значений, счет 1000 раз", "=" * 25)

print(
    timeit.timeit(
        "bubble_sort_up(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_down(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_down_with_marker(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_down_opt(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(100)]

# замеры 100
print("=" * 25, "Массив 100 значений, счет 1000 раз", "=" * 25)

print(
    timeit.timeit(
        "bubble_sort_up(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_down(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_down_with_marker(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "bubble_sort_down_opt(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [randint(-100, 100) for _ in range(1000)]

# замеры 1000
print("=" * 25, "Массив 1000 значений, счет 10 раз", "=" * 25)
print(
    timeit.timeit(
        "bubble_sort_up(orig_list[:])",
        globals=globals(),
        number=10))
print(
    timeit.timeit(
        "bubble_sort_down(orig_list[:])",
        globals=globals(),
        number=10))
print(
    timeit.timeit(
        "bubble_sort_down_with_marker(orig_list[:])",
        globals=globals(),
        number=10))
print(
    timeit.timeit(
        "bubble_sort_down_opt(orig_list[:])",
        globals=globals(),
        number=10))

"""
Алгоритм сортировки начинает сильно проседать на 1000 значений, хотя и на 100 работает не супер как быстро

Оптимизация маркером дает прирост скорости на грани погрешности замеров, иногда даже скорость проседает,
возможно из-за возросших операций проверки условий

Оптимизация количества иттераций при последующих циклах дает стабильный прирост скорости процентов на 20
"""
