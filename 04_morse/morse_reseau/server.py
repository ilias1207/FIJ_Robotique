import network
import comMorse
import ledArduino

ADDRESS ="10.0.0.113"
PORT=1111

socket = network.newServerSocket()
socket.bind((ADDRESS,PORT))

while True: 
    socket.listen(10)
    print("en écoute...")

    thread = network.newThread(socket.accept())
    thread.start()
    #notre communication

    message = thread.clientsocket.recv(4096)
    morse = message.decode("utf-8")

    print("message reçu : ", morse)
    lettre = comMorse.decode(morse)
    
    print ("message traduit: ", lettre)
    ledArduino.envoieCaractere(lettre)

    thread.clientsocket.send("j'ai bien reçu le message".encode())