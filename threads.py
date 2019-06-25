import random
import numpy
from datetime import datetime
import threading
import multiprocessing
import time

def genMatrix(n):
    mat = list()
    for y in range(0, n):
        line = list()
        for x in range(0, n): 
            line = line + [random.randint(0, 1000)]
        mat = mat + [line] 
    return mat

def simpleMul(matA, matB):
    # gen array
    res = list()
    for y in range(0, len(matA)):
        line = list()
        for x in range(0, len(matA)): 
            line = line + [0]
        res = res + [line]
    # mul
    for i in range(len(matA)):
        for j in range(len(matB[0])):
            cell = 0
            for k in range(len(matB)):
                cell = cell + matA[i][k] * matB[k][j]
                #time.sleep(0.005)
            res[i][j] = cell
    return res

class ResultThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(ResultThread, self).__init__(*args, **kwargs)
        self.result = None

def threadMul(matA, matB):
    # Возвращает умноженную строку матрицы
    def mulLine(matA, matB, i):
        res = list()

        for j in range(len(matB[0])):
            cell = 0
            for k in range(len(matB)):
                cell = cell + matA[i][k] * matB[k][j]
                #time.sleep(0.005)
            res = res + [cell]

        threading.currentThread().result = res
        
    # mul
    threads = list()
    for i in range(len(matA)):
        
        # ограничим кол-во потоков 8-ю
        while True:
            count = 0
            for th in threads:
                if th.isAlive():
                    count = count + 1
            if count < 8:
                break
            time.sleep(0)
        
        thread = ResultThread(target = mulLine, args = (matA.copy(), matB.copy(), i))
        threads = threads + [thread]
        thread.start()

    res = list()
    # wait to all thread is done
    for i in threads:   
        i.join()
        res = res + [i.result]
        
    return res

test_n = [10, 50, 100, 200, 400, 450, 600]

for i in test_n:
    print("\nmat size = (" + str(i) + ", " + str(i) + ")")
    matA = genMatrix(i)
    matB = genMatrix(i)
    
    # numpy mul
    oldTime = datetime.now()
    matRes1 = numpy.dot(matA, matB)
    duration1 = (datetime.now() - oldTime)
    print(" numpy matrix multiply duration: " + str(duration1))
    
    # simple mul
    oldTime = datetime.now()
    matRes2 = simpleMul(matA, matB)
    duration2 = (datetime.now() - oldTime)
    print("simple matrix multiply duration: " + str(duration2))
    
    # thread mul
    oldTime = datetime.now()
    matRes3 = threadMul(matA, matB)
    duration3 = (datetime.now() - oldTime)
    print("thread matrix multiply duration: " + str(duration3))
    
    if duration2 > duration3:
        print("*** Thread-driven multuply is winner! ***")
    
    # check
    for y in range(0, len(matA)):
        for x in range(0, len(matA)): 
            assert(matRes1[y][x] == matRes2[y][x])
            assert(matRes1[y][x] == matRes3[y][x])
    
