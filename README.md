# minimaxConnect4

Developed an implementation of a depth-limited minimax algorithm with alpha-beta pruning for a Max Connect-4 game. 
The game is played on a 6x7 grid, with two players alternately placing their pieces on the board. 
The objective is to form a line of four consecutive pieces horizontally, vertically, or diagonally.

Algorithm Description

Minimax Algorithm: The minimax algorithm is a decision rule used for minimizing the possible loss in a worst-case scenario (maximizing the minimum payoff). 
In our implementation, the algorithm explores possible moves in the game tree up to a certain specified depth. 
Each node at this depth is evaluated using an evaluation function, which helps in deciding the best possible move.

Depth Limitation: To prevent exhaustive search and to limit the computation time, we introduced a depth limit. 
The algorithm only explores the game tree up to this depth. 
This approach balances the need for strategic depth with the practical limitations of computation.

Alpha-Beta Pruning: This technique is used to improve the efficiency of the minimax algorithm. 
It prunes branches of the game tree that don't need to be explored because they can't influence the final decision. 
This optimization reduces the number of nodes evaluated, thus speeding up the decision process.

Evaluation Function: The evaluation function is crucial in this setup. 
It assesses the board state's potential for leading to a win or loss. 
We designed this function to calculate the score based on the current state of the board and to give an advantage to states with more pieces on the board, which can lead to potential wins.

In the interactive mode, the game runs from the command line with the following arguments:

python maxconnect4 interactive [input file] [computer-next/human-next] [depth]

For example,

python maxconnect4 interactive input1.txt computer-next 7

One-move mode is to make it easy for programs to compete against each other and communicate
their moves to each other using text files. The one-move mode is invoked as follows:

python maxconnect4 one-move [input file] [output file] [depth]

For example,

python maxconnect4 one-move red next.txt green next.txt 5
