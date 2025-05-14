# n=int(input("Número: "))
# for i in range (0,n+1):
#     n2= n-i
#     print(n2)

# cont1=0
# cont2=0
# num=0
# for x in range(7):
#     num=int(input("digite um número inteiro: "))
#     if num < 0: print("Alarme ativdado! Sala imediatamente!"); break
#     if num % 3 !=0:
#         cont1 +=1
#     else:
#         cont2 +=1
# if cont2 >=4 and num > 0:
#     print( "Cofre aberto com sucesso!")
# elif cont2 >=3:
#     print("Tentativa falhou. O cofre permanece fechado.")


# passos = int(input("Qts passos o austronauta deu?  "))

# pedras = 0
# buracos = 0

# for i in range(1, passos+1):

#     obs= input(f"Passo {i}: Pedra (P) ou Buraco (B)?").upper()
#     if obs == "P":
#         pedras += 1
#     elif obs == 'B':
#         buracos +=1
#     else:
#         print('Entrada inválida: {pedras}')
# print("Arroz")

# print("\nBatata") 

# eq=0
# ins=0
# for i in range(8):
    
#     n=int(input("Digite um n? "))
    
#     if (n % 2 == 0 and n % 5 ==0) or (n != 0 and n % 3 ==0):
#         print()

# energia_total = 0
# contador_numero = 0

# while energia_total > 100:
#     num = int(input('Digite um num(positivo ou negativo)'))
#     contador_numero += 1
    
#     if num >= 0:
#         energia_total +=num
#         print(f"Energia aumentada em {num}. Total {energia_total}")
#     else:
#         energia_total +=num
#         print(f"Energia aumentada em {abs(num)}. Total {energia_total}")

# print("Balança estab.!")
# print('f.Total = {energia_total}')

# v=0
# t=0

# while v < 5:
#     n=int(input('Digite:??  '))
#     t +=1
#     if n < 2 or n % 2 == 0 and n !=2:
#         print('Rejeitado')

#     div = 2
#     eh_primo = True
    
#     while div * div < n:
#         if n % div==0:
#             eh_primo = False
#             break
#         div += 1

#     if eh_primo and n % 2 !=0:
#         print('validos')
#         v+=1
#     else:
#         print('rejeitados')
