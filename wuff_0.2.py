#-*- coding: utf-8 -*-
# @author: Juho-Petteri Lesonen

import os
import math
import random

##### Funktiot ######

def check_lista():
    if os.path.exists("temput_lista.txt") == False:
        print("Temppuja ei löytynyt. Lisää temppuja ennen kuin jatkat.")
        print("")
    else:
        print("Temppulista löydetty.")
        print("")
    return
        
    
def add_temppu():
    f = open('temput_lista.txt', 'r')

    for line in f.readlines():
        
        line=line.strip().split()
        temput0.append(str(line[0]))
        lajit0.append(str(line[1]))
        ajat0.append(str(line[2]))
        vaikeudet0.append(str(line[3]))
        
    f.close()
    
    temppu1 = raw_input("Nimi: ")
    laji1 = raw_input("Laji: ")
    aika1 = raw_input("Aika: ")
    vaikeus1 = raw_input("Vaikeus :")    
    
    temput0.append(temppu1)
    lajit0.append(laji1)
    ajat0.append(aika1)
    vaikeudet0.append(vaikeus1)
    
    f = open('temput_lista.txt', 'wb')
    for i in range(0,len(lajit0)):
        a = temput0[i] 
        b = lajit0[i]
        c = ajat0[i]
        d = vaikeudet0[i]
        
        f.write("%s %s %s %s\n" % (a,b,c,d))
        
    f.close()
    return

   
def mod_temppu():
    
    f = open('temput_lista.txt', 'r')

    for line in f.readlines():
        
        line=line.strip().split()
        temput0.append(str(line[0]))
        lajit0.append(str(line[1]))
        ajat0.append(str(line[2]))
        vaikeudet0.append(str(line[3]))
        
    f.close()    
    
    print(temput0)
        
    mod = raw_input("Muutettava temppu: ")
    mod=str(mod)
    
    testi = mod in temput0
    
    if testi == False:
        print("Ei löydy. Tarkista oikeinkirjoitus.")
    else:
        i = temput0.index(mod)
        temput0[i] = raw_input("Nimi: ")
        lajit0[i] = raw_input("Laji: ")
        ajat0[i] = raw_input("Aika: ")
        vaikeudet0[i] = raw_input("Vaikeus: ")
        
        f = open('temput_lista.txt', 'w')
        
        for k in range(0,len(lajit0)):
            print(k)
            a = temput0[k] 
            b = lajit0[k]
            c = ajat0[k]
            d = vaikeudet0[k]
        
            f.write("%s %s %s %s\n" % (a,b,c,d))
        
        f.close()

    return
    
    
def dele_temppu():

    f = open('temput_lista.txt', 'r')

    for line in f.readlines():
        
        line=line.strip().split()
        temput0.append(str(line[0]))
        lajit0.append(str(line[1]))
        ajat0.append(str(line[2]))
        vaikeudet0.append(str(line[3]))
        
    f.close()    
    
    for i in range(0,len(lajit0)):
        print(temput0[i])    
    
    dele = raw_input("Poistettava temppu: ")
    dele=str(dele)
    testi = dele in temput0
    if testi == False:
        print("Ei löydy. Tarkista oikeinkirjoitus")
    else:
        i = temput0.index(dele)
        temput0.remove(temput0[i])
        lajit0.remove(lajit0[i])
        ajat0.remove(ajat0[i])
        vaikeudet0.remove(vaikeudet0[i])
        
        f = open('temput_lista.txt', 'wb')
        
        for k in range(0,len(lajit0)):
            a = temput0[k] 
            b = lajit0[k]
            c = ajat0[k]
            d = vaikeudet0[k]
        
            f.write("%s %s %s %s\n" % (a,b,c,d))
        
        f.close()
    return

 
