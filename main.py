import numpy as np
import pygame as pg
from functions import *

largura = 480
altura = 640
distancia_focal = 200
rodando = True
angulo_rotacao = 0
tela = pg.display.set_mode((largura, altura))
clock = pg.time.Clock()

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

vertices = np.array([
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, -1],
    [-1, 1, 1],
    [1, -1, -1],
    [1, -1, 1],
    [1, 1, -1],
    [1, 1, 1],])

vertices = vertices.T*50
vertices = np.vstack((vertices, np.ones((1, vertices.shape[1]))))

while rodando:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            rodando = False

    projecao_pontos = projecao_cubo(vertices, distancia_focal)
    tela.fill((0, 0, 0))

    for aresta in arestas:
        inicio = (projecao_pontos[aresta[0]][0] + largura/2, projecao_pontos[aresta[0]][1] + altura/2)
        fim = (projecao_pontos[aresta[1]][0] + largura/2, projecao_pontos[aresta[1]][1] + altura/2)

        distancia_inicio = projecao_pontos[aresta[0]][2]
        distancia_fim = projecao_pontos[aresta[1]][2]
        linha_largura = 1/(distancia_inicio/1400 + distancia_fim/1400)

        if projecao_pontos[aresta[0]][2] > 0 and projecao_pontos[aresta[1]][2] > 0 and linha_largura < 30:
            pg.draw.line(tela, (255, 255, 255), inicio, fim, int(linha_largura))
        
    pg.display.flip()
    clock.tick(60)

pg.quit()