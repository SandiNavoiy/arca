new = []
with open('1.txt', 'r', encoding="utf-8") as file:
    for i in file:
        if len(i) == 6:
            i = i.replace("\n", "")
            new.append(i)

rez = []
for i in new:
    if  "з" not in i and "е" not in i and "б" not in i and "р" not in i  and "а" not in i and "с" not in i and "д" not in i and "н" not in i and "ч" not in i and i[1] == "у" and i[3] == "о" and "п" in i and "к" in i:
        rez.append(i)

print(rez)
