from random import randint
numero_random = randint(0,10)
print('Sou seu computador...Acabei de pensar em um número de 0 a 10, você consegue adivinhar qual é? ')
acertou = False
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    if jogador != numero_random:
        print('Você não acertou, noob!')
    if jogador == numero_random:
        acertou = True
        print('Acertou, peste!')
    10