#stack вызова: вызов функции внутри функции (переменная и адрес возврата)
#error stack overflow причины: слишком много функций/слишком много данных передается в функции

#рекурсия, gcd = нод
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
    
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)  
def factor(x:float, n:int):     #x^n = x * x^(n-1) возведение в степень
        if n == 0:
            return 1
        if n % 2 == 0:
            return factor(x*x, (n // 2)
        return x * (x ** (n - 1))
        
#ханойские башни, переместить N колец с iтой палочки на jтую чтобы короткие сверху
#1)N-1 i>>3-i-j  #3=0+1+2, номера палочек
#2)1 i>>j
#3)N-1 3-i-j>>j
#N=1 i>>j
def hanoy(N:int, i = 1, j = 3):
    if N == 1:
        print("Move from {i} to {j}")
        return
    hanoy(N-1, i, 6-i-j)  #6=1+2+3
    print(f"Move from {i} to {j}")
    hanoy(N-1, 6-i-j, j)

#генерация последовательностей
def gen_seq(A:list, N:int, prefix=...)
    if prefix is ...: #в префиксе информация о том что сгенерировали
        prefix = []
    if N == 0:
        print(''.join(map(str, prefix)), end=', ')
        return
    for element in A:
        prefix.append(element)
        gen_seq(A, N-1, prefix)
        prefix.pop()
    
#генерация перестановок
def gen_comb(A:list, N:int, prefix=...)
    if prefix is ...: #в префиксе информация о том что сгенерировали
        prefix = []
    if N == 0:
        print(''.join(map(str, prefix)), end=', ')
        return
    for i in range(len(A)):
        if A[i] is None:
            continue          #новая итерация
        prefix.append(A[i])
        A[i] = None
        gen_comb(A, N-1, prefix) 
        A[i] = prefix.pop()
        
#быстрая сортировка Хоара qsort О(N*lnN)~ O(N^2)
def split_barrier(A, barrier):

    left = [] 
    middle = []  
    right = []
    
    for x in A: 
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)
    return left, middle, right
def hoar_sort(A, depth=1, part='left'):
    #print('depth:', depth, 'part:', part, 'array before:', A)
    if (len(A) <= 1):
        return A
    else:
        L, M, R = split_barrier(A, A[0])
        A = hoar_sort(L, depth + 1) + M + hoar_sort(R, depth + 1, 'right')
    #print('depth:', depth, 'part:', part, 'array after:', A)
    return A
#делим список на два подсписка и сортируем их
#чтобы разделить идем слева и справа навстречу ищем элементы не в своих половинах меняем их местами и рекурсия(новые подсписки на еще списки)
def qsort(A:list, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(A) - 1
    if end <= start:
        return
    i = start
    j = end
    while i < j:
        while A[i] < A[end]:
            i += 1
        while j >= start and A[j] >= A[end]:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[i], A[end] = A[end], A[i]
    qsort(A, start, i-1)
    qsort(A, i+1, end)
    
#сортировка слиянием (дано два отсортированных массива) О(N)
def mergesort(A:list):
    if len(A) < 2:
        return
    n = len(A) // 2
    B = list(A[:n])
    C = list(A[n:])
    mergesort(B)
    mergesort(C)
    i = j = k = 0
    while i < len(B) and j < len(C):
        if B[i] < C [j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
        k += 1
    for i in range(i, n):
        A[k] = B[i]
        k += 1
    while j < len(C):
        A[k] = C[j]
        k += 1
        j += 1     
#сравниваем два массива по первым элементам, как только один из элементов меньших тот дописываем и переходим к другому массиву
#рекурсия по делению на подмассивы и слиянию О(N*lnN), минимум доп памяти - под еще один массив(плохо)
#ВСТРОЕННАЯ в питоне Тим сорт (слияние+вставка, вставка начинает работать когда массив уже маленький)

#рисование фрактала(самоподобная фигура) прямые коха на каждой такая фигура
import turtle
def f(L, N):
    if N == 1:
        turtle.forwatrd(L)
    else:
        f(L/3, N-1)                          #идти вперед
        turtle.left(60)
        f(L/3, N-1)
        turtle.right(120)
        f(L/3, N-1)
        turtle.left(60)
        f(L/3, N-1)
turtle.tracer(False)
turtle.goto(-250, 0)
f(500, 6)
turtle.right(120)
f(500, 6)
turtle.right(120)
f(500, 6)
turtle.right(120)
turtle.update()
turtle.mainloop()
       
#числа Фибоначчи O(Fib(n))
def fib(N):
    if N < 2:
        return N
    return fib(N-1) + fib(N-2)
for i in range(1000):
    print(fib(i))
#не запускаем рекурсию уже посчитанных чисел O(n)
def fib(N):
    c = [0] * (N+1)
    c[1] = 1
    for i in range(2, N+1):
        c[i] = c[i-1] + c[i-2]
    return c[N]
#результат сохраняем отдельным образом и fib(N-2) уже прибавляем к нему
cache = [0, 1]
def fib(N):
    if N >= len(cache):
        cache.append(fib(N-1) + fib(N-2))
    return cache[N]
for i in range(1000):
    print(i, fib(i))
    
    
#задача про подтягивания(с) через кэш
cash = []
def f(k, m):
    if m == 1:
        res = k
        cash.append(res)
        return res
    if len(cash) >= m + 1:
        return cash[m]
    res = f(k, m - 1) + (k + m - 1) + (k + m - 2)
    cash.append(res)
    return(res)
print(f(1, 10)) 
    
        
        
        