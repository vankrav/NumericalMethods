import  random

def f(x):
    return (x-2)* (x-3) * (x-3) * (x-7)


def start_appox(start, stop):
    while True:
        x0, x1 = random.randrange(start, stop), random.randrange(start, stop)
        if f(x0) * f(x1) < 0:
            return x0, x1


def dih(x0, x1, e, max_iteration, f):
    iteration = 0
    xm = (x1 + x0) / 2
    while abs(x1-x0) >= e:
        iteration += 1
        f_x0 = f(x0)
        f_x1 = f(x1)
        f_xm = f(xm)
        if f_xm * f_x0 < 0:
            x1 = xm
        else:
            x0 = xm
        if iteration >= max_iteration:
            return xm
        xm = (x1 + x0) / 2

    return xm


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x0, x1 = start_appox(-10000, 10000)
    e = 0.001
    root = dih(x0, x1, e, 500, f)

    if root is not None:
        print(f"Приближенный корень: {root}")
    else:
        print("Метод не сошелся к корню.")
    print()