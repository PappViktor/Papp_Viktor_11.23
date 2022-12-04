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