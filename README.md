 
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=111827&height=12" width="100%" alt="Separador superior"/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=111827&height=230&section=header&text=EQUIPO%2002&fontSize=78&fontColor=FFFFFF&fontAlignY=38&desc=SIMULADOR%20DE%20PLANIFICACI%C3%93N%20DE%20CPU&descSize=17&descColor=FFB000&descAlignY=65&animation=fadeIn" width="100%" alt="Equipo 02 - Simulador de CPU"/>

<br/>

<img src="https://img.shields.io/badge/PROYECTO-ACAD%C3%89MICO-2563EB?style=for-the-badge" alt="Proyecto académico"/>
<img src="https://img.shields.io/badge/EQUIPO-02-111827?style=for-the-badge" alt="Equipo 02"/>
<img src="https://img.shields.io/badge/INTEGRANTES-06-FFB000?style=for-the-badge&labelColor=111827" alt="Seis integrantes"/>

<br/><br/>

**Organización · Desarrollo · Simulación · Análisis**

*Proyecto académico 2026*

</div>

---

## 01. Presentación del equipo

Somos el **Equipo 02**, conformado por seis integrantes que trabajan colaborativamente en el diseño, desarrollo e implementación de un simulador de planificación de procesos de CPU.

Nuestro trabajo se orienta a la aplicación de conceptos fundamentales de sistemas operativos y programación, mediante la implementación de diferentes algoritmos de planificación y el análisis de su comportamiento a través de métricas y representaciones gráficas.

Buscamos desarrollar una solución organizada, modular y funcional, promoviendo la participación de todos los integrantes durante las distintas etapas del proyecto.

### Integrantes

| N.º | Apellidos y nombres | Identificación |
|:---:|---|:---:|
| 01 | Chara Franco, Johan Daymar | `TEAM-01` |
| 02 | Huancas Bereche, Erick Emilio | `TEAM-02` |
| 03 | Pellanne Aro, Carlos Alfredo | `TEAM-03` |
| 04 | Reyes Garcia, Alvaro Pablo | `TEAM-04` |
| 05 | Rivera Garayar, Matias Gabriel | `TEAM-05` |
| 06 | Romero Chac, Luis Antonio | `TEAM-06` |

> Los identificadores son referencias visuales para este documento y no representan cargos institucionales.

---

## 02. Sobre el proyecto

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=111827&height=100&section=header&text=SIMULADOR%20DE%20PLANIFICACI%C3%93N%20DE%20CPU&fontSize=25&fontColor=FFFFFF&fontAlignY=50" width="100%" alt="Simulador de planificación de CPU"/>

</div>

El proyecto consiste en el desarrollo de un **simulador de algoritmos de planificación de CPU**, diseñado para representar y analizar cómo un sistema operativo administra la ejecución de múltiples procesos que compiten por el uso del procesador.

A partir de un conjunto de procesos definidos mediante sus tiempos de llegada, ráfagas de ejecución y prioridades, el simulador ejecuta diferentes estrategias de planificación y permite observar sus resultados.

La solución incorpora métricas de rendimiento y representaciones visuales que facilitan la comparación entre los algoritmos implementados.

### Objetivo general

Desarrollar un simulador de planificación de CPU que permita implementar, ejecutar y comparar diferentes algoritmos de planificación de procesos, utilizando métricas de rendimiento y representaciones gráficas para analizar su comportamiento.

### Objetivos específicos

- Implementar diferentes algoritmos de planificación de CPU.
- Gestionar los procesos considerando sus tiempos de llegada, ráfagas y prioridades.
- Calcular métricas de rendimiento para cada simulación.
- Representar gráficamente la ejecución de los procesos mediante diagramas de Gantt.
- Comparar los resultados obtenidos por los diferentes algoritmos.

---

## 03. Algoritmos de planificación implementados

El simulador contempla cuatro algoritmos clásicos de planificación de CPU:

| Algoritmo | Descripción | Característica |
|---|---|---|
| **FCFS** | Ejecuta los procesos según su orden de llegada. | No apropiativo |
| **SJF** | Selecciona el proceso disponible con la ráfaga más corta. | No apropiativo |
| **Round Robin** | Distribuye el tiempo de CPU mediante turnos de duración determinada. | Apropiativo |
| **Prioridades** | Selecciona el proceso disponible con mayor prioridad. | No apropiativo |

Cada algoritmo se desarrolla de manera independiente para facilitar su mantenimiento, evaluación y comparación.

---

## 04. Métricas de rendimiento

Para analizar el comportamiento de los algoritmos, el simulador calcula las siguientes métricas:

