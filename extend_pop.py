import os
os.system("cls")
            #! E X T E N D
ls = [12,34,5,7]
ls1 = ["Salom","Nima","Gap"]

ls.extend(ls1)          # 1-listni 2-listga qoshib beradi
print(ls)

            #! P O P
ls.pop()                # defoult qiymatda list oxiridagi qiymatni ochirib beradi   
print(ls)                

ls.pop(0)                  # 0-indexdagi malumotni ochirib beradi
print(ls)