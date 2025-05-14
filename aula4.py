###1- var de controle 2- condicao de parada 3- att da var de controle
# 1 var de controle
i = 20
# 2 cond. parada
while i < 50:
    if i % 2 == 0:
        print(f'i = {i}')
        # 3 att da var
    i = i + 1 # incremento
        
        
# criar um laco com while que dependa da resposta do user p continuar o laco
resp = "s"
while resp == "s" or resp == 'S':
    print('Ainda estou repetindo... ')
    while True:
        resp = input('Deseja continuar? (s) = sim / (n) = não')
        resp = resp.lower()
        if resp == 's' or resp== 'n':
            break
            #pass
    #resp = resp.lower()
print('terminei!!!!') 