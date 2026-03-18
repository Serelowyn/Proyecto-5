import pandas as pd
from math import factorial
import math as mt
import numpy as np
from scipy import stats as st

# ---------- Ejercicio 1

cool_rock = pd.DataFrame(
    {
        'Artist': [
            'Queen',
            'Queen',
            'Queen',
            'Pink Floyd',
            'Nirvana',
            'AC/DC',
            'AC/DC',
            'Scorpions',
            'Scorpions',
            'Scorpions',
        ],
        'Song': [
            'The Show Must Go On',
            'Another One Bites The Dust',
            'We Will Rock You',
            'Wish You Were Here',
            'Smells Like Teen Spirit',
            'Highway To Hell',
            'Back in Black',
            'Wind Of Change',
            'Still Loving You',
            'Send Me An Angel',
        ],
    }
)

desired_artist = 'Queen'

desired_outcomes = len(cool_rock[cool_rock['Artist'] == desired_artist])
total_outcomes = len(cool_rock)
probability = desired_outcomes / total_outcomes
print(probability)

# -------- Ejercicio 2

tasks = 10
permutations = factorial(tasks)
probability = 1 / permutations

print(probability)

# -------- Ejercicio 3

tasks = 10
chosen = 3

combinations = factorial(tasks) / (factorial(chosen) * factorial(tasks-chosen))
probability = 1 / combinations

print(probability)

# --------- Ejercicio 4

# Tenemos a 30 estudiantes que realizaron un examen. Sus puntuaciones se almacenan en la variable exam_results. Si un estudiante obtuvo menos de 20 puntos, reprobó el examen. Escribe un programa que cuente cuántos estudiantes reprobaron el examen y almacena el resultado en la variable failed_students. Muestra el resultado.

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)

failed_students = 0

for score in exam_results:
    if score < 20:
        failed_students += 1

print('Número de estudiantes reprobados:', failed_students)

# --------- Ejercicio 5

# Vamos a seguir con los resultados del examen. Ahora tenemos que contar no solo a los estudiantes que reprobaron, sino también a los que obtuvieron otros resultados: excelente (90 puntos o más), notable (70-89 puntos), satisfactorio (50-69) y aprobado (20-49).

exam_results = np.array(
    [
        42,  56,  59,  76,  43,  34,  62,  51,  50,  65,  
        66,  50,  46,  5,  79, 99,  51,  26,  35,   8,  
        34,  47,  64,  58,  61,  12,  30,  63,  20,  68
    ]
)
summarized_data = {'excellent': 0, 'good': 0, 'average': 0, 'passable': 0, 'failed': 0}

for score in exam_results:
    if score >= 90:
        summarized_data['excellent'] += 1
    elif score >= 70:
        summarized_data['good'] += 1
    elif score >= 50:
        summarized_data['average'] += 1
    elif score >= 20:
        summarized_data['passable'] += 1
    else:
        summarized_data['failed'] += 1

for result in summarized_data:
    print(result, '-', summarized_data[result])
    
# --------- Ejercicio 6

# Los portátiles de Pineapple son caros, pero siguen siendo populares entre los geeks de la informática: el 60% de los clientes están dispuestos a comprarse una computadora portátil de esta marca si acuden a la tienda. Los portátiles de Banana son más baratos, pero no tan populares: solo el 20% de los visitantes de la tienda están dispuestos a comprarlos. Supongamos que la tienda solo tiene a la venta equipos de Pineapple. ¿Cuál es la probabilidad de que 50 de cada 80 clientes realicen una compra en un día? Guarda el resultado en la variable probability y muéstralo. No olvides que en Python se utiliza el signo ** para la exponenciación.

p = 0.6
q = 0.4
n = 80
k = 50

probability = factorial(n) / (factorial(k) * factorial(n-k)) * (p ** k) * (q ** (n-k))

print(probability)


# --------- Ejercicio 7

