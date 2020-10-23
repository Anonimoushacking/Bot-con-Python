from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from selenium import webdriver
import logging
logging.basicConfig(filename='archivarlog.log',level=logging.DEBUG)


chatbot = ChatBot('Jhon')

chatbot.storage.drop()

conversacion = open('conoc.txt','r').readlines()

entrenador = ListTrainer(chatbot)

entrenador.train(conversacion)

while True:
    solicitud = input('YO: ')
    respuesta = chatbot.get_response(solicitud)
    print('Jhon: ',respuesta)
    

