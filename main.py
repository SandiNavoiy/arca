import requests

respose  = requests.get("https://arsagera.ru/api/v1/funds/fa/fund-metrics/?total_net_assets")
print(respose.json())