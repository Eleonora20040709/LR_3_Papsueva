# Работа с Очировой Ириной (7 вариант)

import os
my_secret = os.environ["S1_Papsueva_Ochirova"]
print(S1_Papsueva_Ochirova)

import os
my_secret = os.environ["S2_Papsueva_Ochirova"]
print(S2_Papsueva_Ochirova)

import os
my_secret = os.environ["S3_Papsueva_Ochirova"]
print(S3_Papsueva_Ochirova)

# Индивидуальное задание вариант 8, изменения вариант 7
from sympy import *

k, T, C, L = symbols("k C T L")
# линейный способ
C_ost = 80000 # Изменена начальная стоимость, изменено корректно (Проверено Очировой) 5 баллов
Am_lst = []
C_ost_lst = []
for i in range(5): # Изменено количество периодов, изменено корректно (Проверено Очировой) 5 баллов
    Am = (C - L) / T
    C_ost -= Am.subs({C: 80000, T: 5, L: 0})
    Am_lst.append(round(Am.subs({C: 80000, T: 5, L: 0}), 2))
    C_ost_lst.append(round(C_ost, 2))

print("Am_lst:", Am_lst)
print("C_ost_lst:", C_ost_lst)

# способ уменьшаемого остатка
Aj = 0
C_ost = 80000 # Изменена начальная стоимость, изменено корректно (Проверено Очировой) 5 баллов
Am_lst_2 = []
C_ost_lst_2 = []
for i in range(5): # Изменено количество периодов, изменено корректно (Проверено Очировой) 5 баллов
    Am = k * 1 / T * (C - Aj)
    C_ost -= Am.subs({C: 80000, T: 5, L: 0, k: 2})
    Am_lst_2.append(round(Am.subs({C: 80000, T: 5, L: 0, k: 2}), 2))
    Aj += Am
    C_ost_lst_2.append(round(C_ost, 2))

print("Am_lst_2:", Am_lst_2)
print("C_ost_lst_2:", C_ost_lst_2)

# Контейнер табличного вывода
import pandas as pd

Y = range(1, 6)
table1 = list(zip(Y, C_ost_lst, Am_lst)) # Что это означант? Ответ: это список кортежей, где каждый кортеж содержит значения из трех списков Y, C_ost_lst и Am_lst.
table2 = list(zip(Y, C_ost_lst_2, Am_lst_2))
tfame = pd.DataFrame(table1, columns=["Y", "C_ost_lst", "Am_lst"])
tfame2 = pd.DataFrame(table2, columns=["Y", "C_ost_lst_2", "Am_lst_2"])

print(tfame)
print(tfame2)

# Контейнер визуализации
import numpy as np
import matplotlib.pyplot as plt

plt.plot(tfame["Y"], tfame["C_ost_lst"], label="Am") # Что это означант? Ответ: это построение графика, где по оси X откладываются значения из столбца "Y" таблицы tfame, а по оси Y - значения из столбца "C_
plt.savefig("chart7.png")
plt.figure()
plt.plot(tfame2["Y"], tfame2["C_ost_lst_2"], label="Am_2")
plt.savefig("chart8.png")

plt.figure()
vals = Am_lst
labels = [str(x) for x in range(1, 6)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart9.png")

plt.figure()
vals = Am_lst_2
labels = [str(x) for x in range(1, 6)]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)
fig, ax = plt.subplots()
ax.pie(
    vals,
    labels=labels,
    autopct="%1.1f%%",
    shadow=True,
    explode=explode,
    wedgeprops={"lw": 1, "ls": "--", "edgecolor": "k"},
    rotatelabels=True,
)
ax.axis("equal")
plt.savefig("chart10.png")

plt.figure()
table1 = list(zip(Y, Am_lst))
table2 = list(zip(Y, Am_lst_2))
tfame = pd.DataFrame(table1, columns=["Y", "Am_lst"]) # Что это означант? Ответ: это создание объекта DataFrame из списка кортежей table1 с указанием названий столбцов "Y" и "Am_lst".
tfame2 = pd.DataFrame(table2, columns=["Y", "Am_lst_2"])
plt.bar(tfame["Y"], tfame["Am_lst"])
plt.savefig("chart11.jpeg") 
plt.figure()
plt.bar(tfame2["Y"], tfame2["Am_lst_2"])
plt.savefig("chart12.png")
plt.figure()
