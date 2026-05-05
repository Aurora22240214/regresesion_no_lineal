# Análisis de Regresión No Lineal y Pruebas de Estrés Computacional

Este proyecto ilustra de manera didáctica la aplicación de modelos de **Regresión Polinomial** implementados desde cero utilizando álgebra matricial, para predecir y modelar el comportamiento del consumo de recursos del hardware local durante la ejecución de pruebas computacionales progresivamente intensivas.

El material está diseñado con rigor pedagógico para estudiantes de Ingeniería en Sistemas. Demuestra tanto la materialización física del impacto asintótico de un algoritmo $O(N^3)$, como la resolución cerrada estructurada de Mínimos Cuadrados Ordinarios (MCO) en modelos de Machine Learning clásico.

## Requisitos de Entorno

* **Python 3.8 o superior**
* `numpy`: Destinado a operaciones analíticas y álgebra tensorial lineal.
* `pandas`: Destinado a la lectura y escritura estructural de bases de datos.
* `matplotlib`: Implementación gráfica bidimensional de las curvas de ajuste polinomial continuo.
* `psutil`: Sensor métrico para extraer telemetría física de Hardware en fase de ejecución.

Puede instalar integralmente todo el entorno virtual requerido empleando la orden de gestor local de paquetes pip:
```bash
pip install numpy pandas matplotlib psutil openpyxl
```

## Arquitectura del Proyecto

El flujo operativo del material se segmenta en dos etapas analíticas claramente definidas:

### 1. Generador de Carga Estructural (`dataset.py`)
Este script despliega un bucle iterativo experimental donde escala progresivamente el tamaño perimetral de dos matrices sintéticas para después operarlas algebraicamente de forma masiva (Complejidad de Cómputo de $O(N^3)$). A la par de ese estrangulamiento algorítmico, emplea trazados asíncronos para inspeccionar el delta temporal, y los consumos máximos escalados de Memoria RAM junto a la ocupación del CPU. A posteriori exporta las métricas unificadas resultantes a un archivo Excel denominado `datos_rendimiento_pc.xlsx`.

**Comando de inicialización:**
```bash
python dataset.py
```

### 2. Motor de Inferencia y Reconstrucción Polinómica (`main.py`)
Script modular principal, dotado de un menú interactivo interactivo. Se encarga de procesar el archivo Excel obtenido previamiente con los datos del hardware estresado para implementar dinámicamente sobre la curva base obtenida un *pipeline* con capacidad multi-grado de ajuste. Su objetivo final consiste en trazar comparativas numéricas tangibles estimando y mitigando la tasa de error que experimenta un modelo lineal tradicional frente a observaciones bi-espaciales no lineales.

**Comando de inicialización:**
```bash
python main.py
```

## Comprendiendo la Matemática Subyacente (Guía Estudiantil)

La **Regresión Polinomial Paramétrica** postula que la correlación biunívoca inferida entre la característica predictora dependiente $x$ (en esta investigación: tamaño dimensional de la matriz de esfuerzo) y la proyección estimada $\hat{y}$ (tiempo consumido en cálculo en el procesador físico) se ajusta armónicamente usando una expansión estática controlada por el parámetro k-ésimo dictatorial.

El problema algebraico asume el planteo estructural: 
$$ \hat{y} = \theta_{0} + \theta_{1}x + \theta_{2}x^{2} + \dots + \theta_{k}x^{k} $$

**1. Conformación Analítica - Matriz de Diseño ($\Phi$):**
El fundamento informático programado sobre `main.py` define a esta matriz dimensional anexando o incrementando secuencialmente a manera de columna el vector primario observacional hasta el coeficiente de ajuste pretendido. Se referencia bibliográficamente como una versión modificada del postulado de la *Matriz de Vandermonde*.

**2. Extracción de Lógica Cerrada Continua (Mínimos Cuadrados Ordinarios):**
Con el sustento final de identificar el mejor vector canónico multidimensional de parámetros absolutos ($\Theta$) que logre deprimir a un mínimo funcional aceptable la suma penalizada de varianzas ($MSE$ Error Cuadrático Medio), el código computacional soslaya abordajes asintóticos como el Descenso del Gradiente optando firmemente por el despeje categórico numérico por medio de plantear analíticamente la resolución de la **Ecuación Normal**:

$$ \vec{\Theta} = (\Phi^{T} \Phi)^{-1} \Phi^{T} \vec{Y} $$

Esto se computa a su vez dentro del engine del proyecto aplicando explícitamente operaciones del álgebra tensorial de numpy en la forma procedimental directa `np.linalg.solve(Phi.T @ Phi, Phi.T @ y)` asegurando exactitud aritmética pura e inmediata.

---

> [!NOTE]
> **Reflexión sobre Estabilidad del Software de Análisis**
> Como podrá testear con el sistema en tiempo real, el cálculo de un *Número de Condición* se imprime rutinariamente en todo test para constatar la viabilidad numérica que previene inestabilidades intrínsecas a los recursos del PC. A niveles y grados polinómicos desmesuradamente elevados, el tensor transpuesto puede devenir en una condición colineal mal estructurada.
