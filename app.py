import speech_recognition as sr
import os
import gtts
from playsound import playsound

pasta_texto = 'text'
pasta_audio = 'audioe'

def listen():
  microfone = sr.Recognizer()
  with sr.Microphone() as path:
    microfone.adjust_for_ambient_noise(path)

    print('fala ai')

    audio = microfone.listen(path)

    try:
      frase = microfone.recognize_google(audio, language='pt-BR')
      arquivo = frase[:3].lower() + '.txt'
      caminho = os.path.join(pasta_texto, arquivo)
      
      with open(caminho, 'x') as arquivo:
        arquivo.write(frase)
      return caminho
    
    except sr.UnknownValueError:
      print('não consegui capturar o audio')

def speak():
  caminho = listen()
  with open(caminho, 'r') as arquivo:
    conteudo = arquivo.read()
    mp3 = conteudo[:3].lower() + '.mp3'
    caminho = os.path.join(pasta_audio, mp3)
    frase = gtts.gTTS(conteudo, lang='pt-br')
    frase.save(caminho)
    playsound(caminho)



speak()