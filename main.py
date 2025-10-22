import pygame

print('inicio')
pygame.init()
window = pygame.display.set_mode((800, 600))
print('fim')

while True:
    # Checar os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #fechar janela
            quit()  # Fim pygame
