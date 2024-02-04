import datetime
import matplotlib.pyplot as plt

import requests
#Текущая дата
dt_now = datetime.date.today()
#Задаем диапазон дат
date1 = datetime.date(2023, 11, 27)
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


#Вывод графического представления об активах фонда
def grafic(os_x,os_y):
    """Вывод графической части"""
    plt.plot(os_x,os_y)
    plt.title("Активы фонда")
    plt.xlabel("Дни")
    plt.ylabel("Сумма")
    if len(os_x)<10:
        k = 1
    elif 10 <= len(os_x) <= 100:
        k = 20
    elif len(os_x) > 100:
        k = 50
    plt.xticks(os_x[::k], rotation=45)
    plt.show()

grafic(x,y)
#вывод текущей
print("вывод текущей")
respose_now = requests.get(f"https://arsagera.ru/api/v1/funds/fa/fund-metrics/?date={dt_now}")
print(respose_now.json())
