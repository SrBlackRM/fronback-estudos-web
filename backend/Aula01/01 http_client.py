import socket

# criamos um cliente para conexão as configurações passadas em parametro são
# socket.AF_INET > para usarmos IPV4
# socket.SOCK_STREAM > para usarmos a troca de dados de texto, como paginas html, js, css e etc
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# passamos uma tupla para o connect, primeiro elem é o domínio/ip que vamos nos conectar, segundo é a porta do serviço, no caso web é 80.
# mas poderia ser ftp 21, ssh 22
dominio = 'localhost'
client.connect((dominio, 6669))
    
# montamos uma requisição simples
metodo = 'GET'
url = f'https://{dominio}/index.html'
http_version = 'HTTP/1.0'
# user_agent = 'User-Agent: Michel-Client/1.0' (exemplo de user-agent)

# request
# juntamos a requisicao em um comando unico \r\n é para quebra de linha
cmd = f"{metodo} {url} {http_version}\r\n\r\n".encode()

# para enviar o request
client.send(cmd)

# vamos criar um encadeamento para recebimento dos dados (chunk)
while True:
    # receberemos 512 bytes de arquivo por vez
    data = client.recv(512)
    
    # fazemos uma verificação para saber se ficou faltando baixar mais informações, caso contrário, vamos printando o html
    if len(data) < 1:
        break
    # na hora de printar os dados precisamos fazer um decode e o end="" serve para tirar a quebra de linha do final, não atrapalhando o html
    print(data.decode(), end="")

# importante fechar a comunicação com servidor
client.close()



# Forma antiga com requests
# import requests
# result = requests.get("https://example.com")

# print(result.status_code)
# print(result.headers)
# print(result.content)

# import httpx

# result = httpx.get("http://example.com/index.html")
# print(result.headers)