# -*- coding: utf-8 -*-

import numpy as np

parcacikSayisi = 10
degiskenSayısı = 4

min_c, max_c = 2,3
min_w, max_w = 1,2
maxiter = 1000

def uyumf(arr):
    uyum = []
    for j in range(0,parcacikSayisi):
        dizi = arr[j,:]
        if sum(dizi*[20,18,22,16])>= 200:
            if sum(dizi*[50,40,40,60])>= 800:
                if sum(dizi*[20,15,20,25])>= 250:
                    if sum(dizi*[100,90,116,100])>= 70:
                        if sum(dizi*[18,16,15,20])>= 24:
                            if sum(dizi*[1000,800,850,900])>= 1500:
                               uyum2 = 0
                               for i in range(0,degiskenSayısı):
                                   if dizi[i] >= 0:
                                       uyum2 = uyum2 + 1
                                   if uyum2 == degiskenSayısı:
                                       uyum.append(1)
        else:
            uyum.append(0)
    if sum(uyum) == parcacikSayisi:
        uyum = 1
    else:
        uyum = 0
    return uyum

def amac_fonk(arr):
    amac = []
    for i in range(0,len(arr)):
        amac.append(sum(arr[i,:]*[55,94,50,55]))
    return amac

liste = np.random.uniform(low=0, high=25.0, size=[parcacikSayisi,degiskenSayısı])  
uyumf(liste)

while uyumf(liste) == 0:
    liste = np.random.uniform(low=0, high=100.0, size=[parcacikSayisi,degiskenSayısı])    
    liste = np.asarray(liste, dtype=np.float32)

amac_deger = amac_fonk(liste)

a = amac_deger.index(max(amac_deger))
gbest_amac = max(amac_deger)

gbest = []
for i in range(parcacikSayisi):
    gbest.append(np.array(liste[a]).T.tolist())

pbest = liste
pbest_amac= amac_deger

velocity = np.random.uniform(low=-1.0, high=1.0, size=[parcacikSayisi,degiskenSayısı])

c1 = np.random.uniform(low=min_c, high=max_c, size=[1,1])
c2 = np.random.uniform(low=min_c, high=max_c, size=[1,1])
w = np.random.uniform(low=min_w, high=max_w, size=[1,1])
rand1 = np.random.uniform(low=0, high=1.0, size=[1,1])
rand2 = np.random.uniform(low=0, high=1.0, size=[1,1])

bulentv = w*velocity + c1*rand1*(pbest-liste) + c2*rand2*(gbest-liste)
bulent = liste+bulentv

for i in range(0,maxiter):
    if uyumf(bulent) == 1 :
        amac_deger2 = amac_fonk(bulent)
        if gbest_amac < max(amac_deger2):
            gbest_amac = max(amac_deger2)
            a = amac_deger2.index(max(amac_deger2))
            gbest = []
            for i in range(parcacikSayisi):
                gbest.append(np.array(bulent[a]).T.tolist())
        for i in range(0,parcacikSayisi):
            if pbest_amac[i] < amac_deger2[i]:
                pbest_amac[i] = amac_deger2[i]
                pbest[i] = bulent[i]
        
        c1 = (max_c-min_c)*i/maxiter + c1
        c2 = (max_c-min_c)*i/maxiter + c2
        w = (max_w-min_w)*(maxiter-i)/maxiter + min_w
        rand1 = np.random.uniform(low=0, high=1.0, size=[1,1])
        rand2 = np.random.uniform(low=0, high=1.0, size=[1,1])
        bulentv = w*bulentv + c1*rand1*(pbest-bulent) + c2*rand2*(gbest-bulent)
        bulent = bulent+bulentv
    else :
        maxiter = maxiter + 1

print("Gbest : " + str(gbest[1]))
print("Gbest amac : " + str(gbest_amac))

