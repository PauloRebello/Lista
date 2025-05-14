s=("1/1+2/3+3/5+4/7+n/2*n−1")
n=int(input('Digite um n: '))
s=0
for i in range (1,n+1):
    s+=i/(2*i-1)
print(f"O valor {n} é {s}")


n1=int(input('Digite um número: '))
for a in range (1,n1):
    n1 +=a
print(n1)