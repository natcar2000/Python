sequencia = [0, 1]


def principal():
    while True:
        opcao = input('Deseja verificar se um número faz parte da sequência de Fobonacci? s[im]/n[ao] >> ')
        if opcao == 's' or opcao == 'sim':
            pass
        elif opcao == 'n' or opcao == 'nao':
            break
        else:
            print('Opção inválida.')
            continue
        numero = informa_numero()
        if numero:
            verificacao = verifica_numero(numero)
            print(verificacao)


# Permite ao osuário informar o número que ele deseja verificar se faz parte da sequência de Fibonacci
def informa_numero():
    numero = int(input('Informe um número entre 0 e 1000: '))
    return numero


# Verifica se o número informado faz parte da sequência de Fibonacci
def verifica_numero(numero):
    membro_atual = sequencia[-1]
    for i in range(15):
        membro_atual += sequencia[-2]
        sequencia.append(membro_atual)
    if numero in sequencia:
        return 'O número informado pertence à sequência.'
    else:
        return 'O número informado não pertence à sequência.'


principal()
