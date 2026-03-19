# ----------------- Importaciones

import pandas
import numpy
from scipy import stats
from matplotlib import pyplot
import seaborn

# ----------------- Fin de las importaciones

# ----------------- Se abren los archivos

df_calls = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 5\\megaline_calls.csv")
df_internet = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 5\\megaline_internet.csv")
df_mensajes = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 5\\megaline_messages.csv")
df_plans = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 5\\megaline_plans.csv")
df_users = pandas.read_csv(r"C:\\Users\\sasor\\Desktop\\Tripleten\\Sprint 5\\megaline_users.csv")

# ----------------------------

# -------------- 1.4 TARIFAS (plans)

# Imprime la información general/resumida sobre el DataFrame de las tarifas

df_plans.describe()
df_plans.dtypes
df_plans.info()
df_plans.isna()

# Imprime una muestra de los datos para las tarifas

print(df_plans.head())

# -------------- 1.5 Corregir datos (plans)

# de mb a gb
df_plans['gb_per_month_included'] = df_plans['mb_per_month_included'] / 1024

# -------------- 1.6 Enriquecer datos (plans)

#minusculas
df_plans['plan_name'] = df_plans['plan_name'].str.lower()

#revisar tipo de dato
df_plans['usd_per_minute'] = df_plans['usd_per_minute'].astype(float)
df_plans['usd_per_message'] = df_plans['usd_per_message'].astype(float)
df_plans['usd_per_gb'] = df_plans['usd_per_gb'].astype(float)

print(df_plans.head())

# -------------- 1.7 Usuarios (users)

# Imprime la información general/resumida sobre el DataFrame de usuarios
df_users.describe()
df_users.dtypes
df_users.info()
df_users.isna()

# Imprime una muestra de datos para usuarios
print(df_users.head())

# -------------- 1.7.1 Correccion de datos (users)

# 1. Convertir fechas a tipo datetime
df_users['reg_date'] = pandas.to_datetime(df_users['reg_date'], errors='coerce')
df_users['churn_date'] = pandas.to_datetime(df_users['churn_date'], errors='coerce')

# 2. Minusculas nombres de planes
df_users['plan'] = df_users['plan'].str.lower()

# 3. Asegurar tipos de datos correctos
df_users['user_id'] = df_users['user_id'].astype(int)
df_users['age'] = df_users['age'].astype(int)

# 4. Opcional: limpiar nombres de ciudades (ejemplo: quitar "MSA")
df_users['city'] = df_users['city'].str.replace(' MSA', '', regex=False)

# 5. Revisar valores faltantes y rellenar
print(df_users.isna().sum())
print(df_users)

# -------------- 1.8 Llamadas (calls)

# Imprime la información general/resumida sobre el DataFrame de usuarios
df_calls.describe()
df_calls.dtypes
df_calls.info()
df_calls.isna()

# Imprime una muestra de datos para usuarios
print(df_calls.head())

# 1. Convertir la fecha al formato correcto
df_calls['call_date'] = pandas.to_datetime(df_calls['call_date'], errors='coerce')

# 2. Asegurar que la duración sea numérica (float)
df_calls['duration'] = df_calls['duration'].astype(float)

# 3. Convertir id y user_id a enteros
df_calls['id'] = df_calls['id'].astype(str)
df_calls['user_id'] = df_calls['user_id'].astype(str)

# 4. Revisar valores faltantes
print(df_calls.isna().sum())

# -------------- 1.9 Mensajes (mensajes)

# Imprime la información general/resumida sobre el DataFrame de usuarios
df_mensajes.describe()
df_mensajes.dtypes
df_mensajes.info()
df_mensajes.isna()

# Imprime una muestra de datos para usuarios
print(df_mensajes.head())

# 1. Convertir la fecha al formato correcto
df_mensajes['message_date'] = pandas.to_datetime(df_mensajes['message_date'], errors='coerce')

# 2. Convertir id y user_id a enteros
df_mensajes['id'] = df_mensajes['id'].astype(int)
df_mensajes['user_id'] = df_mensajes['user_id'].astype(int)

# 3. Revisar valores faltantes
print(df_mensajes.isna().sum())