def make_list():
    
    
    f = open('temput_lista.txt', 'r')

    for line in f.readlines():
        
        line=line.strip().split()
        temput0.append(str(line[0]))
        lajit0.append(str(line[1]))
        ajat0.append(str(line[2]))
        vaikeudet0.append(str(line[3]))
        
    f.close()
    
    len_toko = lajit0.count("toko")
    len_koti = lajit0.count("koti")
    len_agil = lajit0.count("agility")
    len_rally = lajit0.count("rallytoko")
    len_temput = lajit0.count("temput")
    len_nayttelyt = lajit0.count("nayttelyt")
       
    
    toko_pro = raw_input("Toko määrä prosenteissa: ")
    toko = int(toko_pro)
    
    koti_pro = raw_input("Koti määrä prosenteissa: ")
    koti = int(koti_pro)
    
    agil_pro = raw_input("Agility määrä: ")
    agil = int(agil_pro)    
    
    rallytoko_pro = raw_input("Rallytoko määrä: ")
    rallytoko = int(rallytoko_pro)    
    
    temput_pro = raw_input("Temput määrä: ")
    temput = int(temput_pro)    
    
    nayttelyt_pro = raw_input("Näyttelyt määrä: ")
    nayttelyt = int(nayttelyt_pro)   

    if toko + koti + agil + rallytoko + temput + nayttelyt != 100:
        print("Ei käy.")
    else:
        
        if toko == 0: 
            toko_n = 0
        else:
            toko_n = int(len_toko/(toko*0.01))
        
        if koti == 0:
            koti_n = 0
        else:
            koti_n = int(len_koti/(koti*0.01))
        
        if agil == 0:
            agil_n = 0
        else:
            agil_n = int(len_agil/(koti*0.01))
            
        if rallytoko == 0:
            rally_n = 0
        else:
            rally_n = int(len_rally/(agil*0.01))
        
        if temput == 0:
            temput_n = 0
        else:
            temput_n = int(len_temput/(rallytoko*0.01))
            
        if nayttelyt == 0:
            nayttelyt_n = 0
        else:
            nayttelyt_n = int(len_nayttelyt/(nayttelyt*0.01))
        
    
    #print(toko_n,koti_n,agil_n,rally_n,temput_n,nayttelyt_n)
    
    lajilista = [toko_n,koti_n,agil_n,rally_n,temput_n,nayttelyt_n]
    lajilista2 = [len_toko,len_koti,len_agil,len_rally,len_temput,len_nayttelyt]
    lajilista3 = [toko,koti,agil,rallytoko,temput,nayttelyt]
    
    maximum1 = max(lajilista)
    place1 = lajilista.index(maximum1)
    maximum2 = lajilista2[place1]
    
    #print(maximum1,maximum2)
    
    total_num = int(maximum2/(lajilista3[place1]*0.01))
    
    #print(total_num)
    
    total_toko = int(math.ceil(total_num * (lajilista3[0]*0.01)))
    total_koti = int(math.ceil(total_num * (lajilista3[1]*0.01)))
    total_agil = int(math.ceil(total_num * (lajilista3[2]*0.01)))
    total_rally = int(math.ceil(total_num * (lajilista3[3]*0.01)))
    total_temput = int(math.ceil(total_num * (lajilista3[4]*0.01)))
    total_nayttelyt = int(math.ceil(total_num * (lajilista3[5]*0.01)))
    
    
    if total_toko == 0:
        print("Ei tokoloilua tanaan...")
        print("")
    else:
        temppu_toko_indeksi = [i for i, x in enumerate(lajit0) if x == "toko"]
        
        temppulista_toko1 = [temput0[i] for i in temppu_toko_indeksi]
        aikalista_toko1 = [ajat0[i] for i in temppu_toko_indeksi]
        vaikeuslista_toko1 =[vaikeudet0[i] for i in temppu_toko_indeksi]
        
        multiple = total_toko / len_toko
        multiple2 = total_toko % len_toko
        
        rand_index1 = [int(len(temppulista_toko1)*random.random()) for i in xrange(multiple*len(temppulista_toko1))]
        rand_index2 = [int(len(temppulista_toko1)*random.random()) for i in xrange(multiple2)]                
        print(rand_index1)
        
        temppulista_toko2 = [temppulista_toko1[i] for i in rand_index1]
        aikalista_toko2 = [aikalista_toko1[i] for i in rand_index1]
        vaikeuslista_toko2 = [vaikeuslista_toko1[i] for i in rand_index1]
        
        temppulista_toko3_add = [temppulista_toko1[i] for i in rand_index2]
        aikalista_toko3_add = [aikalista_toko1[i] for i in rand_index2]
        vaikeuslista_toko3_add = [vaikeuslista_toko1[i] for i in rand_index2]
        print(temppulista_toko3_add)
        print(aikalista_toko3_add)
        print(vaikeuslista_toko3_add)


        
        temppulista_toko_add = random.sample(temppulista_toko1, multiple2)
        temppulista_toko2 = (multiple * temppulista_toko1) + temppulista_toko_add
        temppulista_toko_f = random.sample(temppulista_toko2,len(temppulista_toko2))
        
        print(temppulista_toko_f)
        print("")
        
    
    if total_koti == 0:
        print("Ei kotoilua tanaan...")
        print("")
    else:
        temppu_koti_indeksi = [i for i, x in enumerate(lajit0) if x == "koti"]
        temppulista_koti1 = [temput0[i] for i in temppu_koti_indeksi]

        multiple = total_koti / len_koti
        multiple2 = total_koti % len_koti
        
        temppulista_koti_add = random.sample(temppulista_koti1, multiple2)
        temppulista_koti2 = (multiple * temppulista_koti1) + temppulista_koti_add
        temppulista_koti_f = random.sample(temppulista_koti2,len(temppulista_koti2))
        print(temppulista_koti_f)
        print("")
    
    
    if total_agil == 0:
        print("Ei agiliteilya tänaan...")
        print("")
    else:
        temppu_agil_indeksi = [i for i, x in enumerate(lajit0) if x == "agility"]
        temppulista_agil1 = [temput0[i] for i in temppu_agil_indeksi]

        multiple = total_agil / len_agil
        multiple2 = total_agil % len_agil
        
        temppulista_agil_add = random.sample(temppulista_agil1, multiple2)
        temppulista_agil2 = (multiple * temppulista_agil1) + temppulista_agil_add
        temppulista_agil_f = random.sample(temppulista_agil2,len(temppulista_agil2))
        print(temppulista_agil_f)
        print("")
        
        
    if total_rally == 0:
        print("Ei rallitokoilua tanaan...")
        print("")
    else:
        temppu_rally_indeksi = [i for i, x in enumerate(lajit0) if x == "rallytoko"]
        temppulista_rally1 = [temput0[i] for i in temppu_rally_indeksi]

        multiple = total_rally / len_rally
        multiple2 = total_rally % len_rally
        
        temppulista_rally_add = random.sample(temppulista_rally1, multiple2)
        temppulista_rally2 = (multiple * temppulista_rally1) + temppulista_rally_add
        temppulista_rally_f = random.sample(temppulista_rally2,len(temppulista_rally2))
        print(temppulista_rally_f)
        print("")        
        
   
    if total_temput == 0:
        print("Ei temppuilua tanaan...")
        print("")
    else:
        temppu_temput_indeksi = [i for i, x in enumerate(lajit0) if x == "temput"]
        temppulista_temput1 = [temput0[i] for i in temppu_temput_indeksi]

        multiple = total_temput / len_temput
        multiple2 = total_temput % len_temput
        
        temppulista_temput_add = random.sample(temppulista_temput1, multiple2)
        temppulista_temput2 = (multiple * temppulista_temput1) + temppulista_temput_add
        temppulista_temput_f = random.sample(temppulista_temput2,len(temppulista_temput2))
        print(temppulista_temput_f)
        print("")        
        
        
    if total_nayttelyt == 0:
        print("Ei nayttelyita tanaan...")
        print("")
    else:
        temppu_nayttelyt_indeksi = [i for i, x in enumerate(lajit0) if x == "nayttelyt"]
        temppulista_nayttelyt1 = [temput0[i] for i in temppu_nayttelyt_indeksi]

        multiple = total_nayttelyt / len_nayttelyt
        multiple2 = total_nayttelyt % len_nayttelyt
        
        temppulista_nayttelyt_add = random.sample(temppulista_nayttelyt1, multiple2)
        temppulista_nayttelyt2 = (multiple * temppulista_nayttelyt1) + temppulista_nayttelyt_add
        temppulista_nayttelyt_f = random.sample(temppulista_nayttelyt2,len(temppulista_nayttelyt2))
        print(temppulista_nayttelyt_f)
        print("")        
    
    return

    

##### Pääohjelma #####
if __name__ == "__main__":
    
    temput0=[]
    lajit0=[]
    ajat0=[]
    vaikeudet0=[]
    lista0=[]

    #check_lista()
    #add_temppu()
    #mod_temppu()
    #dele_temppu()

    make_list()







