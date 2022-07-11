# Aula de uso de Dicionarios em Python
print('-/-'*30)
print('Exemplo 001')
pessoas = {'nome': 'Rafael', 'sexo': 'M', 'idade': 37}
print(f'O {pessoas["nome"]} tem idade de {pessoas["idade"]} anos')
del pessoas ['sexo']
pessoas['nome'] = 'Taís'
pessoas['peso'] = 98.5
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('-/-'*30)
print('Exemplo 002')

Brasil = list()
estado1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = { 'UF': 'São Paulo', 'Sigla': 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(Brasil[0] ['UF'])
print(Brasil[1]['Sigla'])
print('-/-'*30)
print('Exemplo 003')
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade fedrativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
for e in brasil:
    for v in e.values():
        print(v, end= '  ')
        print()
print('-/-'*30)