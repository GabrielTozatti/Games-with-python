from random import choice

################################
################################

def jogar():
    
    mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(f'PALAVRA: {letras_acertadas}')
    
    enforco = False
    acertou = False
    erros = 0
    
    while(not enforco and not acertou):
    
        chute = pede_chute()
               
        if chute in palavra_secreta:
           marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
          
        enforco = erros == 7
        acertou = '-' not in letras_acertadas
        print(letras_acertadas)
        
    if acertou:
        mensagem_ganhador()
    else:
       mensagem_perdeu(palavra_secreta)
       
################################
################################

def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")

def carregar_palavra_secreta():
    arquivo = open('palavras.txt', 'r', encoding="utf-8")
    palavra_secreta = choice([linha.strip().upper() for linha in arquivo])
    arquivo.close()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['-' for letra in palavra]

def pede_chute():
    chute = input('Digite uma letra: ')
    return chute.strip().upper()

def marca_chute_correto(chute, palavra_secreta,  letras_acertadas):
    index = 0 
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[index] = letra
        index += 1
        
def mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def mensagem_perdeu(palavra_secreta):
    print('Puxa, você foi enforcado!')
    print(f'A palavra era {palavra_secreta}')
    
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
        
if(__name__ == "__main__"):
    jogar()