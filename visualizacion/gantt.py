
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def guardar_gantt(gantt, titulo, ruta):
    """
    Genera y guarda una imagen PNG con el diagrama de Gantt de la simulación.
    
    Toma la lista de diccionarios (historial de ejecución) generada por los 
    algoritmos y la renderiza como una línea de tiempo horizontal continua.
    
    Args:
        gantt (list): Lista de diccionarios con el historial de ejecución 
                      (ej. [{"proceso": "P1", "inicio": 0, "fin": 4}, ...]).
        titulo (str): Nombre del algoritmo (ej. "FCFS") para el título del gráfico.
        ruta (str): Ruta completa donde se guardará la imagen (ej. "resultados/fcfs.png").
    """
    fig, ax = plt.subplots(figsize=(10, 2.8))
    colores = {}
    paleta = plt.get_cmap("tab20")
    nombres = list(dict.fromkeys(s["proceso"] for s in gantt))
    for i, nombre in enumerate(nombres):
        colores[nombre] = "#dddddd" if nombre == "IDLE" else paleta(i % 20)

    for s in gantt:
        inicio, fin = s["inicio"], s["fin"]
        ax.barh(0, fin-inicio, left=inicio, height=0.5,
                color=colores[s["proceso"]], edgecolor="black")
        ax.text((inicio+fin)/2, 0, s["proceso"], ha="center", va="center", fontsize=9)

    marcas = sorted(set([0] + [s["inicio"] for s in gantt] + [s["fin"] for s in gantt]))
    ax.set_xticks(marcas)
    ax.set_yticks([])
    ax.set_xlabel("Tiempo (ms)")
    ax.set_title(f"Diagrama de Gantt - {titulo}")
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    ax.set_xlim(left=0)
    fig.tight_layout()
    fig.savefig(ruta, dpi=160)
    plt.close(fig)
