import numpy as np
import pygame as pg
from functions import * 
import random

# Configurações da janela e projeção
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

# Inicialização do Pygame
pg.init()
tela = pg.display.set_mode((largura, altura))
clock = pg.time.Clock()

# Definição dos vértices e arestas do cubo
vertices = np.array([[-1, -1, -1], [-1, -1,  1], [-1,  1, -1],
                     [-1,  1,  1], [ 1, -1, -1], [ 1, -1,  1],
                     [ 1,  1, -1], [ 1,  1,  1]])

arestas = [(0, 1),(0, 2),(0, 4),
           (1, 3),(1, 5),(2, 3),
           (2, 6),(3, 7),(4, 5),
           (4, 6),(5, 7),(6, 7)]

# Ajuste de tamanho dos vértices
vertices = vertices.T * 50
vertices = np.vstack((vertices, np.ones((1, vertices.shape[1]))))

# Loop principal do jogo
while rodando:
    for event in pg.event.get():
        # Tratamento de eventos
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                rodando = False  
        if event.type == pg.QUIT:
            rodando = False

        if event.type == pg.MOUSEWHEEL:
            # Altera a distância focal com a roda do mouse
            if event.y > 0 and distancia_focal < 1460:
                distancia_focal += 25
            elif event.y < 0 and distancia_focal > 26:
                distancia_focal -= 25

    # Controle de movimento e velocidade de rotação
    teclas_pressionadas = pg.key.get_pressed()
    if teclas_pressionadas[pg.K_UP]:
        aumento += 0.001 
    if teclas_pressionadas[pg.K_DOWN] and aumento > 0.02:
        aumento -= 0.001 

    if teclas_pressionadas[pg.K_a]:
        x -= 4  
    if teclas_pressionadas[pg.K_d]:
        x += 4  
    if teclas_pressionadas[pg.K_w] and distancia_focal < 1450:
        distancia_focal += 25  
    if teclas_pressionadas[pg.K_s] and distancia_focal > 26:
        distancia_focal -= 25  

    angulo += aumento
    tela.fill((0, 0, 0))  

    # Aplica transformações nos vértices e projeta na tela
    vertices_rotacionados = translacao(x, y, 200) @ rotacao_x(angulo) @ rotacao_y(angulo) @ rotacao_z(angulo) @ vertices
    pontos_projetados = projecao_cubo(vertices_rotacionados, distancia_focal)

    # Seleção aleatória de cores para as arestas do cubo
    cores = [
        (255, 0, 0),  # Vermelho
        (255, 165, 0),  # Laranja
        (255, 255, 0),  # Amarelo
        (0, 255, 0),  # Verde limão
        (0, 255, 255),  # Ciano
        (0, 0, 255),  # Azul
        (128, 0, 128),  # Roxo
        (255, 0, 255),  # Magenta
        (255, 255, 255),  # Branco
        (255, 0, 150),  # Rosa
        (0, 128, 0),  # Verde
        (128, 0, 0),  # Marrom
        (0, 128, 128),  # Azul turquesa
        (255, 255, 224),  # Amarelo claro
        (255, 140, 0),  # Laranja escuro
        (0, 139, 139),  # Ciano escuro
        (139, 0, 139)  # Magenta escuro
    ]

    # Altera a cor das arestas com base no cooldown
    if cooldown_contador <= 0:
        cor = random.choice(cores)
        cooldown_contador = cooldown
    else:
        cooldown_contador -= 1

    # Desenha as arestas do cubo na tela
    for vertice in arestas:
        ponto_inicial = (pontos_projetados[vertice[0]][0] + (largura / 2), pontos_projetados[vertice[0]][1] + altura / 2)
        ponto_final = (pontos_projetados[vertice[1]][0] + (largura / 2), pontos_projetados[vertice[1]][1] + altura / 2)
        pg.draw.line(tela, cor, ponto_inicial, ponto_final, 4)

    pg.display.update()  
    clock.tick(60)  

pg.quit()  