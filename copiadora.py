print ('|' + '\u203E' * 39 + '|') #Print de boas-vindas
print ('|      Copiadora de Autoatendimento     |')
print ('|           Rodrigo Alcantara           |')
print ('|' + '_' * 39 + '|')

def escolha_servico(): #função para escolher serviço
    valores = {'DIG': 1.1, 'ICO': 1, 'IPB': 0.4, 'FOT':0.2}
    while True:
        servico = input('Esolha uma das opções de serviço oferecido:\n')
        if servico in valores: #verifica se a opção escolhida é válida
            print((f'O serviço solicitado é: R${valores[servico]:.2f} por página').replace('.',',') + ('.'))
            return valores[servico] #retorna o valor do serviço escolhido
        else:
            print(f'Opção inválida. Por favor, escolha uma das opções de serviço oferecido:\n')

def num_pag(): #função para escolher número de páginas
    while True:
        try:
            pag = int(input('Qual o número de páginas?\n'))
            if pag < 20:
                break
            elif pag < 200:
                pag = int(pag * 0.85)
                print(f'Para esse número de páginas o desconto será de 15%.')
                break
            elif pag < 2000:
                pag = int(pag * 0.8)
                print(f'Para esse número de páginas o desconto será de 20%.')
                break
            elif pag < 20000:
                pag = int(pag * 0.75)
                print(f'Para esse número de páginas o desconto será de 25%.')
                break
            else:
                print ('Não é possivel fazer tantas páginas por vez!\n Por favor, entre novamente com um novo número de páginas.') #se estiver errado volta
        except ValueError:
            print ('Isso não é um número válido, tente novamente') #se não for número volta
    return pag #retorna o número de páginas já com desconto quando tiver

def servico_extra(): #função para escolher serviço extra
    extras = {'0': 0, '1': 15, '2': 40}
    while True:
        ext = input(str('Deseja fazer algum dos serviços extras:\n'))
        if ext in extras: #verifica se a opção escolhida é válida
            print((f'O serviço extra escolhido custará: R${extras[ext]:.2f}').replace('.',',') + ('.'))
            return extras[ext] #retorna o valor do serviço extra
        else:
            print(f'Opção inválida. Por favor, escolha uma das opções de serviço extra oferecido:\n')


print ('|' + '\u203E' * 39 + '|')
print ('|          SERVIÇOS OFERECIDOS          |') #Print serviços
print ('|' + ' ' * 39 + '|')
print ('| DIG -> Digitalizar            (R$1,10)|')
print ('| ICO -> Impressão Colorida     (R$1,00)|')
print ('| IPB -> Impressão Preto/Branco (R$0,40)|')
print ('| FOT => Fotocópia              (R$0,20)|')
print ('|' + '_' * 39 + '|')

valor_servico = escolha_servico()


print ('|' + '\u203E' * 43 + '|')
print ('|Aproveite a promoção:                      |')
print ('|Quanto mais páginas maior o desconto.      |')
print ('|Limite máximo: 20000 páginas               |')
print ('|' + '_' * 43 + '|')

total_paginas = num_pag()


print ('|' + '\u203E' * 43 + '|')
print ('|              SERVIÇOS EXTRAS              |') #Print serviços extras
print ('|' + ' ' * 43 + '|')
print ('| 0 -> Não desejo serviços extras  (R$15,00)|')
print ('| 1 -> Encadernação Simples        (R$15,00)|')
print ('| 2 -> Encadernação Capa Dura      (R$40,00)|')
print ('|' + ' ' * 43 + '|')
print ('|' + '_' * 43 + '|')

valor_extra = servico_extra()


total = valor_servico * total_paginas + valor_extra

print((f'O total à pagar é: R${total:.2f}').replace('.',',') + ('.'))