import os
os.system("cls")

ls = []
jls = []
tls = []

n = int(input("N: "))

for i in range(n):
    son = int(input(f"{i+1}-Qiymat >> "))
    ls.append(son)

for i in ls:
    if i % 2 == 0:
        jls.append(i)
    elif i % 2 != 0:
        tls.append(i)
print("TOQLAR ==> ",tls)
print("JUFTLAR ==> ",jls)