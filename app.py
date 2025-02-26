import speech_recognition as sr
import os
import gtts
from playsound import playsound

validacao_listen = []
validacao_speak = []
log_frases = []
pasta_audio = 'audioe'

def listen():
  microfone = sr.Recognizer()
  
  with sr.Microphone() as path:
    microfone.adjust_for_ambient_noise(path)

    print('fala ai')

    audio = microfone.listen(path)

    try:
      frase = microfone.recognize_google(audio, language='pt-BR')
      log_frases.append(frase)
      
      frase_falada = log_frases[-1] 
    
      print('Você falou isso: ' + frase_falada)
      
      return frase_falada
    
    except sr.UnknownValueError:
      print('não consegui capturar o audio')

def speak(conteudo):
  nome_arquivo = conteudo.split()

  for nome in nome_arquivo: 
    mp3 = nome.lower() + '.mp3'
    
    if not os.path.exists(pasta_audio): 
      os.makedirs(pasta_audio)
  
    caminho = os.path.join(pasta_audio, mp3)
    
    if not os.path.exists(caminho):
      frase = gtts.gTTS(conteudo, lang='pt-br')
      frase.save(caminho)
      playsound(caminho)
      break
    
    elif os.path.exists(caminho):
      continue
  

while True:
  frase = listen()
  continuar = input('O que você digitou está correto? S/N').upper()[0] 
  
  if continuar == 'S':
    speak(frase)
  
  elif continuar =='N':
    break