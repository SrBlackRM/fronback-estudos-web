import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# diferente do cliente que usa o método send para envio da requisição, o server usa o método bind para acoplar o serviço com uma porta tcp e a interface
# de rede 
server.bind(("localhost", 6669))

# a partir desse momento, já vai ter um descritor do windows ou linux apontando para essa porta
# precisamos agora de um lisntening para escutar essa porta
server.listen()

# precisamos de um loop de eventos para que o servidor fique escutando naquela porta
try:
    # cada vez que esse loop rodar, pegamos o request, interpretamos e trabalhamos em cima dele e retornamos dados para o cliente
    while True:
        # a instancia de client é apenas uma referencia para saber qual é o client e pegar o request
        client, address = server.accept() # metodo accept() retorna uma tupla
        data = client.recv(5000).decode() # encode e decode para enviar/receber dados, como estamos recebendo do cliente, fazemos o decode nesse caso
        print(f'{data=}')
        
        # response
        client.sendall(
            "HTTP/1.0 200 OK\r\n<html><body>Hello</body></html>\r\n\r\n".encode()
        )
        
        # mandar um sinal para terminar a conexão com o client
        client.shutdown(socket.SHUT_WR)
        
except Exception:
    server.close()

# para liberar a porta e o sistema operacional não travar ela após o uso
server.close()