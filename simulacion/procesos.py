
import csv

def validar_procesos(procesos):
    """
    Verifica la integridad lógica y de tipos de datos de una lista de procesos.
    
    Actúa como un mecanismo de programación defensiva para garantizar que 
    los algoritmos de planificación no fallen por datos mal formados.
    
    Args:
        procesos (list): Lista de diccionarios que representan los procesos.
        
    Raises:
        ValueError: Si la lista está vacía, faltan IDs, hay IDs duplicados, 
                    los tipos de datos son incorrectos o los valores son ilógicos 
                    (ej. ráfagas negativas).
                    
    Returns:
        bool: True si todos los procesos son válidos.
    """
    if not procesos:
        raise ValueError("Debe existir al menos un proceso.")
    ids = set()
    for p in procesos:
        if not str(p.get("id", "")).strip():
            raise ValueError("Todos los procesos deben tener un identificador.")
        if p["id"] in ids:
            raise ValueError(f"Identificador duplicado: {p['id']}")
        ids.add(p["id"])
        for campo in ("llegada", "rafaga", "prioridad"):
            if not isinstance(p[campo], int):
                raise ValueError(f"{campo} de {p['id']} debe ser entero.")
        if p["llegada"] < 0:
            raise ValueError("El tiempo de llegada no puede ser negativo.")
        if p["rafaga"] <= 0:
            raise ValueError("El tiempo de rafaga debe ser mayor que cero.")
    return True

def ingresar_procesos():
    """
    Permite al usuario ingresar los procesos manualmente a través de la terminal.
    
    Incluye manejo de excepciones para asegurar que el usuario ingrese
    cantidades válidas y asigna IDs por defecto si el usuario los omite.
    
    Returns:
        list: Lista de diccionarios validados listos para simulación.
    """
    while True:
        try:
            n = int(input("Cantidad de procesos: "))
            if n > 0:
                break
        except ValueError:
            pass
        print("Ingrese un entero positivo.")

    procesos = []
    for i in range(n):
        print(f"\n--- Proceso P{i + 1} ---")
        pid = input(f"ID [P{i + 1}]: ").strip() or f"P{i + 1}"
        llegada = int(input("Tiempo de llegada (>= 0): "))
        rafaga = int(input("Tiempo de rafaga (> 0): "))
        prioridad = int(input("Prioridad (menor numero = mayor prioridad): "))
        procesos.append({
            "id": pid,
            "llegada": llegada,
            "rafaga": rafaga,
            "prioridad": prioridad
        })
    validar_procesos(procesos)
    return procesos

def cargar_procesos_csv(ruta):
    """
    Carga y parsea una lista de procesos desde un archivo CSV.
    
    Ideal para simulaciones masivas o pruebas repetitivas sin necesidad 
    de ingresar los datos manualmente cada vez.
    
    Args:
        ruta (str): Ruta al archivo CSV.
        
    Raises:
        ValueError: Si el archivo no contiene las columnas mínimas requeridas.
        
    Returns:
        list: Lista de diccionarios validados listos para simulación.
    """
    procesos = []
    with open(ruta, newline="", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)
        requeridas = {"id", "llegada", "rafaga", "prioridad"}
        if not requeridas.issubset(set(lector.fieldnames or [])):
            raise ValueError("El CSV debe tener columnas: id,llegada,rafaga,prioridad")
        for fila in lector:
            procesos.append({
                "id": fila["id"].strip(),
                "llegada": int(fila["llegada"]),
                "rafaga": int(fila["rafaga"]),
                "prioridad": int(fila["prioridad"])
            })
    validar_procesos(procesos)
    return procesos
