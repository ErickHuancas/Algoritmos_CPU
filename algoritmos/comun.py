
from copy import deepcopy
from simulacion.metricas import calcular_metricas

def preparar(procesos):
    return deepcopy(procesos)
"""
    Crea una copia profunda e independiente de la lista de procesos original.
    Esto garantiza que la simulación de un algoritmo no altere los datos 
    originales, permitiendo que otros algoritmos se ejecuten desde cero 
    con los mismos datos de entrada. """


def agregar_segmento(gantt, proceso, inicio, fin):
    if fin <= inicio:
        return
    # Fusiona segmentos contiguos del mismo proceso.
    if gantt and gantt[-1]["proceso"] == proceso and gantt[-1]["fin"] == inicio:
        gantt[-1]["fin"] = fin
    else:
        gantt.append({"proceso": proceso, "inicio": inicio, "fin": fin})
        
    """
    Registra un bloque de tiempo de ejecución en el diagrama de Gantt.
    
    Valida que el segmento tenga una duración válida y optimiza el gráfico 
    fusionando bloques contiguos si pertenecen al mismo proceso continuo. """

def finalizar(procesos, gantt, nombre):
    detalles, resumen = calcular_metricas(procesos, gantt)
    return {"algoritmo": nombre, "gantt": gantt, "detalle": detalles, "resumen": resumen}

    """
    Empaqueta los resultados de la simulación y delega el cálculo de métricas.
    
    Estandariza la salida de todos los algoritmos de planificación para que 
    el generador de reportes reciba siempre la misma estructura de datos."""
