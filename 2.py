with open('1.txt', 'r', encoding="utf-8") as file:
    new = [line.strip() for line in file if len(line.strip()) == 5]  # Убираем символ перевода строки сразу и фильтруем длину строки

exclude_chars = set("буквлинзсхемочт")
rez = [i for i in new if not exclude_chars.intersection(i) and i[4] == 'а']

print(rez)




