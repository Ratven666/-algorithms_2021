"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit


def merge_sort(lst_obj):
    if len(lst_obj) > 1:
        center = len(lst_obj) // 2
        left = lst_obj[:center]
        right = lst_obj[center:]

        merge_sort(left)
        merge_sort(right)

        return merge_lst(lst_obj, left, right)
    return lst_obj


def merge_lst(lst_obj, left, right):
    idx = 0
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            lst_obj[idx] = left.pop(0)
        else:
            lst_obj[idx] = right.pop(0)
        idx += 1

    while len(left) > 0:
        lst_obj[idx] = left.pop(0)
        idx += 1

    while len(right) > 0:
        lst_obj[idx] = right.pop(0)
        idx += 1
    return lst_obj


n = int(input("Введите число элементов: "))
orig_list = [random.random() * 50 for _ in range(n)]
print("Исходный -", orig_list)
print("Отсортированный -", merge_sort(orig_list[:]))


orig_list = [random.random() * 50 for _ in range(10)]
print(orig_list)
print(merge_sort(orig_list[:]))

print("=" * 25, "Массив 10 значений, счет 1000 раз", "=" * 25)
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.random() * 50 for _ in range(100)]

print("=" * 25, "Массив 100 значений, счет 1000 раз", "=" * 25)
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.random() * 50 for _ in range(1000)]

print("=" * 25, "Массив 1000 значений, счет 1000 раз", "=" * 25)
print(
    timeit.timeit(
        "merge_sort(orig_list[:])",
        globals=globals(),
        number=1000))

"""
Считается все довольно быстро, за счет нлог сложности
Улучшить принципиально ничего не смог, только разделил общую функцию на две по принципу единственной ответствености
ну и избавился от лишней индексации, вроде так должно по памяти поэкономнее быть
"""