# -------------- 1.10 Internet (internet)

# Imprime la información general/resumida sobre el DataFrame de usuarios
df_internet.describe()
df_internet.dtypes
df_internet.info()
df_internet.isna()

# Imprime una muestra de datos para usuarios
print(df_internet.head())

# 1. Convertir la fecha al formato correcto
df_internet['session_date'] = pandas.to_datetime(df_internet['session_date'], errors='coerce')

# 2. Asegurar que la duración sea numérica (float)
df_internet['mb_used'] = df_internet['mb_used'].astype(float)

# 3. Convertir id y user_id a enteros
df_internet['id'] = df_internet['id'].astype(int)
df_internet['user_id'] = df_internet['user_id'].astype(int)

# 4. Revisar valores faltantes
print(df_internet.isna().sum())

# -------------- 1.11 Estudiar las condiciones de Tarifa

print(df_plans)

# -------------- Calcula el número de llamadas hechas por cada usuario al mes.

# Crear una columna con el mes
df_calls['month'] = df_calls['call_date'].dt.month
df_calls['duration_ceil'] = numpy.ceil(df_calls['duration'])

# Agrupar por usuario y mes, contar llamadas
calls_per_user_month = df_calls.groupby(['user_id', 'month']).agg(
    calls_count=('id', 'count')
).reset_index()
calls_per_user_month['user_id'] = calls_per_user_month['user_id'].astype(int)
calls_per_user_month['month'] = calls_per_user_month['month'].astype(int)

# Guardar el resultado en un nuevo DataFrame
print(calls_per_user_month.head())

# -------------- Calcula la cantidad de minutos usados por cada usuario al mes

# Redondear cada llamada hacia arriba al minuto entero
df_calls['duration_ceil'] = numpy.ceil(df_calls['duration'])

# Agrupar por usuario y mes, sumar minutos
minutes_per_user_month = df_calls.groupby(['user_id', 'month']).agg(
    total_minutes=('duration_ceil', 'sum')
).reset_index()
minutes_per_user_month['user_id'] = minutes_per_user_month['user_id'].astype(int)
minutes_per_user_month['month'] = minutes_per_user_month['month'].astype(int)

# Guardar el resultado en un nuevo DataFrame
print(minutes_per_user_month.head())

# -------------- Calcula el número de mensajes enviados por cada usuario al mes

df_mensajes['month'] = df_mensajes['message_date'].dt.month

# Agrupar por usuario y mes, contar mensajes
messages_per_user_month = df_mensajes.groupby(['user_id', 'month']).agg(
    sms_count=('id', 'count')
).reset_index()
messages_per_user_month['user_id'] = messages_per_user_month['user_id'].astype(int)
messages_per_user_month['month'] = messages_per_user_month['month'].astype(int)

# Guardar el resultado en un nuevo DataFrame
print(messages_per_user_month.head())

# -------------- Calcula el volumen del tráfico de Internet usado por cada usuario al mes

# Crear columna con el mes
df_internet['month'] = df_internet['session_date'].dt.month

# Agrupar por usuario y mes, sumar MB usados
internet_per_user_month = df_internet.groupby(['user_id', 'month']).agg(
    mb_used=('mb_used', 'sum')
).reset_index()

# Convertir MB a GB y aplicar redondeo hacia arriba para facturación
internet_per_user_month['gb_used_for_billing'] = numpy.ceil(internet_per_user_month['mb_used'] / 1024)
internet_per_user_month['user_id'] = internet_per_user_month['user_id'].astype(int)
internet_per_user_month['month'] = internet_per_user_month['month'].astype(int)

# Guardar el resultado en un nuevo DataFrame
print(internet_per_user_month.head())

# -------------- Fusionar datoss

# Fusionar llamadas y minutos
calls_data = calls_per_user_month.merge(minutes_per_user_month, on=['user_id', 'month'], how='outer')

# Agregar mensajes
calls_messages_data = calls_data.merge(messages_per_user_month, on=['user_id', 'month'], how='outer')

# Agregar internet
user_month_data = calls_messages_data.merge(internet_per_user_month, on=['user_id', 'month'], how='outer')

