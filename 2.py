with open('1.txt', 'r', encoding="utf-8") as file:
    new = [line.strip() for line in file if len(line.strip()) == 5]  # Убираем символ перевода строки сразу и фильтруем длину строки

exclude_chars = set("буквслинзй")
rez = [i for i in new if not exclude_chars.intersection(i) and i[1] == "а" and i[3] == "о" and i[0] != "м" and i[4] != "р" and i[1] != "п" and i[4] != "а"]

print(rez)