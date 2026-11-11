
import pandas as pd

def calcular_metricas(procesos, gantt):
    """Calcula espera = retorno - rafaga; retorno = fin - llegada."""
    """
    Calcula los tiempos de espera, retorno y métricas globales de uso de CPU.
    
    Utiliza el diagrama de Gantt para encontrar el instante de finalización absoluto 
    de cada proceso y aplica las fórmulas matemáticas estándar de planificación:
    - Retorno (Turnaround Time) = Tiempo de finalización - Tiempo de llegada
    - Espera (Waiting Time) = Tiempo de Retorno - Tiempo de ráfaga (Burst time)
    
    Args:
        procesos (list): Lista original de diccionarios de procesos.
        gantt (list): Historial de ejecución generado por los algoritmos.
        
    Returns:
        tuple: (filas_detalle, metricas_resumen)
               - filas_detalle: Lista de diccionarios con métricas por proceso individual.
               - metricas_resumen: Diccionario con los promedios globales y uso de CPU.
    """
    fin_por_id = {}
    for segmento in gantt:
        if segmento["proceso"] != "IDLE":
            fin_por_id[segmento["proceso"]] = segmento["fin"]

    filas = []
    for p in procesos:
        fin = fin_por_id[p["id"]]
        retorno = fin - p["llegada"]
        espera = retorno - p["rafaga"]
        filas.append({
            "Proceso": p["id"],
            "Llegada": p["llegada"],
            "Rafaga": p["rafaga"],
            "Prioridad": p["prioridad"],
            "Finalizacion": fin,
            "Espera": espera,
            "Retorno": retorno
        })

    inicio = min([0] + [s["inicio"] for s in gantt])
    fin_total = max(s["fin"] for s in gantt)
    tiempo_total = fin_total - inicio
    tiempo_ocioso = sum(
        s["fin"] - s["inicio"] for s in gantt if s["proceso"] == "IDLE"
    )
    utilizacion = ((tiempo_total - tiempo_ocioso) / tiempo_total * 100) if tiempo_total else 0
    return filas, {
        "espera_promedio": sum(x["Espera"] for x in filas) / len(filas),
        "retorno_promedio": sum(x["Retorno"] for x in filas) / len(filas),
        "utilizacion_cpu": utilizacion,
        "tiempo_total": tiempo_total,
        "tiempo_ocioso": tiempo_ocioso
    }

def construir_resumen(resultados):
    """
    Consolida los resultados de todos los algoritmos evaluados en un DataFrame.
    
    Ideal para visualizar el informe comparativo final y facilitar la exportación 
    de los resultados a un archivo CSV.
    
    Args:
        resultados (dict): Diccionario donde la llave es el nombre del algoritmo 
                           y el valor es la respuesta generada por finalizar().
                           
    Returns:
        pd.DataFrame: Tabla estructurada con las métricas promedio de cada algoritmo.
    """
    filas = []
    for nombre, resultado in resultados.items():
        m = resultado["resumen"]
        filas.append({
            "Algoritmo": nombre,
            "Espera promedio (ms)": m["espera_promedio"],
            "Retorno promedio (ms)": m["retorno_promedio"],
            "Utilizacion CPU (%)": m["utilizacion_cpu"],
            "Tiempo total (ms)": m["tiempo_total"],
            "Tiempo ocioso (ms)": m["tiempo_ocioso"]
        })
    return pd.DataFrame(filas)
