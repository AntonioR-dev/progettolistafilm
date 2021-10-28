""""
LISTA FILM
"""


import pickle
import os

IDfilm = 1
IDserie = 1
lista = []
dict = {}

filename = "list.list"
program = True
menu = True
comando = 0

# SE ESISTE, IMPORTO LA LISTA PREESISTENTE, ALTRIMENTI LA CREO DOPO
exist = os.path.isfile(filename)
if exist:
    with open("list.list", 'rb') as textfileread:
        lista = pickle.load(textfileread)

        # RECUPERO IL VALORE DELL'ULTIMO ID DELLA LISTA CARICATA E LO INCREMENTO DI 1
        for i in lista:
            IDfilm = i["IDfilm"]
            IDserie= i["IDserie"]
        IDfilm = int(IDfilm)
        IDfilm += 1
        IDfilm = int(IDfilm)
        IDfilm += 1
else:
    print("Primo avvio, l'archivio è VUOTO\n")
    with open(filename, 'wb') as textfile:
        pickle.dump(lista, textfile)



#INIZIO PROGRAMMA
print("Benvenuto nell'archivio film e serie TV, carico la lista...\n")

while program:
    menustampa = True
    menucerca = True
    menurimuovi = True

    #MENU PRINCIPALE
    while menu:
        print("1. Lista film\n" +
              "2. Lista serie TV\n" +
              "3. Esci")

        comandomenu = input("Seleziona un'azione:\n")
        if comandomenu != "1" and comandomenu != "2" and comandomenu != "3":
            print("Inserisci un valore corretto!\n")
            continue
        else:
            comandomenu = int(comandomenu)
            wait = True


        #MENU FILM
        if comandomenu == 1:
            flag = "film"
            while wait:
                print("1. Aggiungi un film alla lista\n" +
                    "2. Visualizza la lista\n" +
                        "3. Cerca nella lista\n" +
                        "4. Rimuovi elementi dalla lista\n" +
                        "5 Torna al menu\n")

                comando = input("Seleziona un'azione:\n")
                if comando != "1" and comando != "2" and comando != "3" and comando != "4" and comando != "5":
                    print("Inserisci un valore corretto!\n")
                    continue
                else:
                    comando = int(comando)
                    wait = False
                    menu = False
                    comandomenu == 0

        #MENU SERIE TV
        elif comandomenu == 2:
            flag = "serietv"
            while wait:
                print("1. Aggiungi una serie TV alla lista\n" +
                    "2. Visualizza la lista\n" +
                        "3. Cerca nella lista\n" +
                        "4. Rimuovi elementi dalla lista\n" +
                        "5 Torna al menu\n")

                comando = input("Seleziona un'azione:\n")
                if comando != "1" and comando != "2" and comando != "3" and comando != "4" and comando != "5":
                    print("Inserisci un valore corretto!\n")
                    continue
                else:
                    comando = int(comando)
                    wait = False
                    menu = False
                    comandomenu == 0

        elif comandomenu == 3:
            program = False
            print("Uscita...")
            break

    #INSERIMENTO TITOLI
    while comando == 1:
        titolo = input("Inserisci il titolo (digita X per uscire):\n")
        if titolo == "X" or titolo == "x":
            with open(filename, 'wb') as textfile: #salvo ed esco
                pickle.dump(lista, textfile)
            comando = 0
            menu = True
            continue

        piattaforma = input("Digita la/e piattaforma/e su cui è possibile guardare il titolo:\n")

        if flag == "film":
            archivio = {'titolo': titolo, 'piattaforma': piattaforma, 'IDfilm': IDfilm, 'IDserie': 0, 'tipo': flag}
            IDfilm += 1
        elif flag == "serietv":
            archivio = {'titolo': titolo, 'piattaforma': piattaforma, 'IDfilm': 0, 'IDserie': IDserie, 'tipo': flag}
            IDserie += 1
        lista.append(archivio)

    #MENU STAMPA LISTA
    if comando == 2:
        with open(filename, 'rb') as textfile:
          lista = pickle.load(textfile)
        while menustampa:
            print("1. Stampa tutti i titoli\n" + "2. Torna al menu principale\n" )
            comandostampa = input("Seleziona un'azione:\n")
            if comandostampa != "1" and comandostampa != "2" and comandostampa != "3":
                print("Inserisci un valore corretto!\n")
                continue
            else:
                comandostampa = int(comandostampa)
                menustampa = False
                continue

        #STAMPA LISTA
        if comandostampa == 1:
            menustampa = True
            if flag == "film":
                for i in lista:
                    if flag in i['tipo']:
                        print(str(i["IDfilm"]) + '. ' + str(i['titolo']) + ' Piattaforma/e: ' + str(i['piattaforma']))
                    else:
                        continue
            elif flag == "serietv":
                for i in lista:
                    if flag in i['tipo']:
                        print(str(i["IDserie"]) + '. ' + str(i['titolo']) + ' Piattaforma/e: ' + str(i['piattaforma']))
                    else:
                        continue
            print("\n")

        if comandostampa == 2:
            menustampa = False
            menu = True
            continue

    #MENU RICERCA
    if comando == 3:
        with open(filename, 'rb') as textfile:
          lista = pickle.load(textfile)

        while menucerca:
            print("1. Cerca per titolo\n" + "2. Cerca per piattaforma\n" + "3. Torna al menu principale\n")
            comandocerca = input("Seleziona un'azione:\n")
            if comandocerca != "1" and comandocerca != "2" and comandocerca != "3":
                print("Inserisci un valore corretto!\n")
                continue
            else:
                comandocerca = int(comandocerca)
                menucerca = False
                continue

        # CERCA PER TITOLO
        if comandocerca == 1:
            trovato = False
            menucerca = True
            ricerca = input("Digita il titolo\n")
            ricerca = str(ricerca)
            ricerca = ricerca.casefold()  # rimuovo la dipendenza dal case sensitive
            print("I risultati per" + "'" + str(ricerca) + "'" + "sono i seguenti:\n")

            for y in lista:
                titolotemp = str(y["titolo"])
                titolotemp = titolotemp.casefold()
                if ricerca in titolotemp:
                    trovato = True
                    print("\t" + str(y["titolo"]) + ": " + str(y["piattaforma"]))
            if trovato == False:
                print("Nessun risultato.\n")
            else:
                print("\n")

        if comandocerca == 2:
            trovato = False
            menucerca = True
            ricerca = input("Digita il nome della piattaforma\n")
            ricerca = str(ricerca)
            ricerca = ricerca.casefold() #rimuovo la dipendenza dal case sensitive
            print("I titoli disponibili su " + "'" + str(ricerca) + "'" + " sono i seguenti:\n")

            for y in lista:
                if flag in y["tipo"]:  #distinguo i film dalle serie
                    piattatemp = str(y["piattaforma"])
                    piattatemp = piattatemp.casefold()
                    if ricerca in piattatemp:
                        trovato = True
                        print("\t" + str(y["titolo"]))
                    if trovato == False:
                        print("Nessun risultato.\n")
                    else:
                        print("\n")
                else:
                    continue

        if comandocerca == 3:
            menucerca = False
            menu = True
            continue

    #MENU RIMUOVI
    while comando == 4:
        nuovaeliminazione = True
        with open(filename, 'rb') as textfile:
          lista = pickle.load(textfile)

        contatore = 1
        for i in lista:

            if flag in i['tipo']:
                print(str(contatore) + '. ' + str(i['titolo']))
                contatore += 1

        comandorimuovi = input("Digita il numero del titolo da rimuovere\n")

        for y in lista:
            if flag in y['tipo']:
                if comandorimuovi in str(y['IDfilm']):
                    lista.remove(y)
            elif flag in y['tipo']:
                if comandorimuovi in str(y['IDserie']):
                    lista.remove(y)

        while nuovaeliminazione:
            conferma = input("Desideri rimuovere un altro elemento? (Y/N)\n")
            conferma = conferma.casefold()
            if conferma == 'y':
                nuovaeliminazione = False
                break
            elif conferma == 'n':
                comando = 0
                nuovaeliminazione = False
                with open(filename, 'wb') as textfile:  # salvo ed esco
                    pickle.dump(lista, textfile)
                menu = True
            else:
                print("Inserisci un valore corretto!")
