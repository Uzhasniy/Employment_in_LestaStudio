# def isEven(value):
#     return print(value%2==0)

def number_parity(value):
    if (value/2) == (value//2):
        print('число чётное')
    else:print('число нечётное')

if __name__ == '__main__':
    value = input('Введите число: ')
    number_parity(int(value))