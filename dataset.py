import psutil
import time
import pandas as pd
import numpy as np
from typing import List, Dict, Any

def ejecutar_prueba_rendimiento(iteraciones: int = 40) -> pd.DataFrame:
    """
    Ejecuta una prueba de estrés iterativa simulando una carga computacional matricial.

    A medida que aumentan las iteraciones, el tamaño de las matrices crece linealmente.
    Dicha operación tiene una complejidad algorítmica de O(N^3) debido a la multiplicación
    de matrices, lo que modela un comportamiento temporal inherentemente no lineal. Este
    experimento sirve como entrada para la demostración de la regresión polinomial.

    Args:
        iteraciones (int): Número de ciclos de la prueba de carga.

    Returns:
        pd.DataFrame: Conjunto de datos con las métricas recopiladas por cada iteración.
    """
    print("Iniciando prueba de carga en el sistema...")
    print("Recopilando datos, por favor espere...\n")

    datos_sistema: List[Dict[str, Any]] = []

    # Iteramos aumentando la carga en cada paso
    for i in range(1, iteraciones + 1):
        # Cada paso incrementa el tamaño de las matrices
        tamaño_matriz = i * 150 
        
        tiempo_inicio = time.time()
        
        # Generación de la carga sintética (Multiplicación masiva de matrices)
        matriz_a = np.random.rand(tamaño_matriz, tamaño_matriz)
        matriz_b = np.random.rand(tamaño_matriz, tamaño_matriz)
        _ = np.dot(matriz_a, matriz_b) 
        
        tiempo_fin = time.time()
        tiempo_ejecucion = tiempo_fin - tiempo_inicio
        
        # Recopilación de métricas desde el hardware
        uso_cpu = psutil.cpu_percent(interval=0.1)
        uso_ram = psutil.virtual_memory().percent
        
        datos_sistema.append({
            "Iteracion": i,
            "Tamaño_Problema": tamaño_matriz,
            "Tiempo_Segundos": tiempo_ejecucion,
            "CPU_Porcentaje": uso_cpu,
            "RAM_Porcentaje": uso_ram
        })
        
        print(f"Paso {i:02d}/{iteraciones} | Tamaño: {tamaño_matriz:4d} | CPU: {uso_cpu:5.1f}% | RAM: {uso_ram:4.1f}% | Tiempo: {tiempo_ejecucion:.4f} seg")
    
    return pd.DataFrame(datos_sistema)

def guardar_resultados(df: pd.DataFrame, nombre_archivo: str = "datos_rendimiento_pc.xlsx") -> None:
    """
    Exporta el DataFrame de rendimiento recopilado a un archivo en formato Excel.

    Args:
        df (pd.DataFrame): Conjunto de datos de iteraciones y latencia.
        nombre_archivo (str): Nombre del archivo donde se guardarán los resultados.
    """
    df.to_excel(nombre_archivo, index=False)
    print(f"\nPrueba terminada. Los datos estructurales se han guardado en '{nombre_archivo}'.")

if __name__ == "__main__":
    df_resultados = ejecutar_prueba_rendimiento(40)
    guardar_resultados(df_resultados)