import math as m
import numpy as np
import matplotlib.pyplot as plt


def fibonaci(x1, x2):
    if x2 < 1000:
        return fibonaci(x1=x2, x2=x1+x2)
    else:
        return x1
    
def kwadratowe(a, b, c):
    print(f'{a}x^2 {b}x {c}')
    delta = b*b - (4*a*c)
    if delta > 0:
        x1 = (-b - m.sqrt(delta))/(2*a)
        x2 = (-b + m.sqrt(delta))/(2*a)
        return (x1, x2)    
    elif delta == 0:
        x = b/(2*a)
        return f'{x}, instnieje tylko jeden pierwiastek'
    else:
        return 'Blad: delta mniejsza niz zero'

def statystyka():
    lt = []
    try:
        while True:
            x = float(input())
            lt.append(x)
    except ValueError:
        srednia = sum(lt)/(len(lt))
        suma = 0
        for val in lt:
            suma += (val - srednia)*(val - srednia)
        wariancja = suma/(len(lt) - 1)
        odchylenie = m.sqrt(wariancja)/m.sqrt(len(lt))

        return f'Srednia:\t{srednia}\nWariancja:\t{wariancja}\nOdchylenie:\t{odchylenie}'
    
def zad3(x):
    x = np.float32(x)
    f = m.sqrt(x**2 + 1) - 1
    g = (x**2)/(m.sqrt(x**2 + 1) + 1)
    print(f'f({x}) = {f}\tg({x}) = {g}')

def zad4(x):
    x = np.float32(x)
    f = x - m.sin(x)
    g = (x**3/6) * (1 - (x**2)/20)*(1 - ((x**2)/(6*7)) * (1 - ((x**2/(8*9)))))
    print(f'f({x}) = {f}\tg({x}) = {g}')

def zad5():
    suma1, suma2 = np.float32(0), np.float32(0)
    for i in range(1, 101):
        suma1 += 1/np.float32(i)
    for i in range(100, 0, -1):
        suma2 += 1/np.float32(i)
    print(suma1, suma2)

def func(a):
    return a**8 - (36 * a**7) + (546 * a**6) - (4536 * a**5) + (22449 * a**4) - (67284 * a**3) + (118124 * a**2) - (109584 * a) + 40320

def plotBuilder():
    a = np.linspace(-8, -6, 100)
    
    plt.plot(a, InterpolacjaLagrange())
    #plt.plot(x, np.sin(x))

    plt.show()

def zad6(m = 50, epsilon = 10**(-24), delta = 10**(-24), a = 5.5, b = 6.5): # input -> lkrokow, epsilon, delta, (a, b) wartosci brzegowe fcji
    if np.sign(func(a)) != np.sign(func(b)):
        for i in range(m):
            c = a + (b-a)/2
            if abs(a - b) < delta and func(c) <= epsilon and np.sign(func(a)) == np.sign(func(b)):
                print(f'GOOD\nc = {c}; f(x)={func(c)}')
                break
            else:
                if np.sign(func(c)) != np.sign(func(a)):
                    b = c
                    print(f'c = {b}; f(x)={func(b)}; blad: {abs(func(a) - func(c))}')
                elif np.sign(func(c)) != np.sign(func(b)):
                    a = c
                    print(f'c = {a}; f(x)={func(a)}; blad: {abs(func(b) - func(c))}')
                else:
                    print('error')
                    break
        if abs(func(a) - func(c)) > abs(func(b) - func(c)):
            print(f'LT\nc = {c}; f(x)={func(c)}; blad: {abs(func(a) - func(c))}')
        else:
            print(f'LT\nc = {c}; f(x)={func(c)}; blad: {abs(func(b) - func(c))}')
    else:
        print('brak miesc zerowych na danym przedziale')

def f(a):
    return a**2 - 4

def fprim(a):
    return np.exp(a) - 1/(1 + a**2)

def zad7MetodaNewtona(x0, delta = 10**(-10)): # input -> x0
    x = x0 - f(x0)/fprim(x0)
    krok = 1
    while delta < f(x):
        x = x - f(x)/fprim(x)
        print(krok, x, f(x))
        krok += 1

def zad7MetodaSiecznych(x0, x1, delta = 10**(-10)):
    if x0<x1:
        x0, x1 = x1, x0
    
    krok = 1
    while f(x1) > delta:
        x = x0
        x0 = x1
        x1 = (f(x0) - f(x))/(x0 - x)
        print(f'{krok}\txn = {x1}, xn-1 = {x}, f(xn) = {f(x0)}')


        krok += 1
        
def fmonster(x): # -> f-cja Monster Weierstrassa do domu
    y = 0
    for n in range(100):
        y += (0.9)**n * np.cos((1/(0.9) + (3*np.pi)/(2 * 0.9) + 10e-5)**n * np.pi * x)
    return y

tn = {}

def Tn(x, n): # -> napisz funkcję na wielomiany Czebyszewa używając programowania dynamicznego i jebanej w dupe kurwa rekurencji której matka nigdy nie kochała
    if n == 0:
        return 1
    if n == 1:
        return x
    if n > 1:
        return 2 * x * Tn(x, n-1) - Tn(x, n-2)

def InterpolacjaLagrange(test = 6, delta = 10e-6) -> float: 
    lim = test**2
    X = np.linspace(-1, 1, test)
    Y = [Tn(p, n) for n, p in enumerate(X)]
    x = np.linspace(-1, 1, lim)
    print('points calculated!')

    L = []

    for i in range(test):
        l = []
        for xx in x:
            gl = 1
            dl = 1
            for j in range(test):
                if i != j:
                    gl *= (xx - X[j])
                    dl *= (X[i] - X[j])

            l.append(gl/dl)
        L.append(l)

    print('lagange functions calculated!')
    for i in range(test):
        plt.plot(x, L[i], label=f'l({i})')

    plt.legend()

    plt.show()
    print('l functions shown')

    P = []
    for i in range(lim):
        ly = 0
        for k in range(test):
            ly += Y[k] * L[k][i]
        P.append(ly)

    print('p(x) calculated!')

    plt.title(f'Wielomiany Czebyszewa')
    plt.plot(x, P, color='b')
    plt.plot(x, Tn(x), 'r--')
    plt.plot(X, Y, 'ro')

    plt.show()
     
    err = []
    for val in X:
        for i in range(len(x)):
            if abs(val - x[i]) <= delta:
                err.append((1/(1 + 25**val) - P[i]))

    print(f'Answear status: {len(err) == test}')
    norm = 0
    for er in err:
        norm += er**2
    
    return norm

print(Tn(0.3, 100))
