'''
num = [1,5,3,9,7]
num[2]=5
num.append(2)
num.sort()
print(num)
num.sort(reverse=True)
num.insert(2,3) # insere na lista na posição
print(num)
num.pop(2) # exclui na lista na posição
print(num)
if 4 in num:    
    num.remove(4) # elimina valor
else:
    print('Não encontrei 4 na lista')
print(num)
print(f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'Os valores são {v}...')  
for c,v in enumerate(valores):
    print(f'Na {c+1}ª Posição encontrei o valor :{v}')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
print(f'Foram inserido os valore {valores}')

'''

a = [2,3,4,5]
b = a
b[2] = 8
print(f'Lista A: {a} cópia sem ligação ente A e B')
print(f'Lista A: {b} cópia sem ligação ente A e B')
a = [2,3,4,5]
b = a[:]
b[2] = 8
print(f'Lista A: {a} cópia com ligação ente A e B')
print(f'Lista A: {b}cópia com ligação ente A e B')
