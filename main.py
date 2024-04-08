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

rodando = True

while rodando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            rodando = False

        if event.type == pg.KEYDOWN:
            # Altera a velocidade do personagem
            if event.key == pg.K_UP:
                aumento += 0.01
            if event.key == pg.K_DOWN and aumento > 0.02:
                aumento -= 0.01

        if event.type == pg.MOUSEWHEEL:
            if event.y > 0 and distancia_focal<1460:
                distancia_focal += 25
            elif event.y < 0 and distancia_focal>26:
                distancia_focal -= 25
        # # Obtém o movimento relativo do mouse
        # rel_x, rel_y = pg.mouse.get_rel()
        # # Ajusta a distância focal com base no movimento do mouse
        # distancia_focal -= rel_y

    angulo += aumento
    tela.fill((0,0,0))

    vertices_rotacionados = translacao(0,0,0) @ translacao(0, 0, 250) @ rotacao_x(angulo) @ rotacao_y(angulo) @ rotacao_z(angulo) @ vertices
    pontos_projetados = projecao_cubo(vertices_rotacionados, distancia_focal)


    for vertice in arestas :

        ponto_inicial = (pontos_projetados[vertice[0]][0] + (largura/2), pontos_projetados[vertice[0]][1] + altura/2)
        ponto_final = (pontos_projetados[vertice[1]][0] + (largura/2), pontos_projetados[vertice[1]][1] + altura/2)
        pg.draw.line(tela, (255, 0, 150), ponto_inicial, ponto_final, 4)

    pg.display.update()
    clock.tick(50)

pg.quit()