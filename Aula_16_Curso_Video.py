#Tuplas ()
#tuplas são imútaveis

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(sorted(lanche)) # sorted coloca em ordem
for comida in lanche:
    print(f'Eu vou comer: {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer: {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi para caramba!!!')


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print('Quantos números tem o total da tupla =',len(c))
print('Quantos números 8 há na tupla =',c.count(8))
print('Em que posição',c.index(2),'está o número = 2')


pessoa = ('Rafael', 37, 'Masculino', 90)
print(pessoa)
