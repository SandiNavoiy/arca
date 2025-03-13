from datetime import date, timedelta
import requests
# Текущая дата - 2 дня назад
dt_now = date.today() - timedelta(days=2)
print(f"Сегодняшняя дата {date.today()}")
# Список фордов
d = {"fa" : "Арсагера — фонд акций","f4si": "Арсагера — фонд смешанных инвестиций", "f64": "Арсагера — акции 6.4", "fo" : "Арсагера – фонд облигаций КР 1.55" }
#Перебор
for k,v in d.items():
    respose_now = requests.get(f"https://arsagera.ru/api/v1/funds/{k}/fund-metrics/?date={dt_now}")
    if respose_now.status_code == 200:
        print(f"{v}: -  {respose_now.json()['data'][0]['nav_per_share']} рублей, копеек")
    else:
        print(f"{v}: - Нет данных по текущему дню")