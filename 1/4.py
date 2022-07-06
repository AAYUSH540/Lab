k = 0
flag = 0
count = 0
l_number = list(input("Number : "))
list_number = []
if len(l_number) == 12:
    while k < len(l_number):
        if k == 3 or k == 7:
            list_number.append(l_number[k])
        else:
            list_number.append(int(l_number[k]))
        k += 1
else:
    flag = 1

print(list_number)

for i in list_number:
    count += 1
    if (i == '-'):
        if (count == 4 or count == 8):
            continue
        else:
            flag = 1
    elif type(i) == int:
        continue
    else:
        flag = 1

if flag == 0:
    print("\n Number :")
    for i in list_number:
        print(f"{i}", end="")
    print(" Is A Valid Number")
else:
    print("\n Number :")
    for i in list_number:
        print(f"{i}", end="")
    print(" Is Not A Valid Number")