# Rellenar valores faltantes con 0 (usuarios que no hicieron llamadas, SMS o internet ese mes)
user_month_data = user_month_data.fillna(0)

# Mostrar una muestra del resultado
print(user_month_data.head())

# Añade la información de la tarifa


user_month_data = user_month_data.merge(
    df_users[['user_id', 'plan', 'city']], 
    on='user_id', 
    how='left'
)

# 2. Unir con la tabla de planes para obtener condiciones de cada tarifa
user_month_data = user_month_data.merge(
    df_plans, 
    left_on='plan', 
    right_on='plan_name', 
    how='left'
)

# 3. Mostrar una muestra del resultado
print(user_month_data.head())


# -------------- Calcula el ingreso mensual para cada usuario

# Convertir MB a GB para comparar con el límite del plan
user_month_data['gb_used'] = user_month_data['mb_used'] / 1024
user_month_data['gb_used_for_billing'] = numpy.ceil(user_month_data['mb_used'] / 1024)

# Calcular excedentes de minutos, SMS y GB
user_month_data['extra_minutes'] = numpy.maximum(user_month_data['total_minutes'] - user_month_data['minutes_included'], 0)
user_month_data['extra_sms'] = numpy.maximum(user_month_data['sms_count'] - user_month_data['messages_included'], 0)
user_month_data['extra_gb'] = numpy.maximum(user_month_data['gb_used_for_billing'] - user_month_data['gb_per_month_included'], 0)


# Calcular costo de excedentes
user_month_data['cost_minutes'] = user_month_data['extra_minutes'] * user_month_data['usd_per_minute']
user_month_data['cost_sms'] = user_month_data['extra_sms'] * user_month_data['usd_per_message']
user_month_data['cost_gb'] = user_month_data['extra_gb'] * user_month_data['usd_per_gb']

# Calcular ingreso mensual total por usuario
user_month_data['monthly_revenue'] = (
    user_month_data['usd_monthly_pay'] +
    user_month_data['cost_minutes'] +
    user_month_data['cost_sms'] +
    user_month_data['cost_gb']
)

print(user_month_data[['user_id', 'month', 'plan', 'monthly_revenue']].head())

# -------------- 1.13.1 Llamadas

# -------------- Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.

avg_minutes = user_month_data.groupby(['plan', 'month']).agg(
    avg_call_duration=('total_minutes', 'mean')
).reset_index()

print(avg_minutes.head())

# Gráfico de barras
pyplot.figure(figsize=(10,6))
for plan in avg_minutes['plan'].unique():
    subset = avg_minutes[avg_minutes['plan'] == plan]
    pyplot.bar(subset['month'] + (0.2 if plan == 'ultimate' else -0.2), 
            subset['avg_call_duration'], 
            width=0.4, 
            label=plan.capitalize())

pyplot.xlabel("Mes")
pyplot.ylabel("Duración promedio de llamadas (minutos)")
pyplot.title("Duración promedio de llamadas por plan y mes")
pyplot.legend()
pyplot.xticks(range(1,13))
pyplot.show()


# -------------- Compara el número de minutos mensuales que necesitan los usuarios de cada plan. Traza un histograma.

# Seleccionar columnas relevantes
minutes_by_plan = user_month_data[['plan', 'total_minutes']]

# Crear el histograma
pyplot.figure(figsize=(10,6))

for plan in minutes_by_plan['plan'].unique():
    subset = minutes_by_plan[minutes_by_plan['plan'] == plan]
    pyplot.hist(subset['total_minutes'], 
             bins=30, 
             alpha=0.6, 
             label=plan.capitalize())

pyplot.xlabel("Minutos mensuales usados")
pyplot.ylabel("Número de usuarios")
pyplot.title("Distribución de minutos mensuales por plan")
pyplot.legend()
pyplot.show()

# -------------- Calcula la media y la varianza de la duración mensual de llamadas.

# Calcular la media de minutos mensuales
minutes_stats = user_month_data.groupby('plan')['total_minutes'].agg(
    mean='mean',
    var='var'
).reset_index()

print(minutes_stats)
# -------------- Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas

