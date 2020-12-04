import this

import pygame

pygame.init()
pygame.display.set_caption("minimal program")

screen = pygame.display.set_mode((800, 600), 0)

amarelo = (255, 255, 0)
preto = (0, 0, 0)
azul = (0, 43, 255)

num_colunas = 30
num_linhas = 40

class Control():
    def __init__(self):
        self.lista_tropas = [] #uma lista com todas as tropas
        self.tropas_selecionadas = [] #uma lista com todas as tropas selecionadas

    def mouse_position_to_grid(self, pos):
        tuple = (pos[0]//num_linhas, pos[1]//num_colunas)
        return tuple

    def grid_to_mouse_position(self, grid):
        tuple = (grid[0]*num_linhas, grid[1]*num_colunas)
        return tuple

    def cria_tropa(self, pos): # cria uma tropa dada uma posição
        pos = self.grid_to_mouse_position(self.mouse_position_to_grid(pos))
        tropa = Tropa(pos)
        self.lista_tropas.append(tropa)

    def pinta_tropas(self): #itera através da lista de tropas e pinta
        for tropa in self.lista_tropas:
            tropa.pinta_tropa(screen)

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if evento.button == 1: #botão esquerdo
                    if self.verifica_tropa(pos) == None:
                        self.cria_tropa(pos) #cria uma tropa caso não hajam outras tropas no lugar
                elif evento.button == 3: #botão direito
                    if self.verifica_tropa(pos) != None:
                        t = self.verifica_tropa(pos)
                        t.cor = amarelo #seleciona uma tropa caso uma já exista no lugar, a pinta de amarelo e a adiciona a lista de tropas selecionadas
                        if t not in self.tropas_selecionadas:
                            self.tropas_selecionadas.append(t)
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_e: #limpa lista de tropas selecionadas
                    for tropa in self.tropas_selecionadas:
                        tropa.cor = azul
                    self.tropas_selecionadas.clear



    def verifica_tropa(self, pos): #Verifica se alguma tropa já está nessa posição
        pos = self.grid_to_mouse_position(self.mouse_position_to_grid(pos))
        for tropa in self.lista_tropas:
            if pos == tropa.pos:
                return tropa
        return None

class Tropa():
    def __init__(self, pos):
        self.control = Control()
        self.pos = pos
        self.cor = azul
    def pinta_tropa(self, tela):
        grid = control.mouse_position_to_grid(self.pos)
        grid = control.grid_to_mouse_position(grid)
        pygame.draw.rect(tela, self.cor, (grid[0], grid[1], num_linhas, num_colunas), 0)

if __name__=="__main__":

    control = Control()

    while True:
        screen.fill(preto)
        control.pinta_tropas()
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit(2)

        control.processar_eventos(events)