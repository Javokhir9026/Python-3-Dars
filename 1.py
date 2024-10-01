import os
os.system("cls")

n = int(input("N: "))

lst = []
ylst = []
for i in range(n):
    lst.append((input(f"{i+1}-QIYMAT: ")))
print(lst)

for j in range(len(lst)):
    if lst[j] % 7 == 0:
        ylst[j].append(lst[j])
print(ylst)