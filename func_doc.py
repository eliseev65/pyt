def printMax(x, y):
    '''Выводит максимальное из двух чисел\n\nОба значения должны быть целыми числами.'''
    x = int(x) # конвертируем в целые, если возможно.
    y = int(y)

    if x > y:
        print(x)
    else:
        print(y)

printMax(4, 6)
print(printMax.__doc__)

help(printMax)