
from algoritmos.comun import preparar, agregar_segmento, finalizar

def prioridades(procesos):
    """
    Simula el algoritmo de planificación por Prioridades (No Apropiativo).
    
    En esta implementación, un valor numérico MENOR representa una MAYOR prioridad.
    Una vez que un proceso toma el CPU, no es interrumpido hasta que termina 
    su ráfaga (non-preemptive).
    
    Args:
        procesos (list): Lista de diccionarios con la información de los procesos.
                         Debe incluir las claves 'id', 'llegada', 'rafaga' y 'prioridad'.
                         
    Returns:
        dict: Diccionario empaquetado con el diagrama de Gantt y métricas.
    """
    datos = preparar(procesos)
    pendientes = datos[:]
    tiempo = 0
    gantt = []
    while pendientes:
        disponibles = [p for p in pendientes if p["llegada"] <= tiempo]
        if not disponibles:
            siguiente = min(p["llegada"] for p in pendientes)
            agregar_segmento(gantt, "IDLE", tiempo, siguiente)
            tiempo = siguiente
            continue
        p = min(disponibles, key=lambda x: (x["prioridad"], x["llegada"], x["id"]))
        inicio = tiempo
        tiempo += p["rafaga"]
        agregar_segmento(gantt, p["id"], inicio, tiempo)
        pendientes.remove(p)
    return finalizar(datos, gantt, "Prioridades")
