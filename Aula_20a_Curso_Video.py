#Def Aprendendo rotinas comando def - Cria comando personalizados...

#ex 01
def lin():
    print('=-='*10)
lin()
print('       Curso Python')
lin()
#ex 02
def mensagem(msg):
    print('-=-'*15)
    print(msg)
    print('-=-'*15)
mensagem('          Sistema  de Alunos')
mensagem('         Curso de Pythom é TOP...')
mensagem('              Testando def')
#ex 03
def soma(a, b):
    print('-=-'*12)
    print(f'A soma A->{a} e B->{b}')
    s = a + b
    print(f'A soma A + B: {s}')
    print('-=-'*12)
soma(5 , 4)
soma(7 , 6)
soma(2 , 8)

#ex 04
def contador(* num):
    for valor in num:
        print(f' {valor}.', end='')
    print('Fim')
    
    tam = len(num)
    print(f'Recebi os valores {num} a são ao todo {tam} números')  

contador(2, 1, 7)
contador(3, 5)
contador(1,4 , 7, 9)

#ex 05
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [3, 5, 7, 8, 1, 2,]
dobra(valores)
print(valores)

#ex 06 desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')
soma(5,2)
soma(4, 7, 8)
