from data import * 
from os import system 



def menu():
    system('cls')
    print("Pékség neve")
    print("0 - Kilépés")
    print("1 - Termékek kiírása")
    print("2 - Új termék hozzáadása")
    print("3 - Termék törlése ")
    print("4 - Bevásárlólista kiírása ")
    print("5 - Bevásálólistaba termék hozzáadása")
    print("6 - Bevásárlólista törlése ")
    return input("Választás: ")

def Beolvas():
    file=open("aru.csv","r", encoding="utf-8")

    for egysor in file:
        darabolt=egysor.strip().split(",")
        aru.append(darabolt[0])
        ar.append(int(darabolt[1]))
        kaloria.append(int(darabolt[2]))
    file.close

def BeolvasBev():
    file=open("bevasarlolista.csv","r", encoding="utf-8")
    
    for egysor in file:
        darabolt=egysor.strip().split(",")
        Termek.append(darabolt[0])
        db.append(int(darabolt[1]))
        
    file.close

def kiir():
    system("cls")
    print("asd")
    for i in range(0,len(aru)):
        print(f"\t {i+1} {(aru[i])}, {(ar[i])}, {(kaloria[i])} " )
    input()

def ujaru():
    system("cls")
    print("új termék")
    ujtermek=input("Termék neve: ")
    ujar=int(input("Ára(Ft): "))
    ujkal=float(input("A termék kalória tartalma: "))
    aru.append(ujtermek)
    ar.append(ujar)
    kaloria.append(ujkal)
    end(ujtermek,ujar,ujkal)
    input("")    

def end(aru,ar,kaloria):
    file=open("aru.csv","a",encoding="utf-8")
    file.write(f'\n{aru},{ar},{kaloria}')
    file.close()

def kiir1():
    system("cls")
    print("asd")
    for i in range(0,len(aru)):
        print(f"\t {i+1} {(aru[i])}, {(ar[i])}, {(kaloria[i])} " )

def torles():
    system("cls")
    print("asd")
    kiir1()
    tor=int(input("Melyik termeket töröljem ki?: "))
    aru.pop(tor-1)
    ar.pop(tor-1)
    kaloria.pop(tor-1)
    ment()
    input()

def ment():
    file=open("aru.csv", "w", encoding="utf-8")
    for i in range(len(aru)):
        file.write(f"{aru[i]},{ar[i]},{kaloria[i]}")
        if len(aru)-1>i:
            file.write("\n")
    file.close

def bevkiir():
    system("cls")
    print("asd")
    for i in range(0,len(Termek)):
        print(f"\t {i+1}. {(Termek[i])}, {(db[i])}, ")
    input()

def bevtor():
    system("cls")
    file=open("bevasarlolista.csv","w", encoding="utf-8")
    file.pop("bevasarlolista.csv")

def bevuj():
    system("cls")
    kiir1()
    új=int(input(" "))
    
    