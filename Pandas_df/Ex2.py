
#Scrivi un programma che gestisca un piccolo magazzino utilizzando un Pandas DataFrame. Il programma deve:
#1.  Creare un DataFrame di almeno 8 prodotti con colonne nome, categoria, prezzo,
# quantita, citta. Usare almeno 3 categorie e 3 città.
#2.  Aggiungere la colonna valore_magazzino, calcolata come prezzo × quantita.
#3.  Selezionare i soli prodotti di categoria “informatica” con prezzo > 100 €.
#4.  Ordinare i prodotti per valore_magazzino decrescente.
#7.  Stampare risultati e riepilogo in modo leggibile.

import pandas as pd

# Creazione del DataFrame
dati = {
    "nome": [
        "Laptop", "Mouse", "Tastiera", "Scrivania",
        "Sedia", "Quaderno", "Penna", "Monitor",
        "Lampada", "Zaino"
    ],
    "categoria": [
        "Informatica", "Informatica", "Informatica",
        "Arredamento", "Arredamento", "Cancelleria",
        "Cancelleria", "Informatica", "Arredamento",
        "Accessori"
    ],
    "prezzo": [
        850, 25, 45, 200, 120,
        5, 2, 180, 35, 50
    ],
    "quantita": [
        5, 20, 15, 8, 10,
        50, 100, 7, 12, 18
    ],
    "citta": [
        "Torino", "Milano", "Roma", "Torino",
        "Milano", "Roma", "Torino", "Milano",
        "Roma", "Napoli"
    ]
}

df = pd.DataFrame(dati)

#2.  Aggiungere la colonna valore_magazzino, calcolata come prezzo × quantita.
df['Valore_magazzino']= df['quantita'] * df['prezzo']
print('\n ########################################### \n')
print(df)
print('\n ########################################### \n')
#3.  Selezionare i soli prodotti di categoria “informatica” con prezzo > 100 €.
mask = ((df['categoria'] == 'Informatica') & (df['prezzo'] >100))
df_mask = df[mask]
print(df_mask)
print('\n ########################################### \n')
#4.  Ordinare i prodotti per valore_magazzino decrescente.
ordinati = df.sort_values(by=['Valore_magazzino'], ascending=False)
print(ordinati)









