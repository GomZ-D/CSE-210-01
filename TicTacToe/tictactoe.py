def main ():
#All the calls for run the program
    print('WELCOME! HAVE FUN WITH TIC TAC TOE')
    numbers = [1,2,3,4,5,6,7,8,9]
    player = 'x'
    while not (winnerGame(numbers) or tieGame(numbers)):
        createGrid(numbers)
        choose = playerTurn(player)
       
        updateGrid(numbers,choose,player)
        win = player
        player = whosTurnIsIt(player)
    
    winner(win)
    print('Gracias por jugar')



def createGrid (numbers):
#draw the tictactoe board on the screen
    print()
    print (f'{numbers[0]}|{numbers[1]}|{numbers[2]}\
        \n-+-+-\n\
{numbers[3]}|{numbers[4]}|{numbers[5]}\
         \n-+-+-\n\
{numbers[6]}|{numbers[7]}|{numbers[8]}')
    print()


def playerTurn (player):
#logig for whos turn is it.
    choose = int(input(f"{player}'s turn to choose a square(1-9): "))
    return choose;

def updateGrid (board, choose,player):
    choose = choose-1
    board[choose] = player;


def whosTurnIsIt(player):
    
    if (player == 'x'):
        return 'o'
    elif (player == 'o'):
         return 'x'


def winnerGame (numbers):
#logic to win game - check that x or o are the same in row
# column or diagonal 
    return (numbers[0]==numbers[1]==numbers[2] or
            numbers[3]==numbers[4]==numbers[5] or
            numbers[6]==numbers[7]==numbers[8] or
            numbers[0]==numbers[7]==numbers[8] or
            numbers[2]==numbers[4]==numbers[6] or
            numbers[0]==numbers[3]==numbers[6] or
            numbers[1]==numbers[4]==numbers[7] or
            numbers[2]==numbers[5]==numbers[8])


def tieGame (numbers):
#logic for a tie game
    for number in range(9):
        if numbers[number] == 'x' and numbers[number] == 'o':
            return True
    return False

def winner (player):  
    if (player == 'x') :
        print('The winner is X!!!!!!!')
    elif(player == 'o'):
        print('The winner is O!!!!!!')
    else:
        print('Keep Trying :(')

if __name__ == '__main__':
    main()