-> Submit in Moodle a brief presentation (max. 5 slides), in PDF format (will be used in the class to analyze, 
together with the teacher, the progress of the work)

# Unequal Length Mazes

## Descrição

O jogo **Unequal Length Mazes** consiste num tabuleiro de dimensões arbitrárias com algumas das suas células bloqueadas (obstáculos). O objetivo do jogo é encontrar um caminho desde a célula inferior esquerda até à célula superior direita que passe por todas as células disponíveis (não bloqueadas) apenas uma vez. O caminho deve alternar entre segmentos horizontais e verticais e dois segmentos consecutivos não podem ter o mesmo tamanho. Como é representado na figura seguinte:

<div align="center">
  <img src="../img/GameSolvedExample.png" alt="Exemplo de Solução">
  <p style="margin-top:10px"><i>Figura 1: Exemplo de solução do jogo</i></p>
</div>


## Referência Bibliográficas

Trabalhos relacionados e referências encontradas online:
1. [Jogo semelhante em partes](https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/)
2. [Pathfinding e resolução de labirintos com algoritmo de pesquisa A*](https://www.scirp.org/journal/paperinformation.aspx?paperid=70460)
3. [A-Star para resolução de labirintos](https://levelup.gitconnected.com/a-star-a-search-for-solving-a-maze-using-python-with-visualization-b0cae1c3ba92)

## Formulação do Problema

### 1. *Solitaire Game*

* **Tipo de tabuleiro:** tabuleiro de dimensões arbitrárias, célula de partida no canto inferior esquerdo e célula de chegada no canto superior direito;
* **Tipo de peças:** células vazias, células bloqueadas e células visitadas; 
* **Regras de movimento:** o jodador tem de alternar entre segmentos horizontais e verticais, sendo que dois segmentos consecutivos não podem ter o mesmo tamanho;
* **Condições para terminar jogo derrotado:** ser impossível de resolver, no sentido de não existir nenhum caminho possível que esteja de acordo com as regras do jogo;  
* **Condições para terminar jogo com vitória:** chegar à célula do campo superior direito do tabuleiro, sendo que todas as células do tabuleiro que não eram bloqueadas foram visitadas e que com esse movimento final os seguementos consecutivos não ficaram com igual tamanho;  
* **Score:** (in the event of a win, a score can be awarded depending on the number of moves, resources spent, bonuses collected and/or time spent)  ->> TODO <<--
number of moves ?? how if it is unique or in case it isn't the number os segments??

### 2. Problema de Pesquisa

* **Representação do Estado :** Board(emptyCells + obstacleCells + visitedCells) + CurentCell(Row, Col, Dir, Length) + LastSegment(LastLenght)
    + emptyCell = 0
    + visitedCell = 1
    + obstacleCell = 9
    + Row ∈ [0, HEIGHT[   
    + Col ∈ [0, WIDTH[  
    + Dir = Up | Down | Left | Right   
    + Length ∈ [0, max(HEIGHT, WIDTH)[ 
    + LastLenght ∈ [0, max(HEIGHT, WIDTH)[

```
 +--------> Col
0|
1|
2|
 v
Row
```

* **Estado Inicial** Board(tabuleiro vazio + obstáculos + célula inicial visitada) + CurentCell(HEIGHT-1, 0, None, 0) + LastSegment(None)
* **Teste Objetivo:** Board(tabuleiro cheio + obstáculos) + CurentCell(0, WIDTH-1, Dir, Length) + LastSegment(LastLenght) + Length != LastLenght
* **Operadores:**

| Nomes       | Precondições                                          | Efeitos                                              | Custos |
| ----------- | ----------------------------------------------------- | ---------------------------------------------------- | ------ |
| Up          | Row > 0      <br> Dir = Up    <br> b[Row-1, Col] = 0 | Row-- <br> b[Row, Col] = 1 <br> Lenght++             | 1 | 
| Down        | Row < HEIGHT <br> Dir = Down  <br> b[Row+1, Col] = 0 | Row++ <br> b[Row, Col] = 1 <br> Lenght++             | 1 |
| Left        | Col > 0      <br> Dir = Left  <br> b[Row, Col-1] = 0 | Col-- <br> b[Row, Col] = 1 <br> Lenght++             | 1 |
| Right       | Col < WIDTH  <br> Dir = Right <br> b[Row, Col+1] = 0 | Col++ <br> b[Row, Col] = 1 <br> Lenght++             | 1 |
| SwapToUp    | Length != 0  <br> Length != LastLenght <br> Dir=Left ∨ Dir = Right      | Dir = Up    <br> LastLenght = Lenght <br> Lenght = 0 | 0 |
| SwapToDown  | Length != 0  <br> Length != LastLenght <br> Dir=Left ∨ Dir = Right      | Dir = Down  <br> LastLenght = Lenght <br> Lenght = 0 | 0 |
| SwapToLeft  | Length != 0  <br> Length != LastLenght <br> Dir=Up ∨ Dir = Down         | Dir = Left  <br> LastLenght = Lenght <br> Lenght = 0 | 0 |
| SwapToRight | Length != 0  <br> Length != LastLenght <br> Dir=Up ∨ Dir = Down         | Dir = Right <br> LastLenght = Lenght <br> Lenght = 0 | 0 |

* **Heurísticas/Funções de avaliação:** 
->> TODO <<--

## Implementação já realizada

* **Linguagem de Programação:** Python
* **Ambiente de Desenvolvimento**: Windows/Linux
* **Estruturas de Dados:** ->> TODO <<--
* etc

