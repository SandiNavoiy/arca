from datetime import date, timedelta

import requests

dt_now = date.today() - timedelta(days=2)
print(dt_now)
# fa : "Арсагера — фонд акций" f4si : "Арсагера — фонд смешанных инвестиций" f64 : "Арсагера — акции 6.4" fo : "Арсагера – фонд облигаций КР 1.55"
# nav_per_share : Стоимость пая. Тип: float.
respose_now = requests.get(f"https://arsagera.ru/api/v1/funds/fa/fund-metrics/?date={dt_now}")

print(respose_now.json())