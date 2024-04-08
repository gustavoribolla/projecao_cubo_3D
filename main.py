import numpy as np
import pygame as pg
from functions import *
import random

largura = 640
altura = 480
distancia_focal = 200
rodando = True
angulo = 0
aumento = 0.02
cooldown = 60  
cooldown_contador = 0
cor = (255, 0, 150) 
x = 0
y = 0

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


while rodando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodando = False
        if event.type == pg.MOUSEWHEEL:
            if event.y > 0 and distancia_focal < 1460:
                distancia_focal += 25
            elif event.y < 0 and distancia_focal > 26:
                distancia_focal -= 25

    # Mudar a velocidade de rotação
    teclas_pressionadas = pg.key.get_pressed()
    if teclas_pressionadas[pg.K_UP]:
        aumento += 0.001
    if teclas_pressionadas[pg.K_DOWN] and aumento > 0.02:
        aumento -= 0.001

    #Mover a tela
    if teclas_pressionadas[pg.K_a]:
        x -= 4
    if teclas_pressionadas[pg.K_d]:
        x += 4
    if teclas_pressionadas[pg.K_w]:
        y -= 4
    if teclas_pressionadas[pg.K_s]:
        y += 4

    angulo += aumento
    tela.fill((0, 0, 0))

    vertices_rotacionados = translacao(0, 0, 0) @ translacao(x, y, 250) @ rotacao_x(angulo) @ rotacao_y(
        angulo) @ rotacao_z(angulo) @ vertices
    pontos_projetados = projecao_cubo(vertices_rotacionados, distancia_focal)

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
    (255, 0, 150),    # Pink
    (0, 128, 0),      # Green
    (128, 0, 0),      # Maroon
    (0, 128, 128),    # Teal
    (165, 42, 42),    # Brown
    (255, 255, 224),  # Light Yellow
    (255, 140, 0),    # Dark Orange
    (0, 139, 139),    # Dark Cyan
    (139, 0, 139)     # Dark Magenta
    ]

    if cooldown_contador <= 0:
        cor = random.choice(cores)
        cooldown_contador = cooldown
    else:
        cooldown_contador -= 1

    for vertice in arestas:
        ponto_inicial = (pontos_projetados[vertice[0]][0] + (largura / 2), pontos_projetados[vertice[0]][1] + altura / 2)
        ponto_final = (pontos_projetados[vertice[1]][0] + (largura / 2), pontos_projetados[vertice[1]][1] + altura / 2)
        pg.draw.line(tela, cor, ponto_inicial, ponto_final, 4)

    pg.display.update()
    clock.tick(60)

pg.quit()
