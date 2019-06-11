import network
import comMorse

ADDRESSE =""
PORT = 1111

while True:

    socket = network.newClientSocket()
    socket.connect((ADDRESSE,PORT))

print("ecrit une lettre")
lettre = input()

morse = comMorse.encode(lettre)
socket.send(morse.encode())

reponse = socket.recv(4096)
print(reponse)