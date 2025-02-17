import csv
import json

# Exercício 1
def soma_lista(numeros):
    return sum(numeros)
numeros = [1,2,3,4,5]
print(soma_lista(numeros))

# Exercício 2
def remover_duplicatas(lista):
    lista_sem_duplicatas = []
    return [x for x in lista if not (x in lista_sem_duplicatas or lista_sem_duplicatas.append(x))]
lista_repetida =  ["Matheus", 1, 2, 3, 1, "Matheus"]
print(remover_duplicatas(lista_repetida))

# Exercício 3
def ordenar_por_idade(lista):
    return sorted(lista,key=lambda x: x[1])
lista_tuplas = [("Matheus", 25), ("Amanda", 33), ("Nicolas", 1)]
print(ordenar_por_idade(lista_tuplas))

#Exercício 4
def contar_palavras(texto:str):
    palavras = texto.split()
    dic = {}
    for palavra in palavras:
        dic[palavra.lower()] = dic.get(palavra.lower(),0) + 1
    return dic
texto = "Três pratos de trigo para três tigres tristes"
print(contar_palavras(texto))

# Exercício 5
def inverter_dicionario(dicionario):
    return {v: k for k, v in dicionario.items()}
dicionario = {25: "idade", "Matheus": "nome"}
print(inverter_dicionario(dicionario))

# Exercício 6
def unir_dicionarios(dic1:dict, dic2):
    dic = dic1.copy()
    for k, v in dic2.items():
        dic[k] = dic.get(k, 0) + v
    return dic
dic1 = {1:2, 3:4, 5:6, 7:8}
dic2 = {9:10, 3:4, 1:2, 11:12}
print(unir_dicionarios(dic1, dic2))

# Exercício 7
def conjuntos(conj1, conj2):

    return {
        "união": conj1 | conj2,
        "interseção": conj1 & conj2,
        "diferença": (conj1 - conj2) | (conj2 - conj1)
    }
conj1 = {1, 2, 3, 4, 5, "Matheus"}
conj2 = {"Matheus", 1, 10, 40}
print(conjuntos(conj1, conj2))

# Exercicio 8
def elementos_unicos(lista):
    return list(set(lista))
lista = [1,5,2,"Matheus", 3,4,5,3,5,5,10,11, "Matheus"]
print(elementos_unicos(lista))