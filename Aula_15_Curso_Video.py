s = n = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
print('A soma dos valores é:{}'.format(s))
print(f'A soma dos valores é: {s}')
