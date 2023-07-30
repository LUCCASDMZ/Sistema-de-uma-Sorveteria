# Variáveis para armazenar os valores parciais do peso, pelo e adicionais
valorpelo = 0
valoradicional = 0
valorpeso = 0

# Função para obter o peso do cachorro
def cachorro_peso():
    print('------------------------------ Menu 1 de 3 - Peso Cachorro------------------------------')

    while True:
        try:
            print('')
            peso = int(input('Digite o peso do cachorro: '))
            
            # Verifica se o peso do cachorro é maior ou igual a 50
            if peso >= 50:
                print('Peso acima do permitido, não aceitamos cachorros tão grandes')
                print('Por favor digite o peso do cachorro novamente.')
                print('')
                continue
            
            # Calcula o valor baseado no peso
            if peso < 3:
                valor = 40
            elif peso >= 3 and peso < 10:
                valor = 50
            elif peso >= 10 and peso < 30:
                valor= 60
            else:
                peso >= 30 and peso < 50
                valor = 70
            
            global valorpeso 
            valorpeso += valor
            return peso
            
        # Tratamento de exceção caso o usuário digite um valor não numérico
        except ValueError:
            print('Voce digitou um valor não numérico')
            print('Por favor digite o peso do cachorro novamente.')
            continue

# Função para obter o tamanho do pelo do cachorro
def cachorro_pelo():
    print('-------------------- Menu 2 de 3 - Tamanho pelo do pelo do Cachorro --------------------')
    while True:
        print('')
        print('Qual o tamanho do pelo do cachorro')
        print('c - Pelo Curto')
        print('m - Pelo Medio')
        print('l - Pelo Longo')
        tamanhoPelo =   input('>>')
        
        # Verifica se o tamanho do pelo é válido (c, m, l)
        if tamanhoPelo != 'c' and tamanhoPelo != 'm' and tamanhoPelo != 'l':
                print('Tamanho de pelo invalido!')
                
        else:
            

            if tamanhoPelo == 'c':
                    valor =  1
            elif tamanhoPelo == 'm':
                    valor =  1.5
            else:
                    tamanhoPelo == 'l'
                    valor =  2

            global valorpelo
            valorpelo += valor
            return valorpelo

# Função para selecionar os serviços adicionais
def cachorro_extra():
    print('-------------------- Menu 3 de 3 - Servico adicional -----------------------------------')
    while True:
        print('')
        print('Deseja algum servico adicional ?')
        print('1 - Corte de Unhas - R$ 10,00')
        print('1 - Escovar os Dentes - R$ 12,00')
        print('1 - Limpar as Orelhas - R$ 15,00')
        print('0 - Nao desejo mais nada')

        adiconal = input('>>')


        global valoradicional
        

        if adiconal == '1':    
            valoradicional += 10
        elif adiconal == '2':
            valoradicional += 12
        elif adiconal == '3':
            valoradicional += 15
        elif adiconal == '0':
            # Caso o usuário não queira mais nenhum serviço adicional,
            # retorna 0 para indicar que o loop deve ser interrompido
            return adiconal

        else:
            print('Opção inválida, tente novamente.')

        
        
        

#Inicio do Main
print('-------------------- Bem-Vindo ao petshop do Luccas Duarte Mendanha --------------------')
peso_cachorro = cachorro_peso() # Obtém o peso do cachorro
cachorro_pelo() # Obtém o tamanho do pelo do cachorro
cachorro_extra() # Obtém os serviços adicionais escolhidos pelo usuário
valortotal= valorpeso * valorpelo + valoradicional # Calcula o valor total somando o valor do peso, pelo e adicionais
print('')
print('-------------------- Detalhes do Pedido -------------------------------------------------')
print('O peso do cachorro: ', peso_cachorro,'KG')
print('Tamanho do pelo:','Curto' if valorpelo == 1 else ('Medio' if valorpelo == 1.5 else 'Longo')) # Exibe o tamanho do pelo com base no valorpelo (1 para Curto, 1.5 para Médio, 2 para Longo)
print('Serviços adicionais: R$ {:.2f}'.format (valoradicional))
print('Valor total: R$ {:.2f}'.format (valortotal))
print('------------------------------------------------------------------------------------------')