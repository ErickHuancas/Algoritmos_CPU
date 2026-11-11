
from algoritmos.comun import preparar, agregar_segmento, finalizar

def fcfs(procesos):
    """
    Simula el algoritmo de planificación de CPU FCFS (First-Come, First-Served).
    
    Es un algoritmo no apropiativo (non-preemptive) que atiende a los procesos 
    estrictamente en el orden en que llegan a la cola de listos. """
    
    datos = preparar(procesos)
    tiempo = 0
    gantt = []
    #Ordenar los procesos por tiempo de llegada.
    for p in sorted(datos, key=lambda x: (x["llegada"], x["id"])):
        if tiempo < p["llegada"]:
        # Manejo de tiempo inactivo (IDLE)
        # Si el reloj actual es menor al tiempo de llegada del siguiente proceso, 
        # significa que la cola de listos está vacía y el CPU no hace nada.
            agregar_segmento(gantt, "IDLE", tiempo, p["llegada"])
            tiempo = p["llegada"]
        inicio = tiempo
        tiempo += p["rafaga"] ## Sumar todo el tiempo de ráfaga (burst) de golpe
        agregar_segmento(gantt, p["id"], inicio, tiempo)
    return finalizar(datos, gantt, "FCFS")
