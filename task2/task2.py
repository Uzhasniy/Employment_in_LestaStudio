class First:
    
    def fifo_append_pop(array):
        app = input('Введите число: ')
        array.append(int(app))
        array.pop(0)
        print(array)
    
    def fifo_insert_remove(array):
        app = input('Введите число: ')
        array.insert(7,(int(app)))
        remove_index = array[0]
        array.remove(remove_index)
        print(array)

class Second:

    def cut_append(array):
        app = input('Введите число: ')
        array = array[1:] + [int(app)]
        print(array)

if __name__ == '__main__':
    array = [32,13,54,7,9,45,2]
    First.fifo_append_pop(array)
    First.fifo_insert_remove(array)
    Second.cut_append(array)