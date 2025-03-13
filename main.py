import datetime
import requests
from matplotlib import pyplot as plt


#Текущая дата
dt_now = datetime.date.today()
#Задаем диапазон дат один год
dt_year = datetime.date.today() - datetime.timedelta(days=365)

date1 = dt_year
date2 = dt_now

print(" Выберите фонд")
print("fa : Арсагера — фонд акций")
print("f4si :Арсагера — фонд смешанных инвестиций")
print("f64: Арсагера — акции 6.4")
print("fo : Арсагера – фонд облигаций КР 1.55")
print("Введите из представленных вариантов")
fond = input()

#вывод информации о стоимости пая
respose  = requests.get(f"https://arsagera.ru/api/v1/funds/{fond}/fund-metrics/?from={date1}&to={date2}")
if respose.status_code == 200:
    # Преобразование JSON в словарь
    data = respose.json()
x = []
y = []
index = date1
for i in data['data']:
    x.append(str(index))
    index += datetime.timedelta(days=30)

    y.append(i['nav_per_share'])

d = {"fa" : "Арсагера — фонд акций","f4si": "Арсагера — фонд смешанных инвестиций", "f64": "Арсагера — акции 6.4", "fo" : "Арсагера – фонд облигаций КР 1.55" }
#Вывод графического представления об активах фонда
# Создание графика
podpis = d[fond]
plt.plot(x, y, label="График курса")

# Добавление подписей
plt.title(podpis)
plt.xlabel("Ось дат")
plt.ylabel("Ось значений, руб")

# Добавление легенды
plt.legend()

# Отображение графика
plt.show()
