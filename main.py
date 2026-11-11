
from pathlib import Path
import pandas as pd

from simulacion.procesos import ingresar_procesos, cargar_procesos_csv, validar_procesos
from algoritmos.fcfs import fcfs
from algoritmos.sjf import sjf
from algoritmos.round_robin import round_robin
from algoritmos.prioridades import prioridades
from visualizacion.gantt import guardar_gantt
from visualizacion.graficos import guardar_comparacion
from simulacion.metricas import construir_resumen

RESULTADOS = Path("resultados")
GRAFICOS = RESULTADOS / "graficos"

def ejecutar_todos(procesos, quantum):
    # Cada algoritmo recibe sus propios datos; ninguno modifica la entrada original.
    return {
        "FCFS": fcfs(procesos),
        "SJF": sjf(procesos),
        "Round Robin": round_robin(procesos, quantum),
        "Prioridades": prioridades(procesos),
    }

def main():
    print("=" * 54)
    print("       SIMULADOR DE ALGORITMOS DE PLANIFICACION CPU")
    print("=" * 54)
    print("1. Ingresar procesos por consola")
    print("2. Cargar procesos desde CSV")
    opcion = input("Seleccione una opcion: ").strip()

    if opcion == "2":
        ruta = input("Ruta del archivo CSV [resultados/procesos.csv]: ").strip()
        procesos = cargar_procesos_csv(ruta or "resultados/procesos.csv")
    elif opcion == "1":
        procesos = ingresar_procesos()
    else:
        print("Opcion no valida.")
        return

    validar_procesos(procesos)
    print("\nProcesos ingresados:")
    print(pd.DataFrame(procesos).to_string(index=False))

    quantum = int(input("\nQuantum para Round Robin (entero positivo): "))
    if quantum <= 0:
        raise ValueError("El quantum debe ser mayor que cero.")

    resultados = ejecutar_todos(procesos, quantum)
    resumen = construir_resumen(resultados)

    RESULTADOS.mkdir(exist_ok=True)
    GRAFICOS.mkdir(parents=True, exist_ok=True)
    resumen.to_csv(RESULTADOS / "resultados.csv", index=False, encoding="utf-8-sig")

    print("\n========== COMPARACION DE ALGORITMOS ==========")
    print(resumen.round(2).to_string(index=False))

    for nombre, resultado in resultados.items():
        nombre_archivo = nombre.lower().replace(" ", "_")
        guardar_gantt(resultado["gantt"], nombre, GRAFICOS / f"gantt_{nombre_archivo}.png")

    guardar_comparacion(resumen, GRAFICOS / "comparacion_metricas.png")
    print(f"\nResultados guardados en: {RESULTADOS.resolve()}")
    print(f"Graficos guardados en: {GRAFICOS.resolve()}")
    print("\nCriterio: menor espera y retorno suelen ser mejores; mayor utilizacion indica menos tiempo ocioso.")
    print("La utilizacion se calcula desde t=0 hasta la finalizacion del ultimo proceso.")

if __name__ == "__main__":
    main()
