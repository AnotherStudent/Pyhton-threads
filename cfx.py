import matplotlib.pyplot as plot
import math
import numpy

# delphi
graph, ax = plot.subplots()
ax.plot([10, 50, 100, 200, 400, 450, 600], [0, 0, 3, 33, 356, 389, 813], color="blue", label="Однопоточная реализация")
ax.plot([10, 50, 100, 200, 400, 450, 600], [21, 8, 24, 43, 161, 195, 452], color="red", label="Многопоточная реализация")
ax.set_xlabel("Кол-во итераций")
ax.set_ylabel("Затраченное время (ms)")
ax.legend()
plot.title('Delphi')
#plot.show()
graph.savefig('cfx_delphi.png')

# python
graph, ax = plot.subplots()
ax.plot([10, 50, 100, 200, 400, 450, 600], [0, 21, 167, 1303, 11874, 20677, 43029], color="blue", label="Однопоточная реализация")
ax.plot([10, 50, 100, 200, 400, 450, 600], [1, 29, 182, 1366, 12093, 19869, 62638], color="red", label="Многопоточная реализация")
ax.set_xlabel("Кол-во итераций")
ax.set_ylabel("Затраченное время (ms)")
ax.legend()
plot.title('Python')
#plot.show()
graph.savefig('cfx_python.png')