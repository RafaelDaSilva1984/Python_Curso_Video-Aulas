'''
teste = list()
teste.append('Rafael')
teste.append(37)
galera = list()
galera.append(teste[:])
teste[0] = 'Taís'
teste[1] = 35
galera.append(teste[:])
print(galera)   


galera = [['João', 19],['Pedro', 22],['Antonio', 33],['Adamastor', 44]]
print(galera[0][0])
print(galera[1][0])


galera = [['João', 19],['Pedro', 22],['Antonio', 33],['Adamastor', 44]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

'''
totmaior = totmenor = tot = 0
galera = list()
dados = list()
for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:]) # [:] cópia de dados
    dados.clear()
for p in galera:
    if p[1] >= 21:
        totmaior += 1
        print(f'{p[0]} é maior de idade {p[1]} anos')
    else:
        totmenor += 1
        print(f'{p[0]} é menor de idade {p[1]} anos')
    tot += 1
print(f'Maior de idade são {totmaior} pessoas e são {totmenor} pessoas em um total de {tot}')
print(galera)