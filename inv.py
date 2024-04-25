def principal():
    while True:
        opcao = input('Deseja inverter alguma string? s[im]/n[ao] >> ')
        if opcao == 's' or opcao == 'sim':
            pass
        elif opcao == 'n' or opcao == 'nao':
            break
        else:
            print('Opção inválida.')
            continue
        string = informa_string()
        if string:
            inversao = inverte_string(string)
            print(inversao)


# Permite ao osuário informar a string que ele deseja inverter
def informa_string():
    string = input('Escreva uma palavra ou uma frase para inverter: ')
    return string


# Realiza a inversão da string informada
def inverte_string(string):
    return string[::-1]


principal()
