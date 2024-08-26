import time


def f(x): return -x ** 2 + 2 * x + 1


def flinha(x): return -2 * x + 2


def media(a, b): return (a + b) / 2


def modulo(x):
    if x < 0:
        return x * (-1)
    else:
        return x


# Questão 1
def metodoTEU(a: int, b: int):
    for x in range(a, b + 1):
        if (f(x) * f(x - 1)) < 0:
            print(f"[{x - 1},{x}]")


# Questão 2
def metodoBisseccao(a: int, b: int):
    if f(a) < 0:
        menor0 = a
        maior0 = b
    else:
        menor0 = b
        maior0 = a

    while True:
        x = media(menor0, maior0)
        if modulo(f(x)) >= 0.05:
            if f(x) < 0:
                menor0 = x
            else:
                maior0 = x
        else:
            print(f"x' = {round(x, 4)}")
            break


# Questão 3
def metodoNewtonRaphson(a: int, b: int):
    x = media(a, b)
    while True:
        if modulo(f(x)) >= 0.05:
            x = x - (f(x) / flinha(x))
        else:
            print(f"x' = {round(x, 4)}")
            break


print("Questão 1:")
metodoTEU(-3, 3)

print("\nQuestão 2:")
metodoBisseccao(-1, 0)

print("\nQuestão 3:")
metodoNewtonRaphson(2, 3)
