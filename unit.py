from matplotlib import pyplot as plt


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