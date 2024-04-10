# Projeção 3D de um Cubo

## Introdução:

O projeto consiste na confecção de um cubo colorido em 3D que gira constantemente, podendo mover a câmera para visualizar o cubo em vários perspectivas, aumentar e diminuir a velocidade na qual o cubo gira e aumentar e diminuir a distância focal (zoom) da câmera.

## Como Utilizar o programa:

1. O cubo inicia com uma aceleração padrão, que pode ser aumentada e diminuída através das setas de "cima" e "baixo" do teclado;
2. A posição da câmera pode ser alterada horizontalmente para visualizar o cubo de diferentes perspectivas através das teclas de  ```a``` e ```d```;
3. A distância focal pode ser mudada através do scroll do mouse ou das teclas de ```w``` e ```s```, podendo mover a câmera para frente e para trás até um limite;
4. O Pygame é fechado ao clicar no X presente na tela ou através da tecla ```esc``` no teclado.

## Como Executar:

1. Instale o python em seu computador;
2. Clone esse repositório para sua máquina;
3. Instale as bibliotecas necessárias (contidas em ```requirements.txt```);
4. Execute a projeção pelo arquivo ```main.py```.

## Organização:

O código está separado em arquivos, com cada arquivo comentado para melhor organização do projeto;<br>
As funções estão separadas no arquivo ```functions.py```.

## Código e Modelo Físico:

### 1. Cálculo de Rotação e Translação do Cubo:

O motivo para o cálculo das rotações e translação é aplicar as transformações aos vértices do cubo antes de projetá-los na tela. Essas transformações permitem que o cubo seja movido e rotacionado em um espaço tridimensional e para isso, há a multiplicação da função de translação pela rotação das 3 dimensões, além da multiplicação da matriz resultante das rotações e translação pelos vértices originais do cubo. A função de translação recebe o ```x``` atual, o ```y``` atual e inicialmente o ```z=200```, representando a profundidade de visão ao cubo. Já as funções de rotação recebem o atual ângulo de rotação e realizam a multiplicação matricial através das matrizes expostas abaixo.

### 2. Matrizes:

#### Matriz de Transformação:

$$
\begin{bmatrix}
z_p \\
x_{p}w_{p} \\
w_p \\
\end{bmatrix} = 
\begin{bmatrix}
0 & 0 & -d \\
1 & 0 & 0 \\
0 & -\frac{1}{d} & 0 \\
\end{bmatrix}
\begin{bmatrix}
x_o \\
z_o \\
1 \\
\end{bmatrix}
$$

#### Matrizes de Rotação (X, Y e Z):

$$
R_x = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos(\theta) & -\sin(\theta) & 0 \\
0 & \sin(\theta) & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_y = \begin{bmatrix}
\cos(\theta) & 0 & \sin(\theta) & 0 \\
0 & 1 & 0 & 0 \\
-\sin(\theta) & 0 & \cos(\theta) & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\hspace{0.5in}
R_z = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & 0 \\
\sin(\theta) & \cos(\theta) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

#### Matriz de Translação:

$$
T = \begin{bmatrix}
1 & 0 & 0 & x \\
0 & 1 & 0 & y \\
0 & 0 & 1 & z \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

### 3. Função de Projeção:

#### Introdução:

Em resumo, a função ```projecao_cubo(pontos, dist_focal)``` realiza uma projeção perspectiva dos pontos seguindo o modelo de câmera pinhole. A projecão dos pontos tridimensionais é feita em relação a uma câmera virtual com distância focal ```dist_focal```, retornando as coordenadas projetadas dos pontos no plano de imagem (2D), com a profundidade z mantida como parte da informação retornada. Ou seja, a função recebe pontos em 3D e os remodela para 2D para que eles possam ser mostrados no computador.

#### Definição da Matriz de Transformação:

A função começa definindo uma matriz de transformação ```transformacao``` que descreve a projeção perspectiva.<br>
A primeira linha da matriz (```[0, 0, 0, -dist_focal]```) define um deslocamento ao longo do eixo z (para trás) equivalente à distância focal negativa.<br>
As próximas três linhas (```[1, 0, 0, 0]```, ```[0, 1, 0, 0]```, ```[0, 0, -1/dist_focal, 0]```) são parte da matriz de projeção perspectiva.

#### Aplicação da Transformação aos Pontos:

A matriz de transformação transformacao é aplicada aos pontos tridimensionais pontos utilizando multiplicação matricial:<br>
```matriz_transformada = transformacao @ pontos```

#### Projeção dos Pontos Transformados:

Para cada ponto transformado (representado por uma coluna na matriz transformada), calcula-se a coordenada z do ponto.<br>
Verifica-se se a coordenada z do ponto original (```pontos[2][i]```) é menor ou igual a zero. Caso não seja, significa que o ponto está à frente da câmera (na direção do eixo z).<br>
Para os pontos que estão à frente da câmera, calcula-se as coordenadas projetadas (```ponto[1]/z```, ```ponto[2]/z```, ```pontos[2][i]```). Aqui, ```ponto[1]/z``` e ```ponto[2]/z``` representam a projeção 2D do ponto no plano de imagem.<br>
Se o ponto estiver atrás da câmera (ou na mesma posição), as coordenadas projetadas são definidas como ```(0, 0, 0)```.<br>

#### Conversão para NumPy Array e Retorno:

Os pontos projetados são armazenados em uma lista ```pontos_projetados``` e convertidos em um array NumPy A, que é então retornado pela função.

### 4. Projeção Final do Cubo:

Ao início, são definidos os vértices e as arestas que compõem o cubo. Os vértices são especificados como uma matriz NumPy, e as arestas são listadas como pares de índices de vértices:<br>

    vertices = np.array([[-1, -1, -1], [-1, -1,  1], [-1,  1, -1],
                         [-1,  1,  1], [ 1, -1, -1], [ 1, -1,  1],
                         [ 1,  1, -1], [ 1,  1,  1]])

    arestas = [(0, 1),(0, 2),(0, 4),
               (1, 3),(1, 5),(2, 3),
               (2, 6),(3, 7),(4, 5),
               (4, 6),(5, 7),(6, 7)]

Ao final, após a aplicação das multiplicações matriciais descritas acima, o loop ```for``` itera sobre as arestas do cubo, calcula os pontos iniciais e finais das linhas projetadas (```ponto_inicial``` e ```ponto_final```), e então desenha cada linha na tela utilizando a função ```pg.draw.line``` do Pygame. Em suma, o código renderiza os pontos projetados como linhas na tela, sendo cada linha representada por uma aresta do cubo.

## Coloração do Cubo:

A cada segundo é sorteada uma cor para todas as linhas do cubo, para que a experiência fique mais diversa e interessante, dentre as cores a seguir:

```(255, 0, 0)```, ```(255, 165, 0)```, ```(255, 255, 0)```, ```(0, 255, 0)```, ```(0, 255, 255)```, ```(0, 0, 255)```, ```(128, 0, 128)```, ```(255, 0, 255)```, ```(255, 255, 255)```, 
```(255, 0, 150)```, ```(0, 128, 0)```, ```(128, 0, 0)```, ```(0, 128, 128)```, ```(255, 255, 224)```, ```(255, 140, 0)```, ```(0, 139, 139)```, ```(139, 0, 139)```.

As cores estão representadas pela escala RGB (Red, Green, Blue).

## Referências:
1. [ChatGPT](https://chat.openai.com/) para saciar dúvidas relacionadas ao pygame.

## Créditos:
Projeto desenvolvido por Gustavo Colombi Ribolla e Rafaela Afférri de Oliveira.