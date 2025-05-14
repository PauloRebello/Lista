'''
ler dois números onde o 1 vai ser o inicio do laçp e o 2 o fim.
validar os numeros entrada

2- 
    *
   **
  ***
 ****
*****
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5

- ler um mes e um ano qualquer, exibir o calendario completo com os dias da semana

* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

'''
# 

num1 = int(input("Digite o inicio: "))
num2 = int(input("Digite o fim: "))

if num1 > num2 :
    aux = num1
    num1 = num2
    num2 = aux

for i in range (num1, num2, 1):
    print(i)
    #ls -la ls -a rm -f .git git status
    
if num1 > num2 :
    for i in range (num2, num1):
        print(i)
else:
    for i in range (num1, num2):
        print(i)
        
        
        
n = 1
n2 = 2 
n3 = 3
for i in range (n, n2, n3):
    print(i)
