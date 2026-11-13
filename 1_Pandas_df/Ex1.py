#Scrivi un programma che analizzi le valutazioni di alcuni prodotti utilizzando una Pandas Series.
# Il programma deve:
#1.  Creare una Series con le valutazioni di almeno 6 prodotti,
# usando il nome del prodotto come indice. Inserire almeno due valori mancanti (None).
#2.  Individuare e stampare i prodotti privi di valutazione con i metodi di Pandas.
#3.  Calcolare valutazione media, massima e minima, ignorando i dati mancanti.
#4.  Sostituire i dati mancanti con la media, senza modificare la Series originale.
#6.  Stampare i risultati in modo leggibile.
import pandas as pd
valutazioni = pd.Series([1,2, None,None,4,5], index=['Telefono','Tv','Pc','Cuffie','Mouse', 'VR'])
#2.  Individuare e stampare i prodotti privi di valutazione con i metodi di Pandas.
mask = valutazioni.isna()
print(valutazioni[mask])
print("\n ################################################## \n")
#3.  Calcolare valutazione media, massima e minima, ignorando i dati mancanti.
print('il massimo è :', valutazioni.max())
print('il minimo è :', valutazioni.min())
print('la media è :', valutazioni.mean())
print("\n ################################################## \n")

#4.  Sostituire i dati mancanti con la media, senza modificare la Series originale.
copy_valutazioni = valutazioni.copy()
copy_valutazioni = copy_valutazioni.fillna(copy_valutazioni.mean())
print('il df con il fill è :', copy_valutazioni)

df =pd.DataFrame( copy_valutazioni)


