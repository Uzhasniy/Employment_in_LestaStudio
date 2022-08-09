import timeit
import random
import time


array = []
tick_time_array = {
    "sort":0,
    "reverse":0,
    "sorted":0,
}

class Sort:

    def sort_by_asc(array):

        tick_time = timeit.timeit(lambda: array.sort(), number=10000)
        tick_time_array["sort"] = tick_time
        array.sort()
        print(f'Массив отсортирован через sort: {array}\nЗатраченное время: {tick_time}\n')
        return tick_time_array

    def sort_by_desc(array):

        tick_time = timeit.timeit(lambda: array.reverse(), number=10000)
        tick_time_array["reverse"] = tick_time
        array.sort()
        array.reverse()
        print(f'Массив отсортирован через sort+reverse: {array}\nЗатраченное время: {tick_time}\n')
        return tick_time_array


class Sorted:

    def sorted_array(array):
        
        tick_time = timeit.timeit(lambda: sorted(array), number=10000)
        tick_time_array["sorted"] = tick_time
        sorted_array = sorted(array)
        print(f'Массив отсортирован через sorted: {sorted_array}\nЗатраченное время: {tick_time}\n')
        return tick_time_array


def main():

    for i in range(random.randrange(5,20)):
        i = random.randint(1, 99)
        array.append(i)
    print(f'Полученный массив: {array}\n')

    Sort.sort_by_asc(array)
    Sort.sort_by_desc(array)
    Sorted.sorted_array(array)

    print('-'*20)
    print(f'Быстрее всего выполнилась сортировка методом {min(tick_time_array)},\nвремя её выполнения: {tick_time_array.get(min(tick_time_array))}\n')
    

if __name__ == '__main__':
    main()