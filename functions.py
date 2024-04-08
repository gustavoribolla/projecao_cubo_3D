import numpy as np

def rotacao_x(theta):
    A = np.array([[1, 0, 0, 0],
                  [0, np.cos(theta), -np.sin(theta), 0],
                  [0, np.sin(theta), np.cos(theta), 0],
                  [0, 0, 0, 1]])
    return A

def rotacao_y(theta):
    A = np.array([[np.cos(theta), 0, np.sin(theta), 0],
                  [0, 1, 0, 0],
                  [-np.sin(theta), 0, np.cos(theta), 0],
                  [0, 0, 0, 1]])
    return A

def rotacao_z(theta):
    A = np.array([[np.cos(theta), -np.sin(theta), 0, 0],
                  [np.sin(theta), np.cos(theta), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    return A

def translacao(x, y, z):

    A = np.array([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1]])

    return A

def projecao_cubo(pontos, dist_focal):

    transformacao = np.array([[0,0,0,-dist_focal], 
                              [1,0,0,0], 
                              [0,1,0,0], 
                              [0,0,-1/dist_focal,0]])
    
    matriz_transformada = transformacao @ pontos
    pontos_projetados = []
    for i, ponto in enumerate(matriz_transformada.T):
        z = ponto[3]
        if pontos[2][i] > 0:
            pontos_projetados.append((ponto[1]/z, ponto[2]/z, pontos[2][i]))
        else:
            pontos_projetados.append((0, 0, 0))
    return np.array(pontos_projetados)