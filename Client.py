from socket import *

serverName = '127.0.0.1'
serverPort = 6789

sentence = input("metti una frase: ")

while sentence != "END":

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    clientSocket.makefile('w').writelines(sentence + '\n')

    response = clientSocket.makefile().readline()
    print("Risposta: " + response)

    clientSocket.close()
    sentence = input()

