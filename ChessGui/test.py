from ChessGui import ChessGui

GAME_FLAG = True

thing = ChessGui()
thing.InitializeBoard()

while GAME_FLAG:
    fromPos = input("From: ")
    toPos = input("To: ")
    if fromPos == 0:
        GAME_FLAG = False
    thing.MovePiece(fromPos, toPos)


hang = input("outside loop")