# Crear el diagrama de caja
pyplot.figure(figsize=(8,6))
user_month_data.boxplot(column='total_minutes', by='plan')

pyplot.title("Distribución de la duración mensual de llamadas por plan")
pyplot.suptitle("")  # Elimina el título automático de pandas
pyplot.xlabel("Plan")
pyplot.ylabel("Minutos mensuales usados")
pyplot.show()

# -------------- 1.13.2 Mensajes

# -------------- Comprara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan

# Seleccionar columnas relevantes
messages_by_plan = user_month_data[['plan', 'month', 'sms_count']]

# Calcular promedio de mensajes por plan y mes
avg_messages = messages_by_plan.groupby(['plan', 'month']).agg(
    avg_sms=('sms_count', 'mean')
).reset_index()

print(avg_messages.head())

# Graficar
pyplot.figure(figsize=(10,6))
for plan in avg_messages['plan'].unique():
    subset = avg_messages[avg_messages['plan'] == plan]
    pyplot.bar(subset['month'] + (0.2 if plan == 'ultimate' else -0.2),
            subset['avg_sms'],
            width=0.4,
            label=plan.capitalize())

pyplot.xlabel("Mes")
pyplot.ylabel("Número promedio de mensajes")
pyplot.title("Mensajes promedio enviados por mes según el plan")
pyplot.legend()
pyplot.xticks(range(1,13))
pyplot.show()

# -------------- Compara la cantidad de tráfico de Internet consumido por usuarios por plan

# Convertir MB a GB para facilitar la interpretación
user_month_data['gb_used'] = user_month_data['mb_used'] / 1024

# Calcular promedio de GB usados por plan y mes
avg_internet = user_month_data.groupby(['plan', 'month']).agg(
    avg_gb=('gb_used', 'mean')
).reset_index()

print(avg_internet.head())

# Graficar comparación por plan
pyplot.figure(figsize=(10,6))
for plan in avg_internet['plan'].unique():
    subset = avg_internet[avg_internet['plan'] == plan]
    pyplot.bar(subset['month'] + (0.2 if plan == 'ultimate' else -0.2),
            subset['avg_gb'],
            width=0.4,
            label=plan.capitalize())

pyplot.xlabel("Mes")
pyplot.ylabel("Promedio de GB usados")
pyplot.title("Consumo promedio de Internet por plan y mes")
pyplot.legend()
pyplot.xticks(range(1,13))
pyplot.show()

# -------------- 1.13.3 Internet

internet_stats = user_month_data.groupby('plan')['gb_used'].agg(
    mean='mean',
    median='median',
    var='var',
    std='std',
    min='min',
    max='max'
).reset_index()

print(internet_stats)

#grafico de violin
pyplot.figure(figsize=(8,6))
seaborn.violinplot(x='plan', y='gb_used', data=user_month_data, inner='quartile')

pyplot.title("Distribución del consumo mensual de Internet por plan")
pyplot.xlabel("Plan")
pyplot.ylabel("GB usados al mes")
pyplot.show()

#grafico de densidad
pyplot.figure(figsize=(10,6))
for plan in user_month_data['plan'].unique():
    subset = user_month_data[user_month_data['plan'] == plan]
    seaborn.kdeplot(subset['gb_used'], label=plan.capitalize(), fill=True, alpha=0.4)

pyplot.xlabel("GB mensuales usados")
pyplot.ylabel("Densidad")
pyplot.title("Distribución de consumo de Internet por plan (KDE)")
pyplot.legend()
pyplot.show()

# -------------- 1.14 Ingreso

# Paso 1: Estadísticas descriptivas de ingresos por plan
income_stats = user_month_data.groupby('plan')['monthly_revenue'].agg(
    mean='mean',
    median='median',
    var='var',
    std='std',
    min='min',
    max='max'
).reset_index()

print(income_stats)

# Paso 2: Evolución mensual del ingreso promedio por plan
avg_income = user_month_data.groupby(['plan','month']).agg(
    avg_revenue=('monthly_revenue','mean')
).reset_index()