| Métrica | Definición |
|---|---|
| Tiempo de espera | Tiempo de retorno menos tiempo de ráfaga. |
| Tiempo de retorno | Tiempo de finalización menos tiempo de llegada. |
| Utilización de CPU | Porcentaje del tiempo total de simulación durante el cual el procesador permanece ocupado. |

Estas métricas permiten evaluar el rendimiento de cada algoritmo y observar las diferencias entre sus estrategias de planificación.

---

## 05. Metodología de trabajo

El desarrollo del proyecto se organiza mediante cuatro aspectos fundamentales:

| Etapa | Descripción |
|---|---|
| **01. Planificación** | Organización de actividades, definición de objetivos y establecimiento de prioridades. |
| **02. Desarrollo** | Implementación modular de los algoritmos y componentes del simulador. |
| **03. Integración** | Conexión de los módulos y verificación del funcionamiento conjunto. |
| **04. Validación** | Ejecución de pruebas, revisión de resultados y evaluación de métricas. |

### Compromisos del equipo

- Cumplir las actividades y los plazos establecidos.
- Mantener una comunicación clara y oportuna.
- Distribuir responsabilidades de manera organizada.
- Documentar los avances relevantes.
- Revisar y validar los resultados antes de cada entrega.

---

## 06. Definiciones y supuestos

Para mantener criterios uniformes durante las simulaciones, se establecen las siguientes condiciones:

- **FCFS:** algoritmo no apropiativo que selecciona los procesos según su orden de llegada.
- **SJF:** algoritmo no apropiativo que selecciona la ráfaga más corta entre los procesos que ya llegaron.
- **Round Robin:** algoritmo apropiativo que asigna turnos de ejecución utilizando el quantum establecido.
- **Prioridades:** algoritmo no apropiativo donde el número menor representa una prioridad más alta.
- **Desempates:** se resuelven considerando primero el tiempo de llegada y posteriormente el identificador del proceso.
- **Tiempo de espera:** tiempo de retorno menos tiempo de ráfaga.
- **Tiempo de retorno:** tiempo de finalización menos tiempo de llegada.
- **Utilización de CPU:** (tiempo ocupado / tiempo total de simulación) × 100.

---

## 07. Alcance del simulador

El simulador considera las siguientes condiciones:

- Se trabaja con un único procesador (CPU).
- No se consideran sobrecostos por cambios de contexto.
- No se incluyen operaciones de entrada/salida (E/S).
- Los tiempos de los procesos se ingresan como valores enteros en milisegundos.
- El promedio de las métricas se calcula considerando todos los procesos.
- El tiempo total de simulación se mide desde `t = 0` hasta la finalización del último proceso, incluyendo los periodos de inactividad de la CPU.

---

## 08. Estructura del repositorio

El proyecto utiliza una arquitectura modular que separa la implementación de los algoritmos, la simulación, las métricas y la visualización de resultados.

```text
Simulador_CPU/
│
├── main.py
│
├── algoritmos/
│   ├── fcfs.py
│   ├── sjf.py
│   ├── round_robin.py
│   └── prioridades.py
│
├── simulacion/
│   ├── procesos.py
│   └── metricas.py
│
├── visualizacion/
│   ├── gantt.py
│   └── graficos.py
│
├── resultados/
│   ├── csv/
│   └── imagenes/
│
└── pruebas/
    └── pruebas.ipynb
```

### Descripción de los directorios

| Directorio / Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada principal del simulador. |
| `algoritmos/` | Implementación independiente de cada algoritmo de planificación. |
| `simulacion/` | Gestión de procesos, ejecución y cálculo de métricas. |
| `visualizacion/` | Generación de diagramas de Gantt y gráficos comparativos. |
| `resultados/` | Almacenamiento de archivos CSV e imágenes generadas. |
| `pruebas/` | Notebooks y pruebas exploratorias del proyecto. |

---

## 09. Objetivo común

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=111827&height=110&section=header&text=TRABAJO%20COLABORATIVO&fontSize=30&fontColor=FFFFFF&fontAlignY=38&desc=UN%20OBJETIVO%20EN%20COM%C3%9AN&descSize=13&descColor=FFB000&descAlignY=72" width="100%" alt="Trabajo colaborativo"/>

</div>

Como equipo, buscamos integrar nuestros conocimientos y habilidades para construir una herramienta que permita comprender de manera práctica el funcionamiento de los algoritmos de planificación de CPU.

Consideramos que la organización, la comunicación y la colaboración son elementos fundamentales para alcanzar los objetivos del proyecto y obtener resultados de calidad.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=2563EB&height=4" width="100%" alt="Separador inferior"/>

<br/>

**EQUIPO 02**

*Simulador de Planificación de CPU*

**2026 · Proyecto académico**

<img src="https://img.shields.io/badge/Desarrollado%20con-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python"/>

</div>
