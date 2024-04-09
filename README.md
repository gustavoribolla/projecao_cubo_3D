# Projeção 3D de um Cubo

## Introdução:

O projeto consiste na confecção de um cubo em 3D que gira constantemente, podendo mover a câmera para visualizar o cubo em vários ângulos, aumentar e diminuir a velocidade na qual o cubo gira e aumentar e diminuir a distância focal (zoom) da câmera.

## Como Jogar:

1. O cubo inicia com uma aceleração padrão, que pode ser aumentada e se aumentada, diminuida através das setas de "cima" e "baixo" do teclado;
2. A posição da câmera pode ser alterada para visualizar o cubo de diferentes ângulos através das teclas de ```w```, ```a```, ```s``` e ```d```;
3. A distância focal pode ser mudada através do scroll do mouse, podendo mover a câmera para frente e para trás até um limite.

## Como Executar:

1. Instale o python em seu computador;
2. Clone esse repositório para sua máquina;
3. Instale as bibliotecas necessárias (contidas em ```requirements.txt```);
4. Execute o jogo pelo arquivo ```main.py```.

## Organização:

O código está separado em arquivos, com cada arquivo comentado para melhor organização do projeto;<br>
As funções estão separadas no arquivo ```functions.py```.

## Código e Modelo Físico:
### 1. Matrizes:

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

## Referências:
1. [ChatGPT](https://chat.openai.com/) para saciar dúvidas relacionadas ao pygame.

## Créditos:
Projeto desenvolvido por Gustavo Colombi Ribolla e Rafaela Afférri de Oliveira.