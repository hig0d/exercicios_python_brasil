"""13. Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês
elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."""

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

temperaturas = []

for i in range(12):
    temperaturas.append(int(input(f'Digite a temperatura de {meses[i]}: ')))

media = sum(temperaturas) / 12

for i in range(12):
    if temperaturas[i] > media:
        print(f'{temperaturas[i], meses[i]}')