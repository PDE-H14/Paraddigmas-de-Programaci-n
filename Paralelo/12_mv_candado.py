from multiprocessing import Process, Value, Lock
import random
import os

def montecarlo(N: int, resultado:Value, lock:Lock) -> None:
    semilla: float = random.uniform(-1,1)
    random.seed(semilla)
    dentro: int = 0
    for i in range(N):
        x: float = random.uniform(-1,1)
        y: float = random.uniform(-1,1)
        if (x*x+y*y) < 1.0:
            dentro += 1
    with lock:
        resultado.value += dentro

if __name__ == '__main__':
    lock = Lock()
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int(n/cpus)
    print("Procesadores=",cpus,"N=",N)
    resultado = Value('i',0)
    procesos = []
for i in range(cpus):
    procesos.append(Process(target = montecarlo, args=(N,resultado,lock)))

# Comienza los procesos en paralelo
for proceso in procesos:
    proceso.start()

# Espera a que todos los procesos terminen
for proceso in procesos:
    proceso.join()
print("Número de tiros=",cpus*N)
print("Número de aciertos=",resultado.value)
print("Aproximación de PI=",4*float(resultado.value)/(cpus*N))