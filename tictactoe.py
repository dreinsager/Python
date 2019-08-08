#Dispalys the tic tac toe board
def display_board(board):
    print('\n'*100)
    print(board[7]+'  |  '+board[8]+'|'+board[9])
    print('-----------')
    print(board[4]+'  |  '+board[5]+'|'+board[6])
    print('-----------')
    print(board[1]+'  |  '+board[2]+'|'+board[3])

#Takes in the players input to ask if X or O
def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choos X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

print('Welcome to Tic Tac Tow')

while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
