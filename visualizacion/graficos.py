
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

def guardar_comparacion(resumen, ruta):
    metricas = [
        ("Espera promedio (ms)", "Tiempo de espera promedio"),
        ("Retorno promedio (ms)", "Tiempo de retorno promedio"),
        ("Utilizacion CPU (%)", "Utilizacion del CPU")
    ]
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    for ax, (columna, titulo) in zip(axes, metricas):
        valores = resumen[columna].to_numpy()
        barras = ax.bar(resumen["Algoritmo"], valores)
        ax.set_title(titulo)
        ax.tick_params(axis="x", rotation=35)
        ax.grid(axis="y", linestyle="--", alpha=0.35)
        ax.bar_label(barras, fmt="%.1f", padding=2, fontsize=8)
    fig.suptitle("Comparacion de algoritmos de planificacion")
    fig.tight_layout()
    fig.savefig(ruta, dpi=160, bbox_inches="tight")
    plt.close(fig)
