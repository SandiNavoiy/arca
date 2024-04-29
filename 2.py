new = []
with open('1.txt', 'r', encoding="utf-8") as file:
    for i in file:
        if len(i) == 6:
            i = i.replace("\n", "")
            new.append(i)

rez = []
for i in new:
    if  "з" not in i and "е" not in i and "б" not in i and "р" not in i   and "ш" not in i  and "ю" not in i and "х" not in i and "ф" not in i  and "ь" not in i and "г" not in i and "в" not in i and  i[4] == "а" and  i[1] == "л" and  i[2] != "а" and  i[2] == "и" and "э" not in i and "т" not in i:
        rez.append(i)

print(rez)
