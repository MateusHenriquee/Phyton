import pygame # usado para jogos
pygame.init() # inicia o pygame
pygame.mixer.init() # inicializa o mixer (importante!)
pygame.mixer.music.load('exercicio\musica\slk.mp3') # carrega a música
pygame.mixer.music.play() # toca a música
input()# Pausa o programa até você apertar Enter dando tempo do pygame inicializar corretamente
pygame.event.wait()