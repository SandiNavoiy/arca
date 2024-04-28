new = []
with open('1.txt', 'r', encoding="utf-8") as file:
    for i in file:
        if len(i) == 6:
            i = i.replace("\n", "")
            new.append(i)

rez = []
for i in new:
    if  "к" not in i and "т" not in i and "и" not in i and "к" not in i   and "а" not in i  and "в" in i  and i[2] == "о" and "с" in i:
        rez.append(i)

print(rez)
