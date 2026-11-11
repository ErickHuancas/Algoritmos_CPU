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
