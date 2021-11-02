""""
LISTA FILM
"""
#commento

import pickle
import os
import random

IDfilm = 1
IDserie = 1
lista = []
dict = {}

filename = "list.txt"
program = True
menu = True
comando = 0

# SE ESISTE, IMPORTO LA LISTA PREESISTENTE, ALTRIMENTI LA CREO DOPO
print("Benvenuto nell'archivio film e serie TV, carico la lista...")
exist = os.path.isfile(filename)
if exist:
    with open(filename, 'rb') as textfileread:
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
    print("\nPrimo avvio, l'archivio è VUOTO")
    with open(filename, 'wb') as textfile:
        pickle.dump(lista, textfile)

#INIZIO PROGRAMMA
while program:
    menustampa = True
    menucerca = True
    menurimuovi = True

    #MENU PRINCIPALE
    while menu:
        print("\n1. Lista film\n" +
              "2. Lista serie TV\n" +
              "3. Esci")

        comandomenu = input("Seleziona un'azione:\n")

        try:
            comandomenu = int(comandomenu)
        except:
            comandomenu = -1
        if comandomenu < 0:
            print("Inserisci un valore corretto!\n")
            continue
        elif comandomenu > 0 and comandomenu < 4:
            wait = True
        else:
            print("Inserisci un valore corretto!\n")


        #MENU FILM
        if comandomenu == 1:
            flag = "film"
            while wait:
                print("\n1. Aggiungi un film alla lista\n" +
                        "2. Visualizza la lista\n" +
                        "3. Cerca nella lista\n" +
                        "4. Rimuovi elementi dalla lista\n" +
                        "5. Estrai un titolo casuale\n" +
                        "6. Torna al menu principale")

                comando = input("Seleziona un'azione:\n")
                try:
                    comando = int(comando)
                except:
                    comando = -1
                if comando < 0:
                    print("Inserisci un valore corretto!\n")
                    continue
                elif comando > 0 and comando < 7:
                    wait = False
                    menu = False
                    comandomenu == 0
                else:
                    print("Inserisci un valore corretto!\n")

        #MENU SERIE TV
        elif comandomenu == 2:
            flag = "serietv"
            while wait:
                print("\n1. Aggiungi una serie TV alla lista\n" +
                        "2. Visualizza la lista\n" +
                        "3. Cerca nella lista\n" +
                        "4. Rimuovi elementi dalla lista\n" +
                        "5. Estrai un titolo casuale\n" +
                        "6. Torna al menu\n")

                comando = input("Seleziona un'azione:\n")
                try:
                    comando = int(comando)
                except:
                    comando = -1
                if comando < 0:
                    print("Inserisci un valore corretto!\n")
                    continue
                elif comando > 0 and comando < 7:
                    wait = False
                    menu = False
                    comandomenu == 0

        elif comandomenu == 3:
            program = False
            print("Uscita...")
            break

    #INSERIMENTO TITOLI
    while comando == 1:
        titolo = input("\nInserisci il titolo (digita X per uscire):\n")
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
            print("\n1. Stampa tutti i titoli\n" + "2. Torna al menu principale" )
            comandostampa = input("Seleziona un'azione:\n")

            try:
                comandostampa = int(comandostampa)
            except:
                comandostampa = -1

            if comandostampa < 0:
                print("Inserisci un valore corretto!")
                continue
            elif comandostampa > 0 and comandostampa < 3:
                menustampa = False
                continue
            else:
                print("Inserisci un valore corretto!\n")

        #STAMPA LISTA
        if comandostampa == 1:
            menustampa = True
            if flag == "film":
                for i in lista:
                    if flag in i['tipo']:
                        print("\n" + str(i["IDfilm"]) + '. ' + str(i['titolo']) + ': ' + str(i['piattaforma']))
                    else:
                        continue
            elif flag == "serietv":
                for i in lista:
                    if flag in i['tipo']:
                        print("\n" + str(i["IDserie"]) + '. ' + str(i['titolo']) + ': ' + str(i['piattaforma']))
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
            print("\n1. Cerca per titolo\n" + "2. Cerca per piattaforma\n" + "3. Torna al menu principale\n")
            comandocerca = input("Seleziona un'azione:\n")
            try:
                comandocerca = int(comandocerca)
            except:
                comandocerca = -1
            if comandocerca < 0:
                print("Inserisci un valore corretto!\n")
                continue
            elif comandocerca > 0 and comandocerca < 4:
                menucerca = False
                continue
            else:
                print("Inserisci un valore corretto!\n")

        # CERCA PER TITOLO
        if comandocerca == 1:
            trovato = False
            menucerca = True

            ricerca = input("Digita il titolo\n")
            ricerca = str(ricerca)
            ricerca = ricerca.casefold()  # rimuovo la dipendenza dal case sensitive
            print("I risultati per " + "'" + str(ricerca) + "'" + " sono i seguenti:\n")

            for y in lista:
                titolotemp = str(y["titolo"])
                titolotemp = titolotemp.casefold()
                if ricerca in titolotemp and flag in str(y['tipo']):
                    trovato = True
                    print("\t" + str(y["titolo"]) + ": " + str(y["piattaforma"]))
            if trovato == False:
                print("Nessun risultato.\n")
            else:
                continue

        if comandocerca == 2:
            trovato = False
            menucerca = True

            ricerca = input("Digita il nome della piattaforma\n")
            ricerca = str(ricerca)
            ricerca = ricerca.casefold() #rimuovo la dipendenza dal case sensitive

            print("I titoli disponibili su " + "'" + str(ricerca) + "'" + " sono i seguenti:\n")

            for y in lista:

                piattatemp = str(y["piattaforma"])
                piattatemp = piattatemp.casefold()

                if ricerca in piattatemp and flag in str(y['tipo']):
                    trovato = True
                    print("\t" + str(y["titolo"]))
            if trovato == False:
                print("Nessun risultato.\n")
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

        IDtempfilm = 1
        IDtempserie = 1
        contatore = 1

        for i in lista:

            # AGGIORNO DI NUOVO ID DEI TITOLI
            # QUANDO CANCELLO UN TITOLO NEL MEZZO DELLA LISTA HO BISOGNO DI RISCALARE TUTTI I TITOLI SUCCESSIVI DI UNA POSIZIONE IN ALTO!
            if flag == 'film' and flag in i['tipo']:
                if i['IDfilm'] != IDtempfilm:
                    i['IDfilm'] = IDtempfilm
                    IDtempfilm += 1
                else:
                    IDtempfilm += 1
            elif flag == 'serietv' and flag in i['tipo']:
                if i['IDserie'] != IDtempserie:
                    i['IDserie'] = IDtempserie
                    IDtempserie += 1
                else:
                    IDtempserie += 1
            if flag in i['tipo']:
                print(str(contatore) + '. ' + str(i['titolo']))
                contatore += 1


        comandorimuovi = input("Digita il numero del titolo da rimuovere\n")

        #RIMOZIONE
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
                IDtempfilm = 1
                IDtempserie = 1
                #AGGIORNO DI NUOVO ID DEI TITOLI
                #QUANDO CANCELLO UN TITOLO NEL MEZZO DELLA LISTA HO BISOGNO DI RISCALARE TUTTI I TITOLI SUCCESSIVI DI UNA POSIZIONE IN ALTO!
                for i in lista:
                    if flag in i['tipo']:
                        if i['IDfilm'] != IDtempfilm:
                            i['IDfilm'] = IDtempfilm
                            IDtempfilm += 1
                        else:
                            IDtempfilm += 1
                    elif flag in i['tipo']:
                        if i['IDserie'] != IDtempserie:
                            i['IDserie'] = IDtempserie
                            IDtempserie += 1
                        else:
                            IDtempserie += 1
                comando = 0
                nuovaeliminazione = False


                with open(filename, 'wb') as textfile:  # salvo ed esco
                    pickle.dump(lista, textfile)
                menu = True
            else:
                print("Inserisci un valore corretto!")

    #MENU TITOLO CASUALE
    if comando == 5:
        if not lista:
            with open(filename, 'rb') as textfile:
                lista = pickle.load(textfile)

        randlist = []
        contatore = 1

        if flag == "film":
            for i in lista:
                if flag in i['tipo']:
                    randlist.append(i['IDfilm'])
        if flag == "serietv":
            for i in lista:
                if flag in i['tipo']:
                    randlist.append(str(i['IDserie']))

        elemento = random.choice(randlist)
        elemento = str(elemento)

        if flag == "film":
            for i in lista:
                if flag in i['tipo'] and elemento in str(i['IDfilm']):
                    print("\t"+ str(i['titolo']) + ": " + str(i['piattaforma']))


        elif flag == "serietv":
            for i in lista:
                if flag in i['tipo'] and elemento in str(i['IDserie']):
                    print("\t"+ str(i['titolo']) + ": " + str(i['piattaforma']))


        unaltro = input("Estrarre un nuovo elemento? (Y/N)\n")
        if unaltro == 'y' or unaltro == 'Y':
            continue

        elif unaltro == 'n' or unaltro == 'N':
            menu = True
            comando = 0
            comandomenu = 1


    if comando == 6:
        menu = True
        continue

