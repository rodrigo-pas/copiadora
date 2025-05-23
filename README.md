# 🖨️ Copiadora de Autoatendimento – Sistema de Impressões (Python)
Este programa simula o sistema de uma **Copiadora de Autoatendimento**, onde o cliente escolhe o tipo de serviço (digitalização, impressão colorida ou PB, fotocópia), informa o número de páginas e pode ainda adicionar um serviço extra de encadernação. O sistema calcula automaticamente o valor total com aplicação de descontos progressivos.

## 💻 Tecnologias utilizadas
- Linguagem Python
- Terminal/Console

## ⚙️ Funcionalidades
- Exibição de menu com serviços e preços
- Escolha entre os serviços:
  - Digitalizar (DIG)
  - Impressão Colorida (ICO)
  - Impressão PB (IPB)
  - Fotocópia (FOT)
- Descontos progressivos:
  - 15% para até 199 páginas
  - 20% para até 1999 páginas
  - 25% para até 19999 páginas
- Limite máximo de 20.000 páginas
- Serviços extras disponíveis:
  - Encadernação simples
  - Encadernação capa dura
- Validação de entradas para garantir dados corretos
- Cálculo automático do valor total da compra

## ▶️ Como executar
1. Copie o código para um arquivo `.py`, por exemplo `copiadora.py`.
2. Execute com Python 3 em seu terminal:

```bash
python copiadora.py
```

## 🧾Exemplo de execução
```bash
Esolha uma das opções de serviço oferecido:
ICO
O serviço solicitado é: R$1,00 por página

Qual o número de páginas?
250
Para esse número de páginas o desconto será de 20%.

Deseja fazer algum dos serviços extras:
2
O serviço extra escolhido custará: R$40,00

O total à pagar é: R$240,00.
```

## Projeto desenvolvido por Rodrigo Alcantara 🎓