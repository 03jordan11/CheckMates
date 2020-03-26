import tkinter as tk
from PIL import ImageTk, Image
import copy

class ChessGui:
    root = tk.Tk()

    B_SQUARE = Image.open("ChessGui/grnSquare_64.png")
    W_SQUARE = Image.open("ChessGui/whtSquare_64.png")

    B_PAWN = Image.open("ChessGui/b_pawn.png") #21
    B_ROOK = Image.open("ChessGui/b_rook.png") #22
    B_KNIGHT = Image.open("ChessGui/b_knight.png") #23
    B_BISHOP = Image.open("ChessGui/b_bishop.png")#24
    B_QUEEN = Image.open("ChessGui/b_queen.png")#25
    B_KING = Image.open("ChessGui/b_king.png")#26

    W_PAWN = Image.open("ChessGui/w_pawn.png") #11
    W_ROOK = Image.open("ChessGui/w_rook.png") #12
    W_KNIGHT = Image.open("ChessGui/w_knight.png") #13
    W_BISHOP = Image.open("ChessGui/w_bishop.png") #14
    W_QUEEN = Image.open("ChessGui/w_queen.png") #15
    W_KING = Image.open("ChessGui/w_king.png") #16

    chessFrame = tk.Frame(root)
    chessFrame.pack()

    buttonFrame = tk.Frame(root)
    buttonFrame.pack(side = tk.BOTTOM)

    #a 2d array that has a 1 if it is a black square and 0 if white
    boardSquares = [[0 for i in range(8)] for j in range(8)]
    gameState = [[0 for i in range(8)] for j in range(8)]

    #for populating boardSquares
    for row in range(8):
        tempCheck = (row + 1) % 2 == 0
        for column in range(8):
            if tempCheck:
                if (column+1) % 2 != 0:
                    boardSquares[row][column] = 1
                else:
                    boardSquares[row][column] = 0
            else:
                if (column+1) % 2 == 0:
                    boardSquares[row][column] = 1
                else:
                    boardSquares[row][column] = 0

    def PopulateStartingGameState(self):
        for i in range(8):
            self.gameState[1][i] = self.B_PAWN
            self.gameState[6][i] = self.W_PAWN

        #rooks
        self.gameState[0][0] = self.B_ROOK
        self.gameState[0][7] = self.B_ROOK
        self.gameState[7][0] = self.W_ROOK
        self.gameState[7][7] = self.W_ROOK

        #knights
        self.gameState[0][1] = self.B_KNIGHT
        self.gameState[0][6] = self.B_KNIGHT
        self.gameState[7][1] = self.W_KNIGHT
        self.gameState[7][6] = self.W_KNIGHT

        #bishops
        self.gameState[0][2] = self.B_BISHOP
        self.gameState[0][5] = self.B_BISHOP
        self.gameState[7][2] = self.W_BISHOP
        self.gameState[7][5] = self.W_BISHOP

        #queens
        self.gameState[0][3] = self.B_QUEEN
        self.gameState[7][3] = self.W_QUEEN

        #kings
        self.gameState[0][4] = self.B_KING
        self.gameState[7][4] = self.W_KING
        
    def ConvertPosition(self, position):
        row = 8 - int(position[1])
        col = 0
        if position[0] == 'a':
            col = 0
        if position[0] == 'b':
            col = 1
        if position[0] == 'c':
            col = 2
        if position[0] == 'd':
            col = 3
        if position[0] == 'e':
            col = 4
        if position[0] == 'f':
            col = 5
        if position[0] == 'g':
            col = 6
        if position[0] == 'h':
            col = 7
        return row, col

    def MovePiece(self, fromPos, toPos):
        fromRow, fromColum = self.ConvertPosition(fromPos)
        toRow, toColum = self.ConvertPosition(toPos)
        self.PopualteBoardArea(fromRow, fromColum, 'none')
        self.PopualteBoardArea(toRow, toColum, self.gameState[fromRow][fromColum])
        
        self.gameState[toRow][toColum] = self.gameState[fromRow][fromColum]
        self.gameState[fromRow][fromColum] = 0

    def PopualteBoardArea(self, row, column, chessPiece):
        sqr = copy.copy(self.B_SQUARE) if self.boardSquares[row][column] == 1 else copy.copy(self.W_SQUARE)
        if chessPiece == 'none':
            img = ImageTk.PhotoImage(sqr)
            temp = tk.Label(self.chessFrame, image = img )
            temp.image = img
            temp.grid(row = row, column = column)
        else:
            sqr.paste(chessPiece, (0,0), chessPiece)
            img = ImageTk.PhotoImage(sqr)
            temp = tk.Label(self.chessFrame, image = img )
            temp.image = img
            temp.grid(row = row, column = column)

    def InitializeBoard(self):
        for row in range(8):
            for column in range(8):
                if row == 6:
                    self.PopualteBoardArea(row, column, self.W_PAWN)
                elif row == 1:
                    self.PopualteBoardArea(row, column, self.B_PAWN)
                else:
                    self.PopualteBoardArea(row, column, 'none')
        self.PopualteBoardArea(0, 0, self.B_ROOK)
        self.PopualteBoardArea(0, 1, self.B_KNIGHT)
        self.PopualteBoardArea(0, 2, self.B_BISHOP)
        self.PopualteBoardArea(0, 3, self.B_KING)
        self.PopualteBoardArea(0, 4, self.B_QUEEN)
        self.PopualteBoardArea(0, 5, self.B_BISHOP)
        self.PopualteBoardArea(0, 6, self.B_KNIGHT)
        self.PopualteBoardArea(0, 7, self.B_ROOK)
        self.PopualteBoardArea(7, 0, self.W_ROOK)
        self.PopualteBoardArea(7, 1, self.W_KNIGHT)
        self.PopualteBoardArea(7, 2, self.W_BISHOP)
        self.PopualteBoardArea(7, 3, self.W_KING)
        self.PopualteBoardArea(7, 4, self.W_QUEEN)
        self.PopualteBoardArea(7, 5, self.W_BISHOP)
        self.PopualteBoardArea(7, 6, self.W_KNIGHT)
        self.PopualteBoardArea(7, 7, self.W_ROOK)

        #for creating the state of the game
        self.PopulateStartingGameState()

        #button for testing the movement function
        # btn = tk.Button(self.buttonFrame, text="test Button", command = self.ButtonClick)
        # btn.pack(side = tk.BOTTOM)
        #self.root.mainloop()
        

    