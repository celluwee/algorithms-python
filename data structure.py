#структура данных
#1)очередь(поместить/взять из очереди) с разных концов queue = fifo(first input first output)
#2)stack с одного конца filo(first input last output) ex. list
stack = list()
s = input()

def check_braces(s):
    for symb in s:
        if symb in '([':
            stack.append(symb)
        elif symb in ')]':
            if stack.pop() + symb not in '()[]':
                return False
    return True

#обратная польская запись (кладем число на стек встречаем знак делаем это со стеком(с последними двумя числами), стек обновляем, знак после цифр)
#преимущество в отсутствии скобок
#все цифры в строку ответа, остальное - в стек (если закрыли скобку то знак до нее в строку ответа, если хотим положить плюс в стек но сверху умножить то умножить переносим в строку, затем плюс, когда кончается переносим все)
#не решена проблема унарного минуса (прибавление отрицательного числа)
def to_polska(s:str):
    res = []
    stack = []
    for el in s.split()
        if el == '(':
            stack.append(el)
        elif el == ')':
            a = stack.pop()
            while a != '(':
                res.append(a)
                a = stack.pop()
        elif el in {'+', '-'}:
            while len(stack) > 0 and stack[-1] in {'*', '/'}:
                res.append(stack.pop())
            stack.append(el)
        elif el in {'*', '/'}:
            stack.append(el)
        else:
            res.append(el)
    while len(stack):
        res.append(stack.pop())
    return res

#ооп объектно-ориентированное программирование
#class - обобщенное описание объекта
class Vec
    x = 0
    y = 0
V_1 = Vec()
V = Vec()
V.x = 7
V.y = 15
Vec.x = 7

class Vec
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
#как работает? V = Vec() <=> V = Vec. __new__() + Vec. __init__(V, x, y)
A = [Vec() for _ in range(10)]

class Vec:
    def __init__(self, x, y):
        sel.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self, y})'
    def __repr__(self):
        return f'Vec({self.x}, {self, y})'
    def len(self):
        return (self.x** 2 + self.y**2) ** 0.5
if __name__ == "main":                            #для того чтобы можно было отдельно импортировать классы
    from rendom import randint
    A = [Vec(randint(1, 10), randint(1, 10)) for _ in range(5)]
    print(A)
    for v in A:
        print(v, v.len())
     
#from [file_name] import [class_name]


class Vec:
    def __init__(self, x=0, y=0)
        self.x = x
        self.y = y
    def len(self):
        return (self.x**2 + self.y**2) ** 0.5
    def __add__(a, b):
        return Vec(a.x + b.x, a.y + b.y)
    def __mul__(a, b):
        if type(b) is Vec:
            return a.x * b.x + a.y * b.y
        else:
            return Vec(a.x * b, a.y * b)
    __rmul__ = __mul__                               #умножение справа и слева для коммутативных одно и то же
    def __str__(self):
        return f"({self.x},{self.y})"
if __name__ == "__main__":
    v = Vec(3, 4)
    u = Vec(5, 6)
    print(v, u, v + u, v * u)