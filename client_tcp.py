import socket

# Criação de um socket cliente TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Definindo o host e a porta para a conexão com o servidor web
    host = "google.com.br"
    port = 80

    # Estabelecendo uma conexão com o servidor
    client.connect((host, port))

    # Montando a solicitação HTTP GET
    enviando = b"GET / HTTP/1.1\nHost: google.com.br\n\n"

    # Enviando a solicitação para o servidor
    client.send(enviando)

    # Recebendo e decodificando os dados recebidos do servidor
    recebendo = client.recv(1024).decode()

    # Imprimindo os dados recebidos (conteúdo da página web)
    print(recebendo)

except Exception as erro:
    # Lidando com erros que podem ocorrer durante a conexão
    print("Erro ao tentar estabelecer conexão:", erro)

finally:
    # Fechando o socket cliente independentemente do resultado
    client.close()
