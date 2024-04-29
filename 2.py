new = []
with open('1.txt', 'r', encoding="utf-8") as file:
    for i in file:
        if len(i) == 6:
            i = i.replace("\n", "")
            new.append(i)

rez = []
for i in new:
    if  "з" not in i and "е" not in i and "б" not in i and "р" not in i  and "о" not in i and "с" not in i and  i[4] == "а" and  i[2] == "и" and  i[3] == "н":
        rez.append(i)

print(rez)
