import os
os.system("cls")

ls = [1,2,3,1,2,4,5,6,7,7,8,2]
l1 = []
ls.sort()
print(ls)
for i in ls:
    for j in ls:
        if ls[i] == ls[j]:
            ls[i] = 0