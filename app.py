import speech_recognition as sr
import os
import gtts
from playsound import playsound


arquivos = []
pasta_audio = 'audioe'

def listen():
  microfone = sr.Recognizer()
  
  with sr.Microphone() as path:
    microfone.adjust_for_ambient_noise(path)

    print('fala ai')

    audio = microfone.listen(path)

    try:
      frase = microfone.recognize_google(audio, language='pt-BR')
      arquivos.append(frase)
      
      frase_falada = arquivos[-1] 
    
      print('Você falou isso: ' + frase_falada)
      
      return frase_falada
    
    except sr.UnknownValueError:
      print('não consegui capturar o audio')

def speak():
  caminho = listen()
  with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read()
    mp3 = conteudo[:3].lower() + '.mp3'
    caminho = os.path.join(pasta_audio, mp3)
    if not os.path.exists(pasta_audio): 
      os.makedirs(pasta_audio)
    frase = gtts.gTTS(conteudo, lang='pt-br')
    frase.save(caminho)
    playsound(caminho)



speak()