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