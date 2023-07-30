print('')
print('Bem-Vindo a Sorveteria do Luccas Duarte Mendanha')
print('')
# Cardápio separado pelo Nº de bolas e sabor, todos com seu proprio valor de acordo com o Nº de bolas.
print('-------------------------------------Cardápio--------------------------------------')
print('| Nº DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|      1      |         R$6,00         |         R$7,00     |         R$8,00      |')
print('|      2      |         R$10,00        |         R$12,00    |         R$14,00     |')
print('|      3      |         R$14,00        |         R$17,00    |         R$20,00     |')
print('-----------------------------------------------------------------------------------')

#Dicionario com o nome dos sabores
nomes_sabores = {
    'tr': 'Tradicional',
    'pr': 'Premium',
    'es': 'Especial',
                }

# Variável que irá armazenar o valor total do pedido do cliente.
valortotal = 0

# Loop principal do programa para a escolha dos sabores e quantidade de bolas.
while True:

    
    soma = 0 # Variável para armazenar o valor do sorvete escolhido em cada iteração.
    print('')
    sabor = (input('Escolha qual sera o sabor (tr / pr / es): '))

    # Verifica se o sabor escolhido está presente no cardápio, caso contrário, pede nova escolha.
    if sabor != 'tr' and sabor != 'pr' and sabor != 'es':
        print('Sabor de sorvete inválido. Tente novamente')
        print('')
        continue
    
    try:
           
        qntdebolas = int(input('Escola o número de bolas de sorvete desejado (1 / 2 / 3): '))
    except ValueError:
        print('Número de bolas de Sorvete inválida. Tente novamente')
        print('')
        continue

    # Verifica se a número de bolas escolhida está presente no cardápio, caso contrário, ira voltar a escolha do sabor.
    if qntdebolas < 1 or qntdebolas > 3:
        print('Número de bolas de Sorvete Inválido. Tente novamente')
        print('')
        continue
    # Calcula o valor do sorvete com base na quantidade de bolas e no sabor escolhido.
    if qntdebolas == 1:
        if sabor == 'tr':
            soma =6
        elif sabor == 'pr':
            soma = 7
        else:
            sabor == 'es'
            soma = 8
            
    if qntdebolas == 2:
        if sabor == 'tr':
            soma = 10
        elif sabor == 'pr':
            soma = 12
        else:
            sabor == 'es'
            soma = 14
            
    if qntdebolas == 3:
        if sabor == 'tr':
           soma = 14
        elif sabor == 'pr':
            soma = 17
        else:
            sabor == 'es'
            soma = 20
   
    valor = soma # Valor do sorvete escolhido no momento.
    valortotal += valor # Adiciona o valor do sorvete ao valor total do pedido.

    # Exibe o pedido do cliente e o valor a pagar
    print('Você pediu {} bola(s) de sorvete no sabor {}: R$ {:.2f}'.format(qntdebolas, nomes_sabores[sabor], valor))

    # Pergunta ao cliente se deseja pedir mais algum sorvete ou finalizar o pedido.
    escolha = input('Deseja mais algum sorvete? ( Digite sim ou nao): ')
    
    if escolha == 'sim':
        continue # Caso o cliente queira mais sorvetes, o loop continua para nova escolha.
    else:
        # Caso o cliente não queira mais sorvetes, o valor total é exibido e o loop é encerrado.
        print('')
        print('O valor total a ser pago: R$ {:.2f}'.format(valortotal))
        print('')
        break
        
        