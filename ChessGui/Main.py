import tkinter as tk
from PIL import ImageTk, Image
import time
import copy
root = tk.Tk()

B_SQUARE = Image.open("ChessGui/grnSquare_64.png")
W_SQUARE = Image.open("ChessGui/whtSquare_64.png")
B_BISHOP = Image.open("ChessGui/b_bishop.png")
B_KING = Image.open("ChessGui/b_king.png")
B_KNIGHT = Image.open("ChessGui/b_knight.png")
B_PAWN = Image.open("ChessGui/b_pawn.png")
B_QUEEN = Image.open("ChessGui/b_queen.png")
B_ROOK = Image.open("ChessGui/b_rook.png")
W_BISHOP = Image.open("ChessGui/w_bishop.png")
W_KING = Image.open("ChessGui/w_king.png")
W_KNIGHT = Image.open("ChessGui/w_knight.png")
W_PAWN = Image.open("ChessGui/w_pawn.png")
W_QUEEN = Image.open("ChessGui/w_queen.png")
W_ROOK = Image.open("ChessGui/w_rook.png")

chessFrame = tk.Frame(root)
chessFrame.pack()

buttonFrame = tk.Frame(root)
buttonFrame.pack(side = tk.BOTTOM)

#a 2d array that has a 1 if it is a black square and 0 if white
boardSquares = [[0 for i in range(8)] for j in range(8)]

#for populating boardSquares
for row in range(8):
    tempCheck = (row + 1) % 2 == 0
    for column in range(8):
        if tempCheck:
            if (column+1) % 2 == 0:
                boardSquares[row][column] = 1
            else:
                boardSquares[row][column] = 0
        else:
            if (column+1) % 2 != 0:
                boardSquares[row][column] = 1
            else:
                boardSquares[row][column] = 0

def ButtonClick():
    MovePiece(7,1,5,0, W_KNIGHT)
    #print("button was clicked")
    #tk.messagebox.showinfo("Test")
    
def MovePiece(fromRow, fromColumn, toRow, toColumn, chessPiece):
    PopualteBoardArea(fromRow, fromColumn, 'none')
    PopualteBoardArea(toRow, toColumn, chessPiece)

def PopualteBoardArea(row, column, chessPiece):
    sqr = copy.copy(B_SQUARE) if boardSquares[row][column] == 1 else copy.copy(W_SQUARE)
    if chessPiece == 'none':
        img = ImageTk.PhotoImage(sqr)
        temp = tk.Label(chessFrame, image = img )
        temp.image = img
        temp.grid(row = row, column = column)
    else:
        sqr.paste(chessPiece, (0,0), chessPiece)
        img = ImageTk.PhotoImage(sqr)
        temp = tk.Label(chessFrame, image = img )
        temp.image = img
        temp.grid(row = row, column = column)

def InitializeBoard():
    for row in range(8):
        for column in range(8):
            if row == 6:
                PopualteBoardArea(row, column, W_PAWN)
            elif row == 1:
                PopualteBoardArea(row, column, B_PAWN)
            else:
                PopualteBoardArea(row, column, 'none')
    PopualteBoardArea(0, 0, B_ROOK)
    PopualteBoardArea(0, 1, B_KNIGHT)
    PopualteBoardArea(0, 2, B_BISHOP)
    PopualteBoardArea(0, 3, B_KING)
    PopualteBoardArea(0, 4, B_QUEEN)
    PopualteBoardArea(0, 5, B_BISHOP)
    PopualteBoardArea(0, 6, B_KNIGHT)
    PopualteBoardArea(0, 7, B_ROOK)
    PopualteBoardArea(7, 0, W_ROOK)
    PopualteBoardArea(7, 1, W_KNIGHT)
    PopualteBoardArea(7, 2, W_BISHOP)
    PopualteBoardArea(7, 3, W_KING)
    PopualteBoardArea(7, 4, W_QUEEN)
    PopualteBoardArea(7, 5, W_BISHOP)
    PopualteBoardArea(7, 6, W_KNIGHT)
    PopualteBoardArea(7, 7, W_ROOK)

    #button for testing the movement function
    btn = tk.Button(buttonFrame, text="test Button", command = ButtonClick)
    btn.pack(side = tk.BOTTOM)

InitializeBoard()

root.mainloop()