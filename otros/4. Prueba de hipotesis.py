# ------------ Importaciones

import pandas as pd
from scipy import stats as st

# ------------ Fin de las Importaciones

# ------------ Ejercicio 1

# Datos de la muestra

scooters = pd.Series([15, 31, 10, 21, 21, 32, 30, 25, 21,
28, 25, 32, 38, 18, 33, 24, 26, 40, 24, 37, 20, 36, 28, 38,
24, 35, 33, 21, 29, 26, 13, 25, 34, 38, 23, 37, 31, 28, 32,
24, 25, 13, 38, 34, 48, 19, 20, 22, 38, 28, 31, 18, 21, 24,
31, 21, 28, 29, 33, 40, 26, 33, 33,  6, 27, 24, 17, 28,  7,
33, 25, 25, 29, 19, 30, 29, 22, 15, 28, 36, 25, 36, 25, 29,
33, 19, 32, 32, 28, 26, 18, 48, 15, 27, 27, 27,  0, 28, 39,
27, 25, 39, 28, 22, 33, 30, 35, 19, 20, 18, 31, 44, 20, 18,
17, 28, 17, 44, 40, 33,])

optimal_value = 30

alpha = 0.05  # significación estadística crítica

results = st.ttest_1samp(scooters, optimal_value)

print('valor p: ', results.pvalue)

if results.pvalue < alpha:
    print('Rechazamos la hipótesis nula')
else:
    print("No podemos rechazar la hipótesis nula")
    
    
# ------------ Ejercicio 2

# El 1 de junio de 2019 tomaste un curso del famoso coach y empresario llamado Robby Tobbinson. Si aplicas sus exclusivas técnicas conscientes de negocio se garantiza que tu proyecto online generará al menos $800 por día, quizás más, en solo un mes. Él te lo promete. Las promesas están bien pero las pruebas estadísticas son mejores. Vamos a ver qué nos dicen los números. Utiliza un dataset con los ingresos diarios del último mes para probar tu hipótesis. La hipótesis es que tus ingresos diarios promedio igualaron o superaron los $800. Recuerda: la hipótesis que contiene el signo de igualdad suele ser la hipótesis nula. Por lo tanto, "Todo saldrá como lo predijo el coach" es tu hipótesis nula y "Los ingresos serán menores de lo que se predijo" es la hipótesis alternativa. Las desviaciones aleatorias siempre son posibles. Solo puedes decir "¡La metodología de Tobbinson no funcionó!" si tus ingresos son significativamente inferiores a la cantidad propuesta.

revenue = pd.Series([727, 678, 685, 669, 661, 705, 701, 717, 
                     655,643, 660, 709, 701, 681, 716, 655, 
                     716, 695, 684, 687, 669,647, 721, 681, 
                     674, 641, 704, 717, 656, 725, 684, 665])

interested_value = 800

alpha = 0.05  # el nivel de significancia estadística crítica

results = st.ttest_1samp(revenue, interested_value)

print('valor p:', results.pvalue / 2)

if (results.pvalue / 2 < alpha) and (revenue.mean() < interested_value):
    print(
        "Rechazamos la hipótesis nula: los ingresos fueron significativamente inferiores a 800 dólares"
    )
else:
    print(
        "No podemos rechazar la hipótesis nula: los ingresos no fueron significativamente inferiores"
    )
    
# ------------ Ejercicio 3

# Hay dos conjuntos de datos: el tiempo promedio que pasan en un sitio web 1) los usuarios que inician sesión con nombre de usuario y contraseña, y 2) los usuarios que inician sesión a través de las redes sociales. Prueba la hipótesis de que ambos grupos de usuarios pasan la misma cantidad de tiempo en el sitio web.

# tiempo pasado en el sitio web por usuarios con nombre de usuario y contraseña
time_on_site_logpass = [368, 113, 328, 447, 1, 156, 335, 233, 
                       308, 181, 271, 239, 411, 293, 303, 
                       206, 196, 203, 311, 205, 297, 529, 
                       373, 217, 416, 206, 1, 128, 16, 214]

