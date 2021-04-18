

def TicTacToe(game):

    for x in range(3):
        if (game[0][x] == game[1][x] == game[2][x]):
            print("player " + str(game[0][x]) + " won")
            return
        elif (game[x][0] == game[x][1] == game[x][2]):
            print("player " + str(game[x][0]) + " won")
            return


    if (game[0][0] == game[1][1] == game[2][2]):
        print("player " + str(game[0][0]) + " won")
        return
    if (game[2][0] == game[1][1] == game[0][2]):
        print("player " + str(game[2][0]) + " won")
        return

    print("Tie")
    return


game = [[1, 2, 0],
        [2, 1, 0],
        [2, 1, 1]]

TicTacToe(game)