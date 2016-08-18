# -*- coding: utf-8 -*-
# @author: Juho-Petteri Lesonen

import os
from random import randrange

##### Funktiot ######

def check_lista():
    if os.path.exists("temput_lista.txt") == False:
        print("Temppuja ei löytynyt. Lisää temppuja ennen kuin jatkat.")
    else:
        print("Temppulista löydetty.")
    return

def add_temppu():
    f = open('temput_lista.txt', 'r')

    for line in f.readlines():
        
        line=line.strip().split()
        temput.append(str(line[0]))
        lajit.append(int(line[1]))
        ajat.append(int(line[2]))
        vaikeudet.append(int(line[3]))
        
    f.close()
    
    temppu1 = raw_input("Nimi: ")
    laji1 = raw_input("Laji: ")
    aika1 = raw_input("Aika: ")
    vaikeus1 = raw_input("Vaikeus :")    
    
    temput.append(temppu1)
    lajit.append(laji1)
    ajat.append(aika1)
    vaikeudet.append(vaikeus1)
    
    f = open('temput_lista.txt', 'wb')
    for i in range(0,len(lajit)):
        a = temput[i] 
        b = lajit[i]
        c = ajat[i]
        d = vaikeudet[i]
        
        f.write("%s %s %s %s\n" % (a,b,c,d))
        
    f.close()
    print(temput)
    return temput,lajit,ajat,vaikeudet
    
def mod_temppu():
    mod = raw_input("Muutettava temppu: ")
    mod=str(mod)
    testi = mod in temput
    if testi == False:
        print("Ei löydy")
    else:
        i = temput.index(mod)
        temput[i] = raw_input("Nimi: ")
        lajit[i] = raw_input("Laji: ")
        ajat[i] = raw_input("Aika: ")
        vaikeudet[i] = raw_input("Vaikeus: ")
        
        f = open('temput_lista.txt', 'wb')
        
        for k in range(0,len(lajit)):
            a = temput[k] 
            b = lajit[k]
            c = ajat[k]
            d = vaikeudet[k]
        
            f.write("%s %s %s %s\n" % (a,b,c,d))
        
        f.close()
    print(temput)    
    return temput, lajit, ajat, vaikeudet
    
    
def dele_temppu():
    dele = raw_input("Poistettava temppu: ")
    dele=str(dele)
    testi = dele in temput
    if testi == False:
        print("Ei löydy")
    else:
        i = temput.index(dele)
        temput.remove(temput[i])
        lajit.remove(lajit[i])
        ajat.remove(ajat[i])
        vaikeudet.remove(vaikeudet[i])
        
        f = open('temput_lista.txt', 'wb')
        
        for k in range(0,len(lajit)):
            a = temput[k] 
            b = lajit[k]
            c = ajat[k]
            d = vaikeudet[k]
        
            f.write("%s %s %s %s\n" % (a,b,c,d))
        
        f.close()
    print(temput)
    return


def make_list():
    kerrat = raw_input("Kuinka monta: ")
    kerrat = int(kerrat)
    
    toko_pro = raw_input("Toko määrä: ")
    toko = int(toko_pro)
    
    koti_pro = raw_input("Koti määrä: ")
    koti = int(koti_pro)
    
    agil_pro = raw_input("Agility määrä: ")
    agil = int(agil_pro)    
    
    if (toko + koti + agil) != 100.:
        print("Ei käy.")
        
    else:
        toko_m = int((toko / 100.) * kerrat)
        koti_m = int((koti / 100.) * kerrat)
        agil_m = int((agil / 100.) * kerrat)
        
        f = open('temput_lista.txt', 'r')

        for line in f.readlines():
        
            line=line.strip().split()
            temput.append(str(line[0]))
            lajit.append(int(line[1]))
            ajat.append(int(line[2]))
            vaikeudet.append(int(line[3]))
        
        f.close()
        
        lista=[]
        toko_test=0
        koti_test=0
        agil_test=0
        n = 0
        while n != kerrat:
            
            h = [j for j,val in enumerate(ajat) if val==5]
            l = randrange(0,len(h))
            jj=h[l]
            test_num = lajit[jj]
            if test_num == 1:
                if toko_test < toko_m:
                    if vaikeudet[jj] == 7:
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        toko_test += 4
                    elif vaikeudet[jj] == 6:
                        lista.append(temput[jj])
                        toko_test += 1
                    else:
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        toko_test += 2
            elif test_num == 2:
                if koti_test < koti_m:
                    if vaikeudet[jj] == 7:
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        koti_test += 4
                    elif vaikeudet[jj] == 6:
                        lista.append(temput[jj])
                        koti_test += 1
                    else:
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        koti_test += 2

            else:
                if agil_test < agil_m:
                    if vaikeudet[jj] == 7:
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        agil_test += 4
                    elif vaikeudet[jj] == 6:
                        lista.append(temput[jj])
                        agil_test += 1
                    else:
                        lista.append(temput[jj])
                        lista.append(temput[jj])
                        agil_test += 2
            
            h = [j for j,val in enumerate(ajat) if val==4]
            l = randrange(0,len(h))
            jj=h[l]
            test_num = lajit[jj]
            
            
            if test_num == 1:
                if toko_test < toko_m:
                    if vaikeudet[jj] == 7:
                        lista.append(temput[jj])
                        toko_test += 1
                    elif vaikeudet[jj] == 6:
                        lista.append(temput[jj])
                        toko_test += 1
                    else:
                        lista.append(temput[jj])
                        toko_test += 1
            
            
            elif test_num == 2:
                if koti_test < koti_m:
                    if vaikeudet[jj] == 7:
                        lista.append(temput[jj])
                        koti_test += 1
                    elif vaikeudet[jj] == 6:
                        lista.append(temput[jj])
                        koti_test += 1
                    else:
                        lista.append(temput[jj])
                        koti_test += 1

            
            else:
                if agil_test < agil_m:
                    if vaikeudet[jj] == 7:
                        lista.append(temput[jj])
                        agil_test += 1
                    elif vaikeudet[jj] == 6:
                        lista.append(temput[jj])
                        agil_test += 1
                    else:
                        lista.append(temput[jj])
                        agil_test += 1

            
            
            n = len(lista)
            
        f = open('sarja.txt', 'wb')
        for k in range(0,len(lista)):
            a = lista[k] 
        
            f.write("%s\n" % a)
        
        f.close()
        #print(lista)


    return lista
        

##### Pääohjelma #####

temput=[]
lajit=[]
ajat=[]
vaikeudet=[]

#check_lista()
#add_temppu()
#mod_temppu()
#dele_temppu()
make_list()








































