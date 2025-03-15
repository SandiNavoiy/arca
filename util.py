import datetime
import requests
from matplotlib import pyplot as plt

# Список фондов
d = {
    "fa": "Арсагера — фонд акций",
    "f4si": "Арсагера — фонд смешанных инвестиций",
    "f64": "Арсагера — акции 6.4",
    "fo": "Арсагера – фонд облигаций КР 1.55",
}
# Текущая дата
dt_now = datetime.date.today()
# Задаем диапазон - дат один год
dt_year = datetime.date.today() - datetime.timedelta(days=365)

date1 = dt_year
date2 = dt_now


def stoimost_paiy():
    """Функция вывода стоимости пая всех фондов"""
    dt_now = datetime.date.today() - datetime.timedelta(days=2)
    print(f"Сегодняшняя дата {datetime.date.today()}")
    # Список фордов

    # Перебор
    for k, v in d.items():
        respose_now = requests.get(
            f"https://arsagera.ru/api/v1/funds/{k}/fund-metrics/?date={dt_now}"
        )
        if respose_now.status_code == 200:
            print(
                f"{v}: -  {respose_now.json()['data'][0]['nav_per_share']} рублей, копеек"
            )
        else:
            print(f"{v}: - Нет данных по текущему дню")


def graf():

    print(" Выберите фонд")
    print("fa : Арсагера — фонд акций")
    print("f4si :Арсагера — фонд смешанных инвестиций")
    print("f64: Арсагера — акции 6.4")
    print("fo : Арсагера – фонд облигаций КР 1.55")
    print("Введите из представленных вариантов")
    fond = input()
    if fond in d:
        # вывод информации о стоимости пая
        respose = requests.get(
            f"https://arsagera.ru/api/v1/funds/{fond}/fund-metrics/?from={date1}&to={date2}"
        )
        if respose.status_code == 200:
            # Преобразование JSON в словарь
            data = respose.json()
        x = []
        y = []

        for i in data["data"]:
            x.append(i["date"])
            y.append(i["nav_per_share"])

        # Вывод графического представления об активах фонда
        # Создание графика
        podpis = d[fond]
        plt.plot(x, y, label="График курса")

        # Добавление подписей
        plt.title(podpis)
        plt.xlabel("Ось дат")
        plt.ylabel("Ось значений, руб")

        plt.xticks(x[:: len(x) // 10], rotation=45)

        # Добавление легенды
        plt.legend()

        # Отображение графика
        plt.show()

    else:
        print("Нет такого фонда")
