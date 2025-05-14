
import random

# ...
# Lista/TUPLAS / DIC.

# LISTA -> COLEÇÕES HETEROGENEAS DE OBJETOS, PODEM SER QUALQUER TIPO, INCLUSIVE OUTRAS LISTAS {0,1,10,"BETO", (0.2, 0.3)} LISTAS SÃO MUTAVEIS. 
#LISTA-01 = {1,2,3,4,5,6}
#

# ...

LISTA = [1,2,3,4,5,6]
print(LISTA)
nome="beto"
#len -> que retorna tamnaho de uma coleção
print(len(nome))
#Vetor??? existe??? VECTOR -> COLECAO -> vetor [][][]
progs = ['Yes', 'Genesis', 'Pink floyd', 'Elp']

progs [3] = 'metalica'

# print(progs[0])
# print(progs[1])
# print(progs[2])
# print(progs[3])
#1 forma
for i in range(len(progs)):
    print(progs[i])

#2 forma
for prog in progs:
    print(prog)

# incluir novo elemento
progs.append('Guns')

# trocar ultimo elemento
progs[-1] = 'Novo elemento na ultima posição'

# ordenar ascendente/ descendente
progs.sort()

# inverter a lista
progs.reverse()

# pesquisa, FUNÇÃO ENUMERATE() RETORNA UMA TUPLA DE DOIS ELEMENTOS A CADA INTERAÇÃO:
# pop
# remove

for i, p in enumerate(progs):
    print(f'Posicao {i} e elemento = {p}')
#zip, o que é, como usar, restrições, casos de uso, I POSIÇÃO INDICE, P ELEMENTO

#DADA AS SEGUINTES LISTAS [A,B,C] E [D,E,F] COMO PODERIAMOS JUNTAR?
lista1 = ['A', 'B' ,'C']
lista2 = ['D', 'E' ,'F']
lista1.append(lista2)
print(lista1)
# listaA += listaB
# PENSANDO EM LISTAS DE 500 ALUNOS, ONDE SERAO LIDAS (RANDOM) 16 NOTAS M(0-100) OSTRE:
''' 
    A % DE ALUNOS APROVADOS
    A % DE ALUNOS REPROVADOS

    IMPRIMA OS 5 PRIMEIROS ALUNOS COM A MEDIA MAIS ALTA
    IMPRIMA OS 5 PIORES ALUNOS
    IMPRIMA A NOTA MAIS ALTA, A POSIÇÃO E QUAL ALUNO PERTENCE.

'''
alunos = ['y']
for i in range(1, 51):
    # for y in range (1, 200):

        print(i)


x = random.randint(0,100)
