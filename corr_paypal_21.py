import csv

with open("") as pagpay_csv:
    paypal_reader = csv.reader(pagpay_csv)

    with open("") as pay_csv:
        MSR_reader = csv.reader(pay_csv, delimiter=",")

#liste principali
        lordo = []
        dare = []
        avere =[]
        nomiMSR = []
        nomipl = []
        ogman = {"nome": [], "importo": []}
        ogman_def = {}
        dateMSR = []
        datepl = []
        descrizione = []
        numinc = []
#numeri che compaiono più volte in una lista
        numeri_doppi_paypal_2 = []
        numeri_doppi_paypal_3 = []
        numeri_doppi_paypal_4 = []
        numeri_doppi_paypal_5 = []
        numeri_doppi_MSR_2 = []
        numeri_doppi_MSR_3 = []
        numeri_doppi_MSR_4 = []
        numeri_doppi_MSR_5 = []
        importi_no_in_dare = []
        importi_no_in_lordo = []
        index_multipli_in_dare = []
        index_multipli_in_lordo = []
        index_mult_in_dare_corr_in_lordo = []
        index_mult_in_lordo_corr_in_dare = []
#punti di partenza per le sonmme
        lordo_tot = 0
        lordo_tot_mancante = 0
        dare_tot = 0
        dare_tot_mancante = 0
        importi_doppi_mancanti = 0

        next(MSR_reader)


#aggiunta delle voci principali alle rispettive liste: sezione lordo
        for line in MSR_reader:
            nomiMSR.append(line[3])
            dateMSR.append(line[0])
            descrizione.append(line[1])
            lordo.append(line[2])
#evitare errore quando la cifra è divisa da virgole
        for c in range(len(lordo)):
            try:
                lordo[c] = float(lordo[c])
            except:
                pass
#aggiunta delle voci principali alle rispettive liste: sezione dare
        for line in paypal_reader:
            dare.append(line[2])
            nomipl.append(line[1])
            datepl.append(line[0])
            avere.append(line[3])
#evitare errore quando la cifra è divisa da virgole
        for d in range(len(dare)):
            try:
                dare[d] = float(dare[d])
            except:
                pass

        for a in range(len(avere)):
            try:
                avere[a] = float(avere[a])
            except:
                pass
            
            
#confronto tra numeri lordo e numeri in dare per trovare i numeri che compaiono in lordo ma non in dare
        for i in range(len(lordo)):
            if (lordo[i] not in dare):
                ogman["nome"].append(nomiMSR[i])
                ogman["importo"].append(lordo[i])
                ogman_def["mancante in dare"] = nomiMSR[i], lordo[i] , dateMSR[i], descrizione[i]
                print("Manca in dare: " +
                    str(ogman_def["mancante in dare"]))
                
#confronto tra numeri dare e numeri in lordo per trovare i numeri che compaiono in dare ma non in lordo
        print("-"*50)
        
        for k in range(len(dare)):
            if dare[k] not in lordo:
                ogman["nome"].append(nomipl[k])
                ogman["importo"].append(dare[k])
                ogman_def["mancante in lordo"] = nomipl[k], dare[k] , datepl[k]
                print("Manca in lordo: " +
                    str(ogman_def["mancante in lordo"]))

#importi presenti in avere e in lordo ma non in dare
        print("-"*50)
        for j in range(len(avere)):
            if -avere[j] in lordo:
                ogman["nome"].append(nomipl[j])
                ogman["importo"].append(avere[j])
                ogman_def["presente in avere e lordo"] = nomipl[j], avere[j] , datepl[j]
                print("Presente in avere e in lordo: " +
                    str(ogman_def["presente in avere e lordo"]))
        print("-"*50)

#trovare e dividere i numeri che compaiono più volte all'interno delle liste lordo e dare
        for k in dare:
            if dare.count(k) > 1:
                numeri_doppi_paypal_2.append(k)
            if dare.count(k) > 2:
                numeri_doppi_paypal_3.append(k)
            if dare.count(k) > 3:
                numeri_doppi_paypal_4.append(k)
            if dare.count(k) > 4:
                numeri_doppi_paypal_5.append(k)
        
        for x in lordo:
            if lordo.count(x) > 1:
                numeri_doppi_MSR_2.append(x)
            if lordo.count(x) > 2:
                numeri_doppi_MSR_3.append(x)
            if lordo.count(x) > 3:
                numeri_doppi_MSR_4.append(x)
            if lordo.count(x) > 4:
                numeri_doppi_MSR_5.append(x)
