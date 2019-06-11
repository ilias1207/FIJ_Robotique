# coding: utf-8
import ledArduino
import dicoMatrice2D
import comMorse

print("tape une Lettre")
Lettre = input()
reponseMorse = comMorse.encode(Lettre)
print("lecode morse est :", reponseMorse)

reponse = comMorse.decode(reponseMorse)
ledArduino.envoieCaractere(reponse)