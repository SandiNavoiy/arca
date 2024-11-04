new = []
with open('1.txt', 'r', encoding="utf-8") as file:
    for i in file:
        if len(i) == 6:
            i = i.replace("\n", "")
            new.append(i)

rez = []
for i in new:
    if "б" not in i and  "у" not in i and "к" not in i and "а" not in i and "п" not in i and "ю" not in i and "н" not in i  and "р" not in i  and "д" not in i   and "ш" not in i   and "м" not in i  and "е" not in i and i[3] == "в" :
        rez.append(i)

print(rez)
