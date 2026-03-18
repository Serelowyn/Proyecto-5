# ----------------- Importaciones

import pandas
import numpy
import math
from math import factorial
from scipy import stats

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
df_users["churn_date"] = df_users["churn_date"].fillna("01-01-2018")
df_users['churn_date'] = pandas.to_datetime(df_users['churn_date'], errors='coerce')
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
df_calls['id'] = df_calls['id'].astype(int)
df_calls['user_id'] = df_calls['user_id'].astype(int)

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

print("Información general de las tarifas:\n")
print(df_plans)

# -------------- Calcula el número de llamadas hechas por cada usuario al mes.

# Crear una columna con el mes
df_calls['month'] = df_calls['call_date'].dt.month

# Agrupar por usuario y mes, contar llamadas
calls_per_user_month = df_calls.groupby(['user_id', 'month']).agg(
    calls_count=('id', 'count')
).reset_index()

# Guardar el resultado en un nuevo DataFrame
print(calls_per_user_month.head())

# -------------- Calcula la cantidad de minutos usados por cada usuario al mes

# Agrupar por usuario y mes, sumar minutos
minutes_per_user_month = df_calls.groupby(['user_id', 'month']).agg(
    total_minutes=('duration', 'sum')
).reset_index()

# Guardar el resultado en un nuevo DataFrame
print(minutes_per_user_month.head())

# -------------- Calcula el número de mensajes enviados por cada usuario al mes

df_mensajes['month'] = df_mensajes['message_date'].dt.month

# Agrupar por usuario y mes, contar mensajes
messages_per_user_month = df_mensajes.groupby(['user_id', 'month']).agg(
    sms_count=('id', 'count')
).reset_index()

# Guardar el resultado en un nuevo DataFrame
print(messages_per_user_month.head())

# -------------- Calcula el volumen del tráfico de Internet usado por cada usuario al mes

# Crear columna con el mes
df_internet['month'] = df_internet['session_date'].dt.month

# Agrupar por usuario y mes, sumar MB usados
internet_per_user_month = df_internet.groupby(['user_id', 'month']).agg(
    mb_used=('mb_used', 'sum')
).reset_index()

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
