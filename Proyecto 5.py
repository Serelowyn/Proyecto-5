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