import pandas as pd
import os
lordo_df = pd.read_csv("", sep=";")
DA_df = pd.read_csv("", sep=";")

print(lordo_df.head(2))
print("----------")
print(DA_df.head(2))

print(lordo_df.columns)
print(DA_df.columns)

#missing values
Lordo_df = lordo_df.fillna(0)
DA_df = DA_df.fillna(0)


#evitare errore quando la cifra è divisa da virgole
for c in range(len(lordo_df["Lordo "])):
    try:
        lordo_df["Lordo "][c] = float(lordo_df["Lordo "][c])
    except:
        pass

#evitare errore quando la cifra è divisa da virgole
for d in range(len(DA_df["Dare in valuta"])):
    try:
        DA_df["Dare in valuta"][d] = float(DA_df["Dare in valuta"][d])
    except:
        pass

for a in range(len(DA_df["Avere in valuta"])):
    try:
        DA_df["Avere in valuta"][a] = float(DA_df["Avere in valuta"][a])
    except:
        pass

DA_df["Tot valuta"] = DA_df["Dare in valuta"] - DA_df["Avere in valuta"]

valori_diversi_lordo = []
for j in lordo_df["Lordo "]:
    if list(lordo_df["Lordo "]).count(j) != list(DA_df["Tot valuta"]).count(j):
        valori_diversi_lordo.append(j)

lordo_filtered = lordo_df[lordo_df["Lordo "].isin(valori_diversi_lordo)]
lordo_filtered = lordo_filtered[["Data", "Descrizione", "Lordo ", "Indirizzo email mittente", "Nome", "Codice transazione di riferimento"]]
print(lordo_filtered)

print("="*20)

valori_diversi_DA = []

for s in DA_df["Tot valuta"]:
    if list(DA_df["Tot valuta"]).count(s) != list(lordo_df["Lordo "]).count(s):
        valori_diversi_DA.append(s)

DA_df_filtered = DA_df[DA_df["Tot valuta"].isin(valori_diversi_DA)]
DA_df_filtered = DA_df_filtered[["Data registrazione", "Causale contabile", "Dare in valuta", "Avere in valuta", "Tot valuta"]]
print(DA_df_filtered)


DA_df_filtered.to_excel("corr_mancanti/coor_DA_05.xlsx")
lordo_filtered.to_excel("corr_mancanti/corr_Lordo_05.xlsx")

#alternativa
"""
#confronto tra numeri lordo e numeri in dare per trovare i numeri che compaiono in lordo ma non in dare
print("="*10)
lordo= []

for i in range(len(lordo_df["Lordo "])):
    if not lordo_df["Lordo "][i] in list(DA_df["Tot valuta"]):
        lordo.append(lordo_df["Lordo "][i])
        #print("Manca in DA " + str(lordo_df["Lordo "][i]))
        
print(lordo_df[lordo_df["Lordo "].isin(lordo)])

print("="*10)
        
#confronto tra numeri dare e numeri in lordo per trovare i numeri che compaiono in dare ma non in lordo
tot_valuta = []
for k in range(len(DA_df["Tot valuta"])):
    if not DA_df["Tot valuta"][k] in list(lordo_df["Lordo "]):
        tot_valuta.append(DA_df["Tot valuta"][k])

print(DA_df[DA_df["Tot valuta"].isin(tot_valuta)])

print("="*10)

print(lordo_df["Lordo "].value_counts())
print(DA_df["Tot valuta"].value_counts())
"""