pyplot.figure(figsize=(10,6))
for plan in avg_income['plan'].unique():
    subset = avg_income[avg_income['plan'] == plan]
    pyplot.plot(subset['month'], subset['avg_revenue'], marker='o', label=plan.capitalize())

pyplot.xlabel("Mes")
pyplot.ylabel("Ingreso promedio mensual (USD)")
pyplot.title("Ingreso promedio mensual por plan")
pyplot.legend()
pyplot.xticks(range(1,13))
pyplot.show()

# Paso 3: Gráfico de violín para distribución de ingresos
pyplot.figure(figsize=(8,6))
seaborn.violinplot(x='plan', y='monthly_revenue', data=user_month_data, inner='quartile')

pyplot.title("Distribución de ingresos mensuales por plan")
pyplot.xlabel("Plan")
pyplot.ylabel("Ingreso mensual (USD)")
pyplot.show()

# Paso 4: Histograma comparativo
pyplot.figure(figsize=(10,6))
for plan in user_month_data['plan'].unique():
    subset = user_month_data[user_month_data['plan'] == plan]
    pyplot.hist(subset['monthly_revenue'], bins=30, alpha=0.6, label=plan.capitalize())

pyplot.xlabel("Ingreso mensual (USD)")
pyplot.ylabel("Número de usuarios")
pyplot.title("Distribución de ingresos por plan")
pyplot.legend()
pyplot.show()

# -------------- 1.15 Prueba de hipotesis

# Separar ingresos por plan
surf_income = user_month_data[user_month_data['plan'] == 'surf']['monthly_revenue']
ultimate_income = user_month_data[user_month_data['plan'] == 'ultimate']['monthly_revenue']

# Prueba t de Student para muestras independientes
t_stat, p_value = stats.ttest_ind(surf_income, ultimate_income, equal_var=False)

print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_value:.4f}")

# Visualización: Boxplot comparativo
pyplot.figure(figsize=(8,6))
seaborn.boxplot(x='plan', y='monthly_revenue', data=user_month_data)
pyplot.title("Comparación de ingresos mensuales por plan")
pyplot.xlabel("Plan")
pyplot.ylabel("Ingreso mensual (USD)")
pyplot.show()

# Visualización: Distribución KDE
pyplot.figure(figsize=(10,6))
seaborn.kdeplot(surf_income, label="Surf", fill=True, alpha=0.4)
seaborn.kdeplot(ultimate_income, label="Ultimate", fill=True, alpha=0.4)
pyplot.title("Distribución de ingresos mensuales por plan")
pyplot.xlabel("Ingreso mensual (USD)")
pyplot.ylabel("Densidad")
pyplot.legend()
pyplot.show()


#por region

# Separar ingresos por región
ny_income = user_month_data[user_month_data['city'] == 'New York-Newark-Jersey City, NY-NJ-PA']['monthly_revenue']
other_income = user_month_data[user_month_data['city'] != 'New York-Newark-Jersey City, NY-NJ-PA']['monthly_revenue']

# Prueba t de Student para muestras independientes
t_stat, p_value = stats.ttest_ind(ny_income, other_income, equal_var=False)

print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_value:.4f}")

# Visualización: Boxplot comparativo New York-Newark-Jersey City, NY-NJ-PA
pyplot.figure(figsize=(8,6))
seaborn.boxplot(x=user_month_data['city'].apply(lambda r: 'New York-Newark-Jersey City, NY-NJ-PA' if r=='New York-Newark-Jersey City, NY-NJ-PA' else 'Otros'),
            y=user_month_data['monthly_revenue'])
pyplot.title("Comparación de ingresos mensuales: NY-NJ vs otras regiones")
pyplot.xlabel("Región")
pyplot.ylabel("Ingreso mensual (USD)")
pyplot.show()

# Visualización: Distribución KDE
pyplot.figure(figsize=(10,6))
seaborn.kdeplot(ny_income, label="NY-NJ", fill=True, alpha=0.4)
seaborn.kdeplot(other_income, label="Otros", fill=True, alpha=0.4)
pyplot.title("Distribución de ingresos mensuales por región")
pyplot.xlabel("Ingreso mensual (USD)")
pyplot.ylabel("Densidad")
pyplot.legend()
pyplot.show()
