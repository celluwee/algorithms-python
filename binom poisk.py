#биномиального поиска(для отсортированного списка)(нахождения элемента в списке через левую и правую границы, деление на подмассивы) O(log2(n)) тк каждый раз уменьшаем в два раза
def find_left_bound(A:list, x):
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (right + left) // 2
        if A[middle] >= x:                           #если правая граница то >
            right = middle
        else:
            left = middle
    return left                                      #если правая граница, то right
for x in A:
    print(find_left_bound(A, x))

#кол-во дипломов которое помещается (M // k) * (M // n), ищем левую границу + 1
#теорема о промежуточн знач, решение уравнений 
def solve(f, a, b, *, eps=1e-5):
    while b - a > eps:                                   #eps - в каком знаке будет отличие
        m = (a + b) / 2
        if f(m) == 0:
            break
        if f(m) * f(a) < 0:
            b = m
        else:
            a = m
    return m
from math import sin, pi
print(solve(sin, 3, 4), pi)

