from util import stoimost_paiy, graf

print(" Выберите действие")
print("1 : Вывод графического представления об активах фонда")
print("2 : Вывод информации о стоимости пая")
k = input()
if k == "1":
    graf()

elif k == "2":
    stoimost_paiy()
