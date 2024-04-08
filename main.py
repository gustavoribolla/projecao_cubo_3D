import numpy as np
import pygame as pg
from functions import *
import random

largura = 640
altura = 480
distancia_focal = 200
rodando = True
angulo = 0
posicao_jogador = np.array([0, 0, 0, 1])


pg.init()
tela = pg.display.set_mode((largura, altura))
clock = pg.time.Clock()

vertices = np.array([
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1]])

arestas = [
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7)]

vertices = vertices.T * 50
vertices = np.vstack((vertices, np.ones((1, vertices.shape[1]))))
posicao = np.array([0, 0, 0, 1])

cores = [
    (255, 0, 0),      # Red
    (255, 165, 0),    # Orange
    (255, 255, 0),    # Yellow
    (0, 255, 0),      # Lime
    (0, 255, 255),    # Cyan
    (0, 0, 255),      # Blue
    (128, 0, 128),    # Purple
    (255, 0, 255),    # Magenta
    (128, 128, 128),  # Gray
    (255, 255, 255),  # White
    (0, 0, 0),        # Black
    (255, 192, 203),  # Pink
    (0, 128, 0),      # Green
    (128, 0, 0),      # Maroon
    (0, 128, 128),    # Teal
    (165, 42, 42),    # Brown
    (255, 255, 224),  # Light Yellow
    (255, 140, 0),    # Dark Orange
    (0, 139, 139),    # Dark Cyan
    (139, 0, 139)     # Dark Magenta
]



rodando = True

while rodando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            rodando = False

    angulo += 0.01
    tela.fill((0,0,0))

    vertices_rotacionados = translacao(0,0,0) @ translacao(0, 0, 250) @ rotacao_x(angulo) @ rotacao_y(angulo) @ rotacao_z(angulo) @ vertices
    
    pontos_projetados = projecao_cubo(vertices_rotacionados, distancia_focal)

    cor = random.choice(cores)
    for vertice in arestas :

        ponto_inicial = (pontos_projetados[vertice[0]][0] + (largura/2), pontos_projetados[vertice[0]][1] + altura/2)
        ponto_final = (pontos_projetados[vertice[1]][0] + (largura/2), pontos_projetados[vertice[1]][1] + altura/2)
        pg.draw.line(tela, cor, ponto_inicial, ponto_final, 4)

    pg.display.flip()
    clock.tick(50)

pg.quit()