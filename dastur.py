import os
import sys
os.system("cls")

print("\t\t...>>> LISTGA MALUMOT KIRITISH <<<...")
ls = [input("\tMa'lumot: ")]
os.system("cls")

print("\t\t\t...>>> M E N Y U <<<...\n")
print("\t(1) Listni Ko'rish          \t(3) Listdan Ma'lumot o'chirish")
print("\t(2) Listga Ma'lumot qo'shish\t(4) Listga bir necha Ma'lumot qo'shish")

t = int(input())

if t == 1:
    os.system("cls")
    print("\t\t\t...>>> LIST MA'LUMOTI <<<...\n")
    print("\tLIST QIYMATI >> ",ls)
elif t == 2:
    os.system("cls")
    print("\t\t\t...>>> MA'LUMOT QO'SHISH <<<...\n")    
    print("\t(1) APPEND ORQALi    \t(2) INDEX ORQALI")
    t2 = int(input())
    if t2 == 1:
        print("\t\t\t...>>> A P P E N D <<<...\n")
        ss = int(input("N: "))
        for i in range(ss):
            ls.append(int(input("\tQIYMAT: ")))
        print("\t\t Ma'lumot qo'shildi ! ")
        print("\t(1) LIST YANGI MALUMOTNI KO'RISH\t(2) TUGATISH")
        t3 = int(input())
        if t3 == 1:
            print(ss)
        elif t3 == 2:
            exit
        else:
            print("\t\t NOTOGRI TANLOV !!! ")
    elif t2 == 2:
        os.system("cls")
        print("\t\t\t...>>> I N D E X <<<...\n")
        n1 = int(input("\tINDEX: "))
        mal = input("\tMALUMOT: ")
        ls.insert(n1, mal)  
        print("\t\t Ma'lumot qo'shildi ! ")
        print("\t(1) LIST YANGI MALUMOTNI KO'RISH\t(2) TUGATISH")
        t3 = int(input())
        if t3 == 1:
            print(ls)
        elif t3 == 2:
            exit
        else:
            print("\t\t NOTOGRI TANLOV !!! ")
    else:
        print("\t\t NOTOGRI TANLOV !!! ")
elif t == 3:
    os.system("cls")
    print("\t\t...>>> LISTDAN MALUMOT OCHIRISH <<<...\n")
    