# Supongamos que, al lado de una tienda de hardware Pineapple, hay un gran centro comercial con otra tienda que vende computadoras Banana. 160 clientes visitan esa tienda durante el día. ¿Cuál es la probabilidad de que 50 de esos visitantes se compren una computadora portátil? Recuerda que solo el 20% de los usuarios están dispuestos a comprar un portátil de la marca Banana. Guarda el resultado en la variable probability y muéstralo.

p = 0.2
q = 0.8
n = 160
k = 50

probability = factorial(n) / (factorial(k) * factorial(n-k)) * (p ** k) * (q ** (n-k))

print(probability)


# --------- Ejercicio 8

# El número de visitantes mensuales de una tienda virtual tiene una distribución normal con una media de 100 500 y una desviación estándar de 3 500. Encuentra la probabilidad de que en el próximo mes el sitio web del outlet tenga:

# menos de 92 000 visitantes;
# más de 111 000 visitantes.
# Completa el código siguiendo los comentarios y utiliza las sentencias print() del precódigo para mostrar tus resultados.

mu = 100500
sigma = 3500

more_threshold = 111000
fewer_threshold = 92000

p_more_visitors = 1 - st.norm(mu, sigma).cdf(more_threshold)
p_fewer_visitors = st.norm(mu, sigma).cdf(fewer_threshold)

print(f'Probabilidad de que el número de visitantes sea superior a {more_threshold}: {p_more_visitors}')
print(f'Probabilidad de que el número de visitantes sea inferior a {fewer_threshold}: {p_fewer_visitors}')

# --------- Ejercicio 9

# Otra tienda online, Fancy Pants, vende productos de regalo a un público muy limitado de clientes corporativos. Las ventas semanales en la tienda de conjuntos de ajedrez de lujo fabricados con colmillo de mamut tienen una distribución normal con una media de 420 y una desviación estándar de 65. El equipo de inventario está decidiendo cuántos conjuntos pedir. Quieren que la posibilidad de venderlos todos la próxima semana sea del 90%. ¿Cuántos deben pedir?

mu = 420
sigma = 65
prob = 0.9

n_shipment = st.norm(mu, sigma).ppf(prob)

print('Cantidad de artículos a pedir:', int(n_shipment))

# --------- Ejercicio 10

# Los precios de los pedidos realizados en una tienda virtual tienen una distribución normal con una media de 24 dólares y una desviación estándar de 3.20 dólares. Algunos clientes eligen la entrega rápida por mensajería, que tiene un precio fijo independientemente del valor del pedido. Los clientes tienden a molestarse cuando el costo de la entrega es igual al costo del pedido. ¿Cuánto debería costar el envío por mensajería para que no supere el precio del pedido en el 75% de los casos?

mu = 24
sigma = 3.2
threshold = .75

max_delivery_price = st.norm(mu, sigma).ppf(1 - threshold)

print('Costo máximo de envío por mensajería:', max_delivery_price)

# --------- Ejercicio 11

# Una empresa envía a sus clientes un boletín electrónico mensual con novedades y ofertas de los socios. Sabemos que el 40% de los clientes abre el boletín. Uno de los socios está planeando una campaña publicitaria y espera llegar a unos 9000 clientes. Calcula la probabilidad de que se cumplan las expectativas del socio si el boletín se envía a 23 000 personas. En el ejemplo anterior, hemos creado una variable llamada clicks. Aquí, crea otra llamada threshold y guarda el valor 9000 en ella. Que el tamaño de la población sea binom_n y que la probabilidad de que se abra el boletín sea binom_p. Guarda la probabilidad de que se cumplan las expectativas del socio como p_threshold y muéstrala.

binom_n = 23000
binom_p = 0.4

threshold = 9000

mu = binom_n * binom_p
sigma = mt.sqrt(binom_n * binom_p * (1 - binom_p))

p_threshold = 1 - st.norm(mu, sigma).cdf(threshold)
print(p_threshold)