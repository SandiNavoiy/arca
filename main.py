import datetime
import matplotlib.pyplot as plt

import requests
#Текущая дата
dt_now = datetime.date.today()
#Задаем диапазон дат
date1 = datetime.date(2023, 12, 27)
date2 = datetime.date(2023, 12, 30)

#вывод информации о стоимости пая
respose  = requests.get(f"https://arsagera.ru/api/v1/funds/fa/fund-metrics/?from={date1}&to={date2}")
if respose.status_code == 200:
    # Преобразование JSON в словарь
    data = respose.json()
x = []
y = []
index = date1
for i in data['data']:
    x.append(str(index))
    index += datetime.timedelta(days=1)

    y.append(i['nav_per_share'])

# print(data['data'])
#Вывод графического представления об активах фонда
plt.plot(x,y)
plt.title("Активы фонда")
plt.xlabel("Дни")
plt.ylabel("Сумма")
plt.show()


#вывод текущей
print("вывод текущей")
respose_now = requests.get(f"https://arsagera.ru/api/v1/funds/fa/fund-metrics/?date={dt_now}")
print(respose_now.json())
