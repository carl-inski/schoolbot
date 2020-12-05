import time
from datetime import date
import random
import colorama
import os
from colorama import init, Fore, Style
init()
init(autoreset=True)


schulaufgaben_liste = []
schulaufgaben_datum = []
schulaufgaben_counter = 1
datum_counter = 0



def schulaufgabe_eintagen():
  
  global schulaufgaben_liste
  global schulaufgaben_datum

  clear = lambda: os.system("clear")
  clear()
  print (Fore.RED + "SchulBot\n\n")
  print (Fore.BLUE + "Eintragen\n")

  schulaufgaben_liste.append(input("In welchem Fach ist die Schulaufgabe?\n"))

  datum_tag = int(input("\nAn welchem Tag ist die Schulaufgabe?\n"))
  datum_monat = int(input("In welchem Monat ist die Schulaufgabe?\n"))
  datum_jahr = int(input("In welchem Jahr ist die Schulaufgabe?\n"))

  datum_gesammt = date(datum_jahr, datum_monat, datum_tag)

  schulaufgaben_datum.append(datum_gesammt)

  

  print("\n\n")
  print ("1 - Weitere Schulaufgabe eintragen ")
  print ("2 - Zurück zum Menü\n")
  nochmal = input("Was möchtest du jetzt tun?\n")
  if nochmal == "1":
    schulaufgabe_eintagen()
  elif nochmal == "2":
    menu()
  else:
    zurück = input("\nGib bitte eine gültige Zahl ein.\nDrücke Enter für erneute Eingabe")
    schulaufgabe_eintagen()

def schulaufgaben_einsehen():
  clear = lambda: os.system("clear")
  clear()
  print (Fore.RED + "SchulBot\n\n")
  print (Fore.BLUE + "Einsehen\n")

  global datum_counter
  schulaufgaben_counter = 1
  datum_counter = 0

  if len(schulaufgaben_liste) == 0:
    print("Du hast noch keine Schulaufgaben. Gehe im Menü auf 'Eintragen', um Schulaufgaben hinzuzufügen")

  for i in schulaufgaben_liste:
    print(schulaufgaben_counter, "-", i)
    print_datum = schulaufgaben_datum[datum_counter]
    print(print_datum.strftime("%d.%m.%Y"),"\n")
    schulaufgaben_counter += 1
    datum_counter += 1


  print("\n")

  weiter = input("Drücke Enter um zurück zum Menü zu gelangen")
  menu()

def schulaufgaben_löschen():
  global schulaufgaben_liste

  clear = lambda: os.system("clear")
  clear()
  print (Fore.RED + "SchulBot\n\n")
  print (Fore.BLUE + "Löschen\n")

  if len(schulaufgaben_liste) == 0:
    print("Du hast noch keine Schulaufgaben. Gehe im Menü auf 'Eintragen', um Schulaufgaben hinzuzufügen\n")
    zurück = input("Drücke Enter, um zurück zum Menü zu gelangen")
    menu()

  schulaufgaben_counter = 1

  for i in schulaufgaben_liste:
    print(schulaufgaben_counter, "-", i)
    schulaufgaben_counter += 1
  
  print("\n")

  lösch_zahl = input("Welche Schulaufgabe möchtest du löschen?\n")

  if int(lösch_zahl) > len(schulaufgaben_liste):
    zurück = input("\nGib bitte eine gültige Zahl ein.\nDrücke Enter für erneute Eingabe")
    schulaufgaben_löschen()


  schulaufgaben_liste.remove(schulaufgaben_liste[int(lösch_zahl)-1])
  schulaufgaben_datum.remove(schulaufgaben_datum[int(lösch_zahl)-1])

  schulaufgaben_counter = 1
  print("\nDiese Schulaufgaben sind nun übrig:\n")
  for i in schulaufgaben_liste:
    print(schulaufgaben_counter, "-", i)
    schulaufgaben_counter += 1

  

  

  print("\n\n")
  print ("1 - Weitere Schulaufgabe löschen ")
  print ("2 - Zurück zum Menü\n")

  nochmal = input("Was möchtest du jetzt tun?\n")

  if nochmal == "1":
    schulaufgaben_löschen()
  elif nochmal == "2":
    menu()
  else:
    zurück = input("\nGib bitte eine gültige Zahl ein.\nDrücke Enter für erneute Eingabe")
    schulaufgaben_löschen()

  

def menu():
  clear = lambda: os.system("clear")
  clear()
  print (Fore.RED + "SchulBot\n\n")
  print (Fore.BLUE + "Menü\n")

  print ("1 - Schulaufgaben eintragen ")
  print ("2 - Schulaufgaben einsehen")
  print ("3 - Schulaufgaben löschen\n")
  auswahl = input("Was möchtest du tun?\n")

  if auswahl == "1":
    schulaufgabe_eintagen()

  elif auswahl == "2":
    schulaufgaben_einsehen()
  
  elif auswahl == "3":
    schulaufgaben_löschen()


  else:
      zurück = input("\nGib bitte eine gültige Zahl ein.\nDrücke Enter für erneute Eingabe")
      menu()



menu()


