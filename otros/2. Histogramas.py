#  --------------------------------  Importaciones --------------------------------

import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# -------------------------------------------------------------------------

# el dataset pur_time (del inglés purchase_time que significa tiempo de compra)
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])

# escribe tu código aquí
pur_time.hist(
    bins=[15, 30, 45, 60, 75, 90], alpha=0.7
)


# - Hacer 2 histogramas

ej2 = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])

ej2.hist(
    bins=[15, 35, 55, 75, 90], alpha=0.5
)

ej2.hist(
    bins=[15, 45, 55, 90], alpha=0.5
)

# - ejemplo con seabron

dataset = pd.Series([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6])
sns.boxplot(dataset)

# -

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
mean_value = data.mean()  # busca el valor medio en el dataset
spacing_all = data - mean_value # para cada elemento en el dataset encuentra su distancia a la media
spacing_all_mean = spacing_all.mean()  # calcula la distancia media

print(spacing_all_mean)

# - varianza

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

variance = np.var(data)# calcula la varianza aquí
print(variance)# escribe tu código aquí)



# ------- ejercicio 1
# Calcula la desviación estándar del dataset data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) y guárdala en la variable standard_dev. Luego muestra los resultados.

data = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

standard_dev = np.std(data)
print(standard_dev)

# --------- ejercicio 2

adv_mean = 3
adv_var = 0.25
adv_std = np.sqrt(adv_var)

adv_time = adv_mean + 3 * adv_std #calcula el límite superior del intervalo que representa el 99.7% de los usuarios
print('El tiempo de visualización del mensaje es', adv_time)

# ------ ejercicio 3

quiz_mean = 6000 / 100 * 3
quiz_std = 6000 / 100 * 0.4

quiz_bottom_line = quiz_mean - 3 * quiz_std
quiz_top_line = quiz_mean + 3 * quiz_std

print('Intervalo:', quiz_bottom_line, '-', quiz_top_line)

# ------------------ CUESTIONARIO

# Calcular la desviación estándar con NumPy
data = [1, 2, 3, 4, 5]
std_dev = np.std(data)

# Construcción de un histograma de frecuencia
plt.hist(data, bins=5)