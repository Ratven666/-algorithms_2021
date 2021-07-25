"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.
"""

import random
import timeit
import statistics

m = int(input("Введите число \"m\": "))
test_lst = [random.randint(0, 100) for _ in range(2*m + 1)]


def median_statistics(lst):
    return statistics.median(lst)


def median_naive(lst):
    m = len(lst) // 2
    temp_lst = sorted(lst)
    return temp_lst[m]


def median_without_sort(lst: list):
    temp_lst = lst.copy()
    m = len(lst) // 2
    for _ in range(m):
        temp_lst.remove(max(temp_lst))
    return max(temp_lst)


print("Исходный массив")
print(test_lst)
print("Отсортированный исходный массив")
print(sorted(test_lst))
print("Медиана из модуля статистика")
print(median_statistics(test_lst))
print("Медиана найденая через сортировку")
print(median_naive(test_lst))
print("Медиана без сортировки")
print(median_without_sort(test_lst))


print("=" * 25, "Массив 10 значений, счет 1000 раз", "=" * 25)
orig_list = [random.randint(-100, 100) for _ in range(11)]

print(
    timeit.timeit(
        "median_statistics(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "median_naive(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "median_without_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print("=" * 25, "Массив 100 значений, счет 1000 раз", "=" * 25)
orig_list = [random.randint(-100, 100) for _ in range(101)]

print(
    timeit.timeit(
        "median_statistics(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "median_naive(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "median_without_sort(orig_list[:])",
        globals=globals(),
        number=1000))

print("=" * 25, "Массив 1000 значений, счет 1000 раз", "=" * 25)
orig_list = [random.randint(-100, 100) for _ in range(1001)]

print(
    timeit.timeit(
        "median_statistics(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "median_naive(orig_list[:])",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "median_without_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
Три варианта -
первый и второй нлог сложности,
третий - квадратичный, за счет того что линейная сложность поиска максимума и удаления элемента
"""
