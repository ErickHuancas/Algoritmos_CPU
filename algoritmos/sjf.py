
from algoritmos.comun import preparar, agregar_segmento, finalizar

def sjf(procesos):
    """SJF no apropiativo: entre los procesos disponibles elige la menor rafaga."""
    """
    Simula el algoritmo de planificación SJF (Shortest Job First / El trabajo más corto primero).
    
    Versión No Apropiativa (Non-preemptive): Una vez que un proceso obtiene el CPU, 
    se ejecuta hasta terminar su ráfaga por completo, sin ser interrumpido.
    Entre los procesos disponibles en la cola de listos, elige siempre el que 
    tenga la menor ráfaga de CPU.
    
    Args:
        procesos (list): Lista de diccionarios de procesos. Debe incluir las 
                         claves 'id', 'llegada' y 'rafaga'.
                         
    Returns:
        dict: Diccionario empaquetado con el diagrama de Gantt y métricas globales.
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
        p = min(disponibles, key=lambda x: (x["rafaga"], x["llegada"], x["id"]))
        inicio = tiempo
        tiempo += p["rafaga"]
        agregar_segmento(gantt, p["id"], inicio, tiempo)
        pendientes.remove(p)
    return finalizar(datos, gantt, "SJF")
