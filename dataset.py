import psutil
import time
import pandas as pd
import numpy as np

print("🚀 Iniciando prueba de carga en el sistema...")
print("Recopilando datos, por favor espera...\n")

datos_sistema = []

# Iteramos 40 veces, aumentando la carga en cada paso
for i in range(1, 41):
    # Definimos el 'Tamaño del Problema' (N). 
    # Cada vez será una matriz más y más grande.
    tamaño_matriz = i * 150 
    
    # 1. Empezamos a medir el tiempo
    tiempo_inicio = time.time()
    
    # 2. Generamos el estrés (Multiplicación de matrices masivas)
    # Esto tiene una complejidad computacional no lineal
    matriz_a = np.random.rand(tamaño_matriz, tamaño_matriz)
    matriz_b = np.random.rand(tamaño_matriz, tamaño_matriz)
    resultado = np.dot(matriz_a, matriz_b) 
    
    # 3. Terminamos de medir el tiempo
    tiempo_fin = time.time()
    tiempo_ejecucion = tiempo_fin - tiempo_inicio
    
    # 4. Capturamos las métricas del sistema con psutil
    uso_cpu = psutil.cpu_percent(interval=0.1)
    uso_ram = psutil.virtual_memory().percent
    
    # 5. Guardamos la "foto" de este momento
    datos_sistema.append({
        "Iteracion": i,
        "Tamaño_Problema": tamaño_matriz,
        "Tiempo_Segundos": tiempo_ejecucion,
        "CPU_Porcentaje": uso_cpu,
        "RAM_Porcentaje": uso_ram
    })
    
    print(f"Paso {i:02d}/40 | Tamaño: {tamaño_matriz:4d} | CPU: {uso_cpu:5.1f}% | RAM: {uso_ram:4.1f}% | Tiempo: {tiempo_ejecucion:.4f} seg")

# ==========================================
# GUARDAR EN EXCEL
# ==========================================
df = pd.DataFrame(datos_sistema)
nombre_archivo = "datos_rendimiento_pc.xlsx"
df.to_excel(nombre_archivo, index=False)

print(f"\n✅ ¡Prueba terminada! Los datos reales de tu PC se han guardado en '{nombre_archivo}'.")