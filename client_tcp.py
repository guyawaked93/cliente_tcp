import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    host = "google.com.br"
    port = 80

    client.connect((host,port))

    enviando = b"GET / HTTP/1.1\nHost: google.com.br\n\n"
    client.send(enviando)

    recebendo = client.recv(1024).decode()
    print(recebendo)

except Exception as erro:
    print("Erro ao tentar estabelecer conecxao:", erro)

finally:
    client.close()