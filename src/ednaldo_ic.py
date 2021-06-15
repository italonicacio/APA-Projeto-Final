
#v2
from typing import Any

from math import sqrt
from math import floor

def euc(v1,v2):
    return floor(sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2))#distancia euclidiana

def read_instance(filePath):#ler instancia(apenas as de todos para todos)
    f=open(filePath,"r")

    for i in range(6):
        aux=f.readline().split()
        
        if aux[0]=="DIMENSION":
            n=int(aux[2])
        

    cord=[[None]*2 for i in range(n)]
    dist=[[None]*n for i in range(n)]
    for i in range(n):
        linha1=f.readline()
        a=linha1.split()
        cord[i][0]=int(a[1])
        cord[i][1]=int(a[2])

    f.close()    

    for i in range(n):
        for k in range(n):
            dist[i][k]=euc(cord[i],cord[k])
            
    return(n,dist)

def greedy(dimensao,dist): #vizinho mais proximo
    rota=[]
    low=1000;aux=0;guarda_indice=0;cidade_mais_prox = 0
    matrix_flags_vmp = [False] * dimensao

    for k in range(dimensao):
        aux = guarda_indice
        low = 1000
        rota.append(guarda_indice) #adicionando as cidades
        matrix_flags_vmp[guarda_indice] = True #colocando cidade com a flag true
        for i in range(dimensao):
            if (dist[aux][i] != 0 and dist[aux][i] < low and matrix_flags_vmp[i] == False): #cidade mais proxima
                low = dist[aux][i]
                guarda_indice = i
    return rota #retornando a rota final

def cheapest_insertion(dimensao,dist,rota):#iserção mais barata
    low = 1000;lower=1000;aresta=0; cidade_mais_prox = 0
    rota_imb = []
    matrix_flags_imb = [False] * dimensao

    rota_imb.append(rota[0]) #3 cidades iniciais para imb já usando a rota do vizinho mais proximo para não pegar cidades aleatorias
    rota_imb.append(rota[1])
    rota_imb.append(rota[2])
    matrix_flags_imb[rota[0]] = True
    matrix_flags_imb[rota[1]] = True
    matrix_flags_imb[rota[2]] = True

    for j in range(dimensao - 3):
        low = 1000#Qual a menor distancia de uma cidade entre as outras da rota
        for k in range(len(rota_imb)):#Aqui começa o passo 2: encontra a cidade mais proxima do ciclo
            for i in range(dimensao):
                if ((dist[rota_imb[k]][i] != 0) and (dist[rota_imb[k]][i] < low) and matrix_flags_imb[i] == False):
                    cidade_mais_prox = i
                    low = dist[rota_imb[k]][i]
        low=1000

        for z in range(len(rota_imb)):  #Passo 3: encontre uma aresta K que minimize dik + dkj - dij-> cidade i-> cidade K-> cidade J
            for t in range(len(rota_imb)):
                if z != t and (((dist[rota_imb[z]][cidade_mais_prox]) + (dist[rota_imb[t]][cidade_mais_prox])) - (dist[rota_imb[z]][rota_imb[t]]) <= low):#se z=t então vai e volta pra mesmca cidade oque não é oque queremos 
                    low = dist[cidade_mais_prox][rota_imb[z]] + dist[cidade_mais_prox][rota_imb[t]]-(dist[rota_imb[z]][rota_imb[t]])
                    if (t > z):
                        aresta = t
                    else:
                        aresta = z
        rota_imb.insert(aresta, cidade_mais_prox)
        matrix_flags_imb[cidade_mais_prox] = True
    return rota_imb


dimensao,dist=read_instance("distancia3.txt")
rota = greedy(dimensao,dist)
rota_imb = cheapest_insertion(dimensao,dist,rota) #iserção mais barata

print(rota)
print(rota_imb)


'''trocar imb var por vetor de flags se como com 3 iterações fico com n+3  transformar imb e vmp em funções'''
