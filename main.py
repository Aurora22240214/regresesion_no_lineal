import numpy as np
import matplotlib.pyplot as plt
import pandas as pd # <-- Nueva librería agregada
import os

class RegresionPolinomial:
    def __init__(self, grado):
        self.grado = grado
        self.coef = None

    def construir_phi(self, x):
        return np.column_stack([x**j for j in range(self.grado + 1)])

    def ajustar(self, x, y):
        Phi = self.construir_phi(x)
        C = Phi.T @ Phi
        B = Phi.T @ y

        self.coef = np.linalg.solve(C, B)
        condicion = np.linalg.cond(C)

        return condicion

    def predecir(self, x):
        Phi = self.construir_phi(x)
        return Phi @ self.coef

    def ecm(self, y, y_pred):
        return np.mean((y - y_pred)**2)

    def r2(self, y, y_pred):
        ss_total = np.sum((y - np.mean(y))**2)
        ss_res = np.sum((y - y_pred)**2)
        return 1 - (ss_res / ss_total)


# ==========================================
# FUNCIONES DE VISUALIZACIÓN Y ANÁLISIS
# ==========================================

def comparar_modelos(x, y):
    n = len(x)
    split = int(0.8 * n)

    x_train, x_test = x[:split], x[split:]
    y_train, y_test = y[:split], y[split:]

    grados = [1, 2, 3, 5, 10]
    resultados = []

    print("\n=== COMPARACIÓN DE MODELOS ===\n")

    for grado in grados:
        modelo = RegresionPolinomial(grado)
        cond = modelo.ajustar(x_train, y_train)

        y_train_pred = modelo.predecir(x_train)
        y_test_pred = modelo.predecir(x_test)

        ecm_train = modelo.ecm(y_train, y_train_pred)
        ecm_test = modelo.ecm(y_test, y_test_pred)
        r2_val = modelo.r2(y_test, y_test_pred)

        resultados.append((grado, ecm_test))

        print(f"Grado {grado}")
        print(f"ECM train: {ecm_train:.4f}")
        print(f"ECM test : {ecm_test:.4f}")
        print(f"R²       : {r2_val:.4f}")
        print(f"Condición: {cond:.2e}")
        print("-" * 40)

    mejor_grado = min(resultados, key=lambda item: item[1])[0]
    print(f"\n🔥 Mejor grado seleccionado: {mejor_grado}")

    return mejor_grado


def graficar(x, y, modelo, titulo="Modelo"):
    x_suave = np.linspace(min(x), max(x), 300)
    y_suave = modelo.predecir(x_suave)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.5, label="Datos")
    plt.plot(x_suave, y_suave, color='red', linewidth=2, label="Modelo")
    plt.title(titulo)
    plt.legend()
    plt.grid()
    plt.show()


def animacion_grados(x, y):
    plt.ion()
    for grado in range(1, 8):
        modelo = RegresionPolinomial(grado)
        modelo.ajustar(x, y)

        x_suave = np.linspace(min(x), max(x), 300)
        y_suave = modelo.predecir(x_suave)

        plt.clf()
        plt.scatter(x, y, alpha=0.5)
        plt.plot(x_suave, y_suave, color='red')
        plt.title(f"Grado = {grado}")
        plt.pause(1)

    plt.ioff()
    plt.show()


def modo_manual(x, y):
    grado = 1
    while True:
        modelo = RegresionPolinomial(grado)
        cond = modelo.ajustar(x, y)

        y_pred = modelo.predecir(x)
        ecm_val = modelo.ecm(y, y_pred)
        r2_val = modelo.r2(y, y_pred)

        x_suave = np.linspace(min(x), max(x), 300)
        y_suave = modelo.predecir(x_suave)

        plt.figure(figsize=(8, 5))
        plt.scatter(x, y, alpha=0.5)
        plt.plot(x_suave, y_suave, color='red')
        plt.title(f"Grado = {grado}")
        plt.grid()
        plt.show()

        print(f"\nGrado: {grado}")
        print(f"ECM: {ecm_val:.4f}")
        print(f"R²: {r2_val:.4f}")
        print(f"Condición: {cond:.2e}")

        accion = input("\n[n] siguiente | [p] anterior | [q] salir: ").strip().lower()

        if accion == "n":
            grado += 1
        elif accion == "p" and grado > 1:
            grado -= 1
        elif accion == "q":
            break


# ==========================================
# NUEVA FUNCIÓN PARA GESTIÓN DE DATOS
# ==========================================
def cargar_datos():
    print("\n¿Qué fuente de datos deseas utilizar?")
    print("1. Generar datos sintéticos aleatorios")
    print("2. Cargar desde un archivo Excel (.xlsx o .xls)")
    
    opc = input("Selecciona (1/2): ").strip()
    
    if opc == "2":
        ruta = input("Ingresa la ruta del archivo (ej. datos.xlsx): ").strip()
        if not os.path.exists(ruta):
            print("❌ Archivo no encontrado. Usando datos aleatorios por defecto.")
            return generar_datos_aleatorios()
            
        try:
            df = pd.read_excel(ruta)
            print("\nColumnas detectadas:", list(df.columns))
            col_x = input("Escribe el nombre de la columna para X: ").strip()
            col_y = input("Escribe el nombre de la columna para Y: ").strip()
            
            # Limpiamos los datos quitando nulos (NaN)
            df = df.dropna(subset=[col_x, col_y])
            
            # Convertimos a arreglos de NumPy y ordenamos por X para que las gráficas de líneas se vean bien
            df = df.sort_values(by=col_x)
            x = df[col_x].values
            y = df[col_y].values
            print(f"✅ Se cargaron {len(x)} registros exitosamente.")
            return x, y
            
        except Exception as e:
            print(f"❌ Error al leer el Excel: {e}")
            print("Usando datos aleatorios por defecto.")
            return generar_datos_aleatorios()
    else:
        return generar_datos_aleatorios()

def generar_datos_aleatorios():
    np.random.seed(42)
    x = np.linspace(-2, 2, 100)
    y = 1.5*x**3 - 0.5*x**2 + 2*x + 1 + np.random.normal(0, 2.5, 100)
    return x, y


# ==========================================
# MENÚ PRINCIPAL
# ==========================================
if __name__ == "__main__":
    # 1. Primero cargamos los datos (solo se hace una vez)
    x_global, y_global = cargar_datos()

    # 2. Entramos al loop de los modelos
    while True:
        print("""
===== REGRESIÓN NO LINEAL =====
1. Ejecutar modelo completo
2. Animación automática
3. Modo manual (paso a paso)
4. Cambiar datos (Cargar nuevo Excel o Aleatorios)
5. Salir
""")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            mejor_grado = comparar_modelos(x_global, y_global)
            modelo = RegresionPolinomial(mejor_grado)
            modelo.ajustar(x_global, y_global)
            graficar(x_global, y_global, modelo, f"Modelo Final (grado={mejor_grado})")

        elif opcion == "2":
            animacion_grados(x_global, y_global)

        elif opcion == "3":
            modo_manual(x_global, y_global)
            
        elif opcion == "4":
            x_global, y_global = cargar_datos()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("❌ Opción inválida")