#confronto per trovare i numeri che compaiono un numero differrente di volte tra le liste dare e avere
        #numeri che compaiono almeno 2 volte in unamlista e che compaiono meno di 1 volta nell'altra
        for a in range(len(numeri_doppi_paypal_2)):
            if numeri_doppi_paypal_2[a] not in numeri_doppi_MSR_2:
                importi_no_in_lordo.append(numeri_doppi_paypal_2[a])
                
        for b in range(len(numeri_doppi_MSR_2)):
            if numeri_doppi_MSR_2[b] not in numeri_doppi_paypal_2:
                importi_no_in_dare.append(numeri_doppi_MSR_2[b])
        #numeri che compaiono almeno 3 volte in unamlista e che compaiono meno di 2 nell'altra  
        for a in range(len(numeri_doppi_paypal_3)):
            if numeri_doppi_paypal_3[a] not in numeri_doppi_MSR_3:
                importi_no_in_lordo.append(numeri_doppi_paypal_3[a])
        
        for b in range(len(numeri_doppi_MSR_3)):
            if numeri_doppi_MSR_3[b] not in numeri_doppi_paypal_3:
                importi_no_in_dare.append(numeri_doppi_MSR_3[b])
        #numeri che compaiono almeno 4 volte in unamlista e che compaiono meno di 3 volte nell'altra        
        for a in range(len(numeri_doppi_paypal_4)):
            if numeri_doppi_paypal_4[a] not in numeri_doppi_MSR_4:
                importi_no_in_lordo.append(numeri_doppi_paypal_4[a])
                
        for b in range(len(numeri_doppi_MSR_4)):
            if numeri_doppi_MSR_4[b] not in numeri_doppi_paypal_4:
                importi_no_in_dare.append(numeri_doppi_MSR_4[b])
        #numeri che compaiono almeno 5 volte in unamlista e che compaiono meno di 4 volte nell'altra
        for a in range(len(numeri_doppi_paypal_5)):
            if numeri_doppi_paypal_5[a] not in numeri_doppi_MSR_5:
                importi_no_in_lordo.append(numeri_doppi_paypal_5[a])
                
        for b in range(len(numeri_doppi_MSR_5)):
            if numeri_doppi_MSR_5[b] not in numeri_doppi_paypal_5:
                importi_no_in_dare.append(numeri_doppi_MSR_5[b])

        importi_no_in_dare = list(set(importi_no_in_dare))
        print(importi_no_in_dare)
        importi_no_in_lordo = list(set(importi_no_in_lordo))
        print(importi_no_in_lordo)
        
        
#trova l'index dei vari duplicati dei valori presenti in importi_no_in_dare e ..._in_lordo
        def list_duplicates_of(seq, item):
            start_at = -1
            locs = []
            while True:
                try:
                    loc = seq.index(item, start_at+1)
                except ValueError:
                    break
                else:
                    locs.append(loc)
                    start_at = loc
            return locs
        
        for b in importi_no_in_dare:
            index_multipli_in_lordo = list_duplicates_of(lordo, b)
            index_mult_in_lordo_corr_in_dare = list_duplicates_of(dare, b)

        for a in importi_no_in_lordo:
            index_multipli_in_dare = list_duplicates_of(dare, a)
            index_mult_in_dare_corr_in_lordo = list_duplicates_of(lordo, a)


#trova i numeri corrispondenti a partire dagli index dei duplicati
        for el in index_multipli_in_lordo:
            print("Importi che compaiono più in lordo che in dare, corrispondenza in lordo: " + str(nomiMSR[el]) + " , " + str(lordo[el]) + " , " + str(dateMSR[el]) + ")")
        print("")
        for al in index_mult_in_lordo_corr_in_dare:
            print("Importi che compaiono più in lordo che in dare, corrispondenza in dare: " + str(nomipl[al]) + " , " + str(dare[al]) + " , " + str(datepl[al]) + ")")
        print("-"*50)
        for ad in index_multipli_in_dare:
            print("Importi che compaiono più in dare che in lordo, corrispondenza in lordo: " + str(nomipl[ad]) + " , " + str(dare[ad]) + " , " + str(datepl[ad]) + ")")
        print("")
        for ed in index_mult_in_dare_corr_in_lordo:
            print("Importi che compaiono più in dare che in lordo, corrispondenza in dare: " + str(nomiMSR[ed]) + " , " + str(lordo[ed]) + " , " + str(dateMSR[ed]) + ")")