
# Simulador de algoritmos de planificación de CPU

Proyecto académico en Python que compara FCFS, SJF no apropiativo, Round Robin y Prioridades no apropiativo.

## Requisitos
- Python 3.10 o superior
- pip

## Instalación
Desde la carpeta `Simulador_CPU`:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Ejecución
```bash
python main.py
```

El programa permite ingresar procesos por consola o cargarlos desde `resultados/procesos.csv`.
Cada proceso tiene `id`, `llegada`, `rafaga` y `prioridad`. Para prioridades, un número menor significa mayor prioridad. El quantum se solicita al iniciar.

## Archivos generados
- `resultados/resultados.csv`: resumen comparativo.
- `resultados/graficos/gantt_*.png`: un diagrama de Gantt por algoritmo.
- `resultados/graficos/comparacion_metricas.png`: gráficos comparativos.

## Definiciones y supuestos
- FCFS: no apropiativo, orden de llegada.
- SJF: no apropiativo; elige la ráfaga más corta entre los procesos que ya llegaron.
- Round Robin: apropiativo por turnos; utiliza el quantum indicado.
- Prioridades: no apropiativo; el número menor representa mayor prioridad.
- Empates: se resuelven por llegada y luego por identificador.
- Tiempo de espera = tiempo de retorno - ráfaga.
- Tiempo de retorno = finalización - llegada.
- Utilización CPU = (tiempo ocupado / tiempo total de simulación) x 100. El tiempo total se mide desde t=0 hasta que termina el último proceso; por eso incluye periodos ociosos.

## Alcance
La simulación supone un solo CPU, sin sobrecosto por cambio de contexto y sin operaciones de E/S. Los tiempos se ingresan como enteros en milisegundos. El promedio se calcula sobre todos los procesos.

## Estructura
- `algoritmos/`: implementación independiente de cada planificador.
- `simulacion/`: ingreso, validación y métricas.
- `visualizacion/`: diagramas de Gantt y gráficos.
- `resultados/`: CSV e imágenes generadas.
- `pruebas/`: notebook de pruebas exploratorias.
