import datetime
import json

import requests
dt_now = datetime.date.today()
#вывод информации о стоимости пая
respose  = requests.get("https://arsagera.ru/api/v1/funds/fa/fund-metrics/?from=2023-12-27&to=2023-12-31")
if respose.status_code == 200:
    # Преобразование JSON в словарь
    data = respose.json()

for i in data['data']:
    print(i['nav_per_share'])
print(data['data'])


#вывод текущей
respose_now = requests.get(f"https://arsagera.ru/api/v1/funds/fa/fund-metrics/?date={dt_now}")
print(respose_now.json())
