import speech_recognition as sr
import pyttsx3

notas_falar = [] 
notas_audicao = []
# Inicializar o reconhecedor de fala e o engine de conversão de texto para fala
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Método para converter texto em fala
def falar(texto):
    engine.say(texto)
    engine.runAndWait()

# Função para capturar e transcrever a fala
def audicao():
    with sr.Microphone() as microfone:
        print("Fale algo...")
        try:
            # Capta a fala
            fala = recognizer.listen(microfone)
            # Transcreve a fala para texto
            texto = recognizer.recognize_google(fala, language="pt-BR") #A biblioteca usa uma API do Google
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Erro no serviço de reconhecimento de fala: {e}")
            return None

# Main
def main():
    while True:
        print()
        print("####################################################")
        print("## Módulo de Teste Audição e Fala - Projeto PIBEX ##")
        print("####################################################")
        print()
        print("####################################################")
        print("## Digite:                                        ##")
        print("##   1: Transcrever algo que foi falado           ##")
        print("##   2: Falar algo que foi digitado               ##")
        print("##   3: Ver a nota dos testes                     ##")
        print("##   0: Sair do módulo de teste                   ##")
        print("####################################################")
        print()
        opcao = input("Escolha uma opção (1, 2, 3 ou 0): ")

        if opcao == "1":
            audio = audicao()
            nota_da_audicao = int(input('Digite 1 para uma transcrição perfeita ou 0 para uma transcrição com erros: '))
            notas_audicao.append(nota_da_audicao)
            input("Pressione ENTER para continuar...")
        elif opcao == "2":
            texto_digitado = input("Digite algo para eu falar: ")
            falar(texto_digitado)
            nota_da_fala = int(input('Digite 1 para uma fala perfeita e 0 para algum erro: '))
            notas_falar.append(nota_da_fala)
            input("Pressione ENTER para continuar...")
        
        elif opcao == '3':
          zeros_audicao = 0
          uns_audicao = 0
          zeros_falar = 0
          uns_falar = 0
          
          for nota in notas_audicao:
              if nota == 0:
                  zeros_audicao += 1
              elif nota == 1:
                  uns_audicao += 1
           
          for nota in notas_falar:
              if nota == 0:
                  zeros_falar += 1
              elif nota == 1:
                  uns_falar += 1

          precisao_audicao = (100 * uns_audicao) / len(notas_audicao)
          precisao_falar = (100 * uns_falar) / len(notas_falar)
          
          print(f'A precisão da função falar é:  {precisao_falar}, Com um total de acertos de:  {uns_falar}')
          print(f'A precisão da função audição é:  {precisao_audicao}, Com um total de acertos de:  {uns_audicao}')
          input("Pressione ENTER para continuar...")
    
        elif opcao == "0":
            print("Módulo de teste finalizado!")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
