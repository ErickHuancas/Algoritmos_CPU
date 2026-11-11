
from collections import deque
from algoritmos.comun import preparar, agregar_segmento, finalizar

def round_robin(procesos, quantum):
    """
    Simula el algoritmo de planificación Round Robin (Apropiativo).
    
    Asigna un tiempo máximo de ejecución continuo (quantum) a cada proceso.
    Si un proceso no termina en ese tiempo, es interrumpido y enviado al final 
    de la cola de listos (cola circular).
    
    Args:
        procesos (list): Lista de diccionarios de procesos.
        quantum (int): Intervalo de tiempo máximo que un proceso puede usar el CPU de forma continua.
                         
    Returns:
        dict: Diccionario empaquetado con el diagrama de Gantt y métricas.
        
    Raises:
        ValueError: Si el quantum no es un número entero positivo.
    """
    if not isinstance(quantum, int) or quantum <= 0:
        raise ValueError("El quantum debe ser un entero positivo.")
    datos = preparar(procesos)
    por_llegada = sorted(datos, key=lambda x: (x["llegada"], x["id"]))
    restantes = {p["id"]: p["rafaga"] for p in datos}
    cola = deque()
    gantt = []
    tiempo = 0
    i = 0
    completados = 0

    while completados < len(datos):
        while i < len(por_llegada) and por_llegada[i]["llegada"] <= tiempo:
            cola.append(por_llegada[i])
            i += 1

        if not cola:
            siguiente = por_llegada[i]["llegada"]
            agregar_segmento(gantt, "IDLE", tiempo, siguiente)
            tiempo = siguiente
            continue

        p = cola.popleft()
        ejecutar = min(quantum, restantes[p["id"]])
        inicio = tiempo
        tiempo += ejecutar
        restantes[p["id"]] -= ejecutar
        agregar_segmento(gantt, p["id"], inicio, tiempo)

        # Los procesos que llegaron durante el turno entran antes de reencolar al actual.
        while i < len(por_llegada) and por_llegada[i]["llegada"] <= tiempo:
            cola.append(por_llegada[i])
            i += 1

        if restantes[p["id"]] > 0:
            cola.append(p)
        else:
            completados += 1

    return finalizar(datos, gantt, "Round Robin")
