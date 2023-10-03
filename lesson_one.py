import math

def sum_a_b(a, b):
    return a + b


def data_type_lesson():
    a: str = "mafmudin"
    print('data ', a, 'tipe datanya adalah ', type(a))
    return ""


def factorial_lesson(n):
    return math.factorial(n)


def average_lesson(a, b, c, d):
    return (a + b + c + d) / 4


def calculate_lesson(a, b, c, y):
    return (a + b + c) / y ** 2


if __name__ == '__main__':
    print(sum_a_b(12, 5))
    print(data_type_lesson())

    print(factorial_lesson(3))
    print(average_lesson(1,2,3,4))
    print(calculate_lesson(3,4,1, 2))
