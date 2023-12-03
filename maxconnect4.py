#!/usr/bin/env python
"""
Copyright (C) 2016 Chris Conly (chris.conly@uta.edu)

"""
import sys
from MaxConnect4Game import *


def oneMoveGame(currentGame, depth):
    # Check if board is full
    if currentGame.pieceCount == 42:
        print('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)  # Exit if full

    currentGame.aiPlay(depth)  # AI plays

    print('Game state after move:')
    currentGame.printGameBoard()  # Printing board

    currentGame.countScore()  # Updating score based on current board state
    print('Score: Player 1 = %d, Player 2 = %d\n' %
          (currentGame.player1Score, currentGame.player2Score))

    # Switch the current turn to the other player
    currentGame.currentTurn = 1 if currentGame.currentTurn == 2 else 2

    currentGame.printGameBoardToFile()  # Save board state to output file
    currentGame.gameFile.close()  # Close game file


def interactiveGame(currentGame, next_player, depth):
    while not currentGame.is_game_over():
        # Step 2: Print the current board state and score
        currentGame.printGameBoard()
        currentGame.countScore()
        print('Score: Player 1 = %d, Player 2 = %d\n' %
              (currentGame.player1Score, currentGame.player2Score))

        if currentGame.pieceCount == 42:
            print('BOARD FULL\n\nGame Over!\n')
            break

        if next_player == 'computer-next':
            # Step 3: Computer makes the next move
            currentGame.aiPlay(depth)

            # Step 4: Save the current board state in a file called computer.txt
            with open('computer.txt', 'w') as file:
                currentGame.gameFile = file
                currentGame.printGameBoardToFile()

            next_player = 'human-next'
        else:  # Human's turn
            # Step 6: Ask the human to make a move
            column = int(input(
                "Enter the column number (0-6) where you would like to place your piece: "))
            while not currentGame.playPiece(column):
                print("Invalid move. The column is full or does not exist.")
                column = int(
                    input("Enter a column number (0-6) where you would like to place your piece: "))

            # Step 7: Save the current board state in a file called human.txt
            with open('human.txt', 'w') as file:
                currentGame.gameFile = file
                currentGame.printGameBoardToFile()

            next_player = 'computer-next'

        currentGame.currentTurn = 1 if currentGame.currentTurn == 2 else 2


def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print('Four command-line arguments are needed:')
        print(
            'Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile, next_player, depth_str = argv[1:5]
    depth = int(depth_str)

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game()  # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Set currentTurn based on the next_player command line argument
    if next_player == 'computer-next':
        currentGame.currentTurn = 2
    elif next_player == 'human-next':
        currentGame.currentTurn = 1

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]]
                             for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' %
          (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        # Be sure to pass whatever else you need from the command line
        interactiveGame(currentGame, next_player, depth)
    else:  # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        # Be sure to pass any other arguments from the command line you might need.
        oneMoveGame(currentGame, depth)


if __name__ == '__main__':
    main(sys.argv)
