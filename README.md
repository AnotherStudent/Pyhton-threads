# Pyhton-threads

Использование потоков в python, тест производительности вычислений с потоками.  
Как видно из этого теста, из-за особенностей реализации потоков в Python, использование потоков практически не увеличивают производительность.

Аналогичный код(строчка в строчку) на Delphi показывает значительный прирост производительности при использовании потоков.

Delphi:  
```
mat size = (10, 10)
simple matrix multiply duration: 0ms
simple matrix multiply duration: 3ms

mat size = (50, 50)
simple matrix multiply duration: 0ms
simple matrix multiply duration: 8ms

mat size = (100, 100)
simple matrix multiply duration: 3ms
simple matrix multiply duration: 25ms

mat size = (200, 200)
simple matrix multiply duration: 32ms
simple matrix multiply duration: 37ms

mat size = (400, 400)
simple matrix multiply duration: 246ms
simple matrix multiply duration: 149ms

mat size = (450, 450)
simple matrix multiply duration: 329ms
simple matrix multiply duration: 195ms

mat size = (600, 600)
simple matrix multiply duration: 943ms
simple matrix multiply duration: 491ms

mat size = (800, 800)
simple matrix multiply duration: 2619ms
simple matrix multiply duration: 1366ms

mat size = (1500, 1500)
simple matrix multiply duration: 65841ms
simple matrix multiply duration: 30089ms
```

Pyhton:  
```
mat size = (10, 10)
 numpy matrix multiply duration: 0:00:00.000167
simple matrix multiply duration: 0:00:00.001766
thread matrix multiply duration: 0:00:00.004409

mat size = (50, 50)
 numpy matrix multiply duration: 0:00:00.000713
simple matrix multiply duration: 0:00:00.022221
thread matrix multiply duration: 0:00:00.027154

mat size = (100, 100)
 numpy matrix multiply duration: 0:00:00.003517
simple matrix multiply duration: 0:00:00.173255
thread matrix multiply duration: 0:00:00.198097

mat size = (200, 200)
 numpy matrix multiply duration: 0:00:00.018737
simple matrix multiply duration: 0:00:01.624033
thread matrix multiply duration: 0:00:01.908466

mat size = (400, 400)
 numpy matrix multiply duration: 0:00:00.117083
simple matrix multiply duration: 0:00:15.362252
thread matrix multiply duration: 0:00:15.642354

mat size = (450, 450)
 numpy matrix multiply duration: 0:00:00.141888
simple matrix multiply duration: 0:00:20.677068
thread matrix multiply duration: 0:00:18.869476
*** Thread-driven multuply is winner! ***
```
