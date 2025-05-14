# Script com todos os exercícios resolvidos da Lista 01-2
import math

def exercicio_a():
    numero = float(input("a) Digite um número: "))
    print("Maior que 10." if numero > 10 else "Não é maior que 10.")

def exercicio_b():
    numero = float(input("b) Digite um número: "))
    print("Está no intervalo de 100 a 1000." if 100 <= numero <= 1000 else "Fora do intervalo.")

def exercicio_c():
    numero = float(input("c) Digite um número: "))
    if 0 <= numero <= 20:
        print("Intervalo A")
    elif -5 <= numero <= -1:
        print("Intervalo B")
    elif 21 <= numero <= 60:
        print("Intervalo C")
    elif -100 <= numero <= 15:
        print("Intervalo D")
    else:
        print("Fora dos intervalos.")

def exercicio_d():
    raio = float(input("d) Digite o raio: "))
    if raio > 0:
        print(f"Área: {math.pi * raio ** 2:.2f}")
    else:
        print("Raio inválido.")

def exercicio_e():
    nome = input("e) Nome: ")
    funcoes = int(input("Funções criadas: "))
    valor = float(input("Valor por função: "))
    if funcoes > 0 and valor > 0:
        bruto = funcoes * valor
        liquido = bruto * 0.92
        print(f"{nome} | Bruto: R${bruto:.2f} | Líquido: R${liquido:.2f}")
    else:
        print("Valores inválidos.")

def exercicio_f():
    a = float(input("f) A: "))
    b = float(input("B: "))
    if a > 0 and b > 0:
        aux = a
        a = b
        b = aux
        print(f"A: {a}, B: {b}")
    else:
        print("Inválido.")

def exercicio_g():
    notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
    media = sum(notas) / 4
    print("Aprovado" if media >= 6 else "Reprovado")

def exercicio_h():
    a, b, c = [float(input(f"Número {i+1}: ")) for i in range(3)]
    print("Maior:", max(a, b, c))

def exercicio_i():
    n = int(input("i) Número: "))
    print("Par" if n % 2 == 0 else "Ímpar")

def exercicio_j():
    sexo = input("j) Sexo (M/F): ").upper()
    h = float(input("Altura (m): "))
    if sexo == 'M':
        print(f"Peso ideal: {(72.7 * h) - 58:.2f}kg")
    elif sexo == 'F':
        print(f"Peso ideal: {(62.1 * h) - 44.7:.2f}kg")
    else:
        print("Sexo inválido")

def exercicio_k():
    a = float(input("k) A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    delta = b**2 - 4*a*c
    if a == 0:
        print("Não é equação do 2º grau")
    elif delta < 0:
        print("Sem raízes reais")
    elif delta == 0:
        print(f"Raiz: {-b / (2*a):.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Raízes: {x1:.2f}, {x2:.2f}")

def exercicio_l():
    soma = sum([int(input(f"Número {i+1}: ")) for i in range(4) if int(input()) % 2 == 0])
    print(f"Soma dos pares: {soma}")

def exercicio_m():
    impares = [int(input(f"Número {i+1}: ")) for i in range(5)]
    impares = [x for x in impares if x % 2 != 0]
    if impares:
        print(f"Média dos ímpares: {sum(impares)/len(impares):.2f}")
    else:
        print("Sem ímpares")

def exercicio_n():
    valores = sorted([float(input(f"Valor {i+1}: ")) for i in range(3)])
    print("Ordem crescente:", valores)

def exercicio_o():
    a = float(input("Lado A: "))
    b = float(input("Lado B: "))
    c = float(input("Lado C: "))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            tipo = "Equilátero"
        elif a == b or b == c or a == c:
            tipo = "Isósceles"
        else:
            tipo = "Escaleno"
        print(f"Triângulo {tipo}")
    else:
        print("Não é triângulo")

def exercicio_p():
    lados = sorted([float(input(f"Lado {i+1}: ")) for i in range(3)])
    a, b, c = lados
    if a + b > c:
        if c**2 == a**2 + b**2:
            print("Retângulo")
        elif c**2 < a**2 + b**2:
            print("Acutângulo")
        else:
            print("Obtusângulo")
    else:
        print("Não é triângulo")

def exercicio_q():
    z = float(input("z: "))
    w = float(input("w: "))
    y = (z + w) / 2  # exemplo
    print(f"y = {y}")

def exercicio_r():
    saldo = float(input("Saldo médio: "))
    if saldo <= 200:
        credito = 0
    elif saldo <= 400:
        credito = saldo * 0.2
    elif saldo <= 600:
        credito = saldo * 0.3
    else:
        credito = saldo * 0.4
    print(f"Crédito: R${credito:.2f}")

# Menu interativo
funcoes = [
    exercicio_a, exercicio_b, exercicio_c, exercicio_d, exercicio_e,
    exercicio_f, exercicio_g, exercicio_h, exercicio_i, exercicio_j,
    exercicio_k, exercicio_l, exercicio_m, exercicio_n, exercicio_o,
    exercicio_p, exercicio_q, exercicio_r
]

while True:
    print("\nLista de Exercícios - Escolha uma opção:")
    for i, f in enumerate(funcoes):
        print(f"{chr(97 + i)}) Exercício {chr(97 + i)}")
    print("s) Sair")

    opcao = input("Opção: ").lower()
    if opcao == 's':
        break
    indice = ord(opcao) - 97
    if 0 <= indice < len(funcoes):
        funcoes[indice]()
    else:
        print("Opção inválida.")
