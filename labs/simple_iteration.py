import math


"""
    Пример 3.8. Методом простых итераций с точностью e = 0,001 
    уточнить корень трансцендентного уравнения x^2 – e^–x = 0, 
    причем искомый корень x* принадлежит [0,5; 1,0] эквивалентно G.
"""

def simple_iteration_method(G, x0, e, max_iter):

    x = x0
    iterations = 0

    while iterations < max_iter:
        x_next = G(x)
        if abs(x_next - x) < e:
            return x_next, iterations + 1  # Найден приближенный корень
        x = x_next
        iterations += 1

    return None, max_iterations  # Не удалось найти корень за максимальное число итераций


def G(x):
    return math.e ** (-x / 2)


if __name__ == '__main__':
    x0 = (0.5+1) / 2  # Начальное приближение
    epsilon = 0.0001  # Точность
    max_iterations = 10000  # Максимальное число итераций

    root, iterations = simple_iteration_method(G, x0, epsilon, max_iterations)

    if root is not None:
        print(f"Приближенный корень: {root}")
        print(f"Число итераций: {iterations}")
    else:
        print("Метод не сошелся к корню.")