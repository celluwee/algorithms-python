#найти наибольшую общую подпоследовательность(длину)  О(n*m)
#крайний случай - пустая и непустая, по диагонали записываем длину наибольшей общ подпосл к этому моменту, примыкающие к диагонали клетки тоже
def gcs(A:list, B:list):
    N = len(A)
    M = len(B)
    F = [[0] * (M + 1) for _ in range(N + 1)]    #матрица, первая строка/столбец нулевые как крайний случай
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F
def get_common_seq(A, B):
    F = gcs(A, B)
    i = len(A)
    j = len(B)
    res = []
    while i > 0 and j > 0:
        if F[i][j] - F[i-1][j-1] == 1 and A[i-1] == B[j-1]:        #если диагональный на единицу меньше и равны между собой элементы то этот элемент учтен при подсчете общей подпоследовательности и его кладем в res 
            res.append(A[i-1])
            i -= 1
            j -= 1
        else:
            if F[i-1][j] == F[i][j]:
                i -= 1
            else:
                j -= 1
    return res[::-1]
    
#наибольшую возрастающую подпоследовательность O(nlog(n)) + O(n^2)=O(n^2) (например в В кладем отсорт а и выполняем gcs, однако слишком много памяти, реализуем тоже квадратиную но с меньшей памятью)
#под А-итым элементом в таблице будем писать длину наиб возраст с учетом этого элемента, затем максимум из них, идем назать и восстанавливаем саму подпосл
def grs(A:list):
    N = len(A)
    F = [0] * N
    
    for i in range(N):
        m = 0
        for j in range(i):
            if A[j] < A[i] and F[j] > m:
                m = F[j]
        F[i] = 1 + m
    return F
 
def geat_rising_seq(A):
    F = grs(A)
    N = max(F)
    last = float('+inf')
    res = []
    for i in range(len(A)-1, -1, -1):
        if F[i] == N and A[i] < last:
            res.append(A[i])
            last = A[i]
            N -= 1
    return res[::-1]

#задача о рюкзаке(у каждой вещи вес и ценность) - по горизонтали размер рюкзака с шагом в единицу, по вертикали номер объекта
def bag(W:list, p:list, size):
    N = len(W)
    F = [[0] * (size + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(size + 1):
            if W[i] > j:
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = max(F[i-1][j], p[i] + F[i-1][j-W[i]])
    return F
#задача о Кузнечике
1)+1
2)+2(i)
какой последний прыжок?
К_n = K_(n-1) + K_(n-i)
def traj_num(n):
    K = [0, 1] + [0] * n
    for i in range(2, N+1):
        K[i] = K[i-1] + K[i-2]
    return K[n]