# tiempo pasado en el sitio web por usuarios que inician sesión a través de redes sociales
time_on_site_social  = [451, 182, 469, 546, 396, 630, 206, 
                        130, 45, 569, 434, 321, 374, 149, 
                        721, 350, 347, 446, 406, 365, 203, 
                        405, 631, 545, 584, 248, 171, 309, 
                        338, 505]

# Nivel de significación
alpha = 0.05

# Prueba t para muestras independientes
results = st.ttest_ind(time_on_site_logpass, time_on_site_social)

# Mostrar valor p
print('valor p:', results.pvalue)

# Decisión
if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

# ------------ Ejercicio 4

# Tenemos dos datasets: la profundidad de la visita al sitio web de diferentes grupos de usuarios para los meses de verano y otoño. Prueba la hipótesis de que las profundidades de visita de los sitios web son iguales. Por ejemplo, puede ser que en verano los visitantes no se sumerjan tanto en el contenido, lo que sería algo a tener en cuenta al planificar una campaña publicitaria para los meses de verano. Vamos a establecer el nivel de significación en 0.05. No esperamos que las varianzas sean las mismas así que establece el parámetro equal_var en False.  Puedes ejecutar np.var(pages_per_session_autumn) etcétera para verificar la varianza del conjunto.

pages_per_session_autumn = [7.1, 7.3, 9.8, 7.3, 6.4, 10.5, 8.7, 
                            17.5, 3.3, 15.5, 16.2, 0.4, 8.3, 
                            8.1, 3.0, 6.1, 4.4, 18.8, 14.7, 16.4, 
                            13.6, 4.4, 7.4, 12.4, 3.9, 13.6, 
                            8.8, 8.1, 13.6, 12.2]

pages_per_session_summer = [12.1, 24.3, 6.4, 19.9, 19.7, 12.5, 17.6, 
                            5.0, 22.4, 13.5, 10.8, 23.4, 9.4, 3.7, 
                            2.5, 19.8, 4.8, 29.0, 1.7, 28.6, 16.7, 
                            14.2, 10.6, 18.2, 14.7, 23.8, 15.9, 16.2, 
                            12.1, 14.5]

# Nivel de significación
alpha = 0.05

# Prueba t para muestras independientes con varianzas desiguales
results = st.ttest_ind(pages_per_session_autumn, pages_per_session_summer, equal_var=False)

# Mostrar valor p
print('valor p:', results.pvalue)

# Decisión
if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")

# ------------ Ejercicio 5


time_before = [1732, 1301, 1540, 2247, 1632, 1550, 754, 1946, 1889, 
          2748, 1349, 1648, 1665, 2416, 1470, 1681, 1868, 1629, 
          1271, 1633, 2131, 942, 1599, 1127, 2200, 661, 1207, 
          1737, 2410, 1486]

time_after = [955, 2577, 360, 139, 1618, 990, 644, 1796, 1487, 949, 472, 
         1906, 1758, 1258, 2554, 612, 309, 1864, 1294, 1487, 1164, 1559, 
         491, 2286, 1270, 2069, 1553, 1629, 1704, 1623]

# # Nivel de significación
alpha = 0.05

# Prueba t para muestras emparejadas (bilateral)
results = st.ttest_rel(time_before, time_after)

# Mostrar valor p
print('valor p:', results.pvalue)

# Decisión
if results.pvalue < alpha:
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")


# ------------ Ejercicio 6 

bullets_before = [821, 1164, 598, 854, 455, 1220, 161, 1400, 479, 215, 
          564, 159, 920, 173, 276, 444, 273, 711, 291, 880, 
          892, 712, 16, 476, 498, 9, 1251, 938, 389, 513]

bullets_after = [904, 220, 676, 459, 299, 659, 1698, 1120, 514, 1086, 1499, 
         1262, 829, 476, 1149, 996, 1247, 1117, 1324, 532, 1458, 898, 
         1837, 455, 1667, 898, 474, 558, 639, 1012]

print('media anterior:', pd.Series(bullets_before).mean())
print('media posterior:', pd.Series(bullets_after).mean())

alpha = 0.05 # significación estadística crítica

results = st.ttest_rel(
    bullets_before, 
    bullets_after)

print('valor-p:', results.pvalue / 2)

if (results.pvalue / 2 < alpha):
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")