import os
os.system("cls")
ls = []   # 1-usul
ls1 = list()  # 2- usul  (LIST)
ls3 = [11,22,33,44,55,66,77]   # 3-usul
print(*ls3)    # '*'  nelgilarni olib tashlaydi 

for i in range(len(ls3)):
    print(ls3[i])

for j in ls3:
    print(j)