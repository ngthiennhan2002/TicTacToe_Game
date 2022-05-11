import tkinter as tk
from tkinter import *
import time
import threading

class GameTurn:
    def __init__(self):
        self.turn = 0
    def nextTurn(self):
        self.turn += 1
    def reset(self):
        self.turn = 0


class GameBoxButton:
    def __init__(self, CoRow, CoColumn):
        self.isLocked = True
        self.row = CoRow
        self.column = CoColumn
        self.text = ""
    def createGameboxButton(self):
        gameBoxButton = Button(root, command=lambda:ticked(gameBoxButton, self.row, self.column),  width=8, height=4, activebackground='Light salmon', fg='black', font=('Arial', 15))
        gameBoxButton.grid(row=self.row, column=self.column, sticky=E+W+N+S)
        gameBoxButton.config(state='disabled', bg='grey', text="-", disabledforeground='black')
        return gameBoxButton


def changeOnHover(button, colorOnHover, colorOnLeave): # Hàm thay đổi màu khi di chuột vào và ra khỏi button
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def resetTickMatrix(tickMatrix):
    for i in range(3):
        for j in range(3):
            tickMatrix[i][j] = '-'

def next():
    global nextButton, buttons
    gameTurn.reset()
    winLabel.config(text="")
    nextButton.config(state='disabled')
    resetTickMatrix(tickMatrix)
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(state='normal', text='')
            changeOnHover(buttons[i][j], 'DarkOliveGreen1', '#d9d9d9')


def checkWin(tickMatrix, nextButton):
    global winLabel, score, turn, buttons
    winLabel = Label(root, text="", fg='red', font=('Arial', 13, 'bold'))
    winLabel.place(x=300, y=40)
    for i in range(3):
        a = str(tickMatrix[i][0])
        b = str(tickMatrix[i][1])
        c = str(tickMatrix[i][2])
        if a == 'X' and b == 'X' and c == 'X':
            winLabel.config(text="You won!")
            score += 1
            scoreLabel.config(text="Score: " + str(score))
            resetTickMatrix(tickMatrix)
            nextButton.config(state='normal', command=next)
            changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
            return 0
        elif a == 'O' and b == 'O' and c == 'O':
            winLabel.config(text="You lost!")
            resetTickMatrix(tickMatrix)
            nextButton.config(state='normal', command=next)
            changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
            return 0
    for i in range(3):
        a = str(tickMatrix[0][i])
        b = str(tickMatrix[1][i])
        c = str(tickMatrix[2][i])
        if a == 'X' and b == 'X' and c == 'X':
            winLabel.config(text="You won!")
            resetTickMatrix(tickMatrix)
            score += 1
            scoreLabel.config(text="Score: " + str(score))
            nextButton.config(state='normal', command=next)
            changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
            return 0
        elif a == 'O' and b == 'O' and c == 'O':
            winLabel.config(text="You lost!")
            resetTickMatrix(tickMatrix)
            nextButton.config(state='normal', command=next)
            changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
            return 0
    a = str(tickMatrix[0][0])
    b = str(tickMatrix[1][1])
    c = str(tickMatrix[2][2])
    if a == 'X' and b == 'X' and c == 'X':
        winLabel.config(text="You won!")
        score += 1
        scoreLabel.config(text="Score: " + str(score))
        resetTickMatrix(tickMatrix)
        nextButton.config(state='normal', command=next)
        changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
        return 0
    elif a == 'O' and b == 'O' and c == 'O':
        winLabel.config(text="You lost!")
        resetTickMatrix(tickMatrix)
        nextButton.config(state='normal', command=next)
        changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
        return 0
    a = str(tickMatrix[0][2])
    b = str(tickMatrix[1][1])
    c = str(tickMatrix[2][0])
    if a == 'X' and b == 'X' and c == 'X':
        winLabel.config(text="You won!")
        score += 1
        scoreLabel.config(text="Score: "+str(score))
        resetTickMatrix(tickMatrix)
        nextButton.config(state='normal', command=next)
        changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
        return 0
    elif a == 'O' and b == 'O' and c == 'O':
        winLabel.config(text="You lost!")
        resetTickMatrix(tickMatrix)
        nextButton.config(state='normal', command=next)
        changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
        return 0
    if gameTurn.turn >= 8:
        winLabel.config(text="Draw!")
        resetTickMatrix(tickMatrix)
        nextButton.config(state='normal', command=next)
        changeOnHover(nextButton, 'DarkOliveGreen1', 'SystemButtonFace')
        return 0


def ticked(gameBoxButton, row, column):
    text = ""
    if gameTurn.turn % 2 == 0:
        gameBoxButton.text = "X"
        text = gameBoxButton.text
        gameBoxButton.config(state='disabled', text=gameBoxButton.text, disabledforeground='red')
    else:
        gameBoxButton.text = "O"
        text = gameBoxButton.text
        gameBoxButton.config(state='disabled', text=gameBoxButton.text, disabledforeground='blue')
    changeOnHover(gameBoxButton, '#d9d9d9', '#d9d9d9')
    tickMatrix[row-1][column] = text
    checkWin(tickMatrix, nextButton)
    gameTurn.nextTurn()


def gamepad():
    global score
    score = 0
    emptyLabel = Label(root, text="   ")
    emptyLabel.grid(row=0, column=0)
    global scoreLabel
    scoreLabel = tk.Label(root, text="Score: 0", fg='red', font=('Arial', 15, 'bold'))
    scoreLabel.grid(row=0, column=1)
    scoreLabel.config(height=3)
    instruction_label = tk.Label(root, text="You: X\nOpponent: O", fg='red', font=('Arial', 12, 'bold'))
    instruction_label.place(x=300, y=300)
    global buttons
    global tickMatrix
    buttons = [[], [], []]
    tickMatrix = [[], [], []]
    for i in range(3):
        for j in range(3):
            gameboxButton = GameBoxButton(i+1, j).createGameboxButton()
            buttons[i].append(gameboxButton)
            tickMatrix[i].append("-")

def nextButton():
    global nextButton
    nextButton = Button(root, state='disabled', activebackground='Light salmon', text='Next',
                        font=('Arial', 13, 'bold'))
    nextButton.grid(row=1, column=4)

def playButton():
    def click_to_start():
        playButton.config(text="Reset", command=click_to_stop)
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state='normal', bg='#d9d9d9', text='')
                changeOnHover(buttons[i][j], 'DarkOliveGreen1', '#d9d9d9')
                buttons[i][j].isLocked = False
    def click_to_stop():
        playButton.config(text="Start", command=click_to_start)
        gameTurn.reset()
        winLabel.config(text="")
        global nextButton, score
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state='disabled', bg='grey', text='-', disabledforeground='black')
                buttons[i][j].isLocked = True
                changeOnHover(buttons[i][j], 'grey', 'grey')
                score = 0
                scoreLabel.config(text="Score: " + str(score))
                resetTickMatrix(tickMatrix)
                nextButton.config(state='disabled')
    emptyLabel = Label(root, text="      ")
    emptyLabel.grid(row=1, column=3)
    nextButton()
    playButton = Button(root, command=click_to_start, activebackground='Light salmon', text='Start', font=('Arial', 13, 'bold'))
    playButton.grid(row=2, column=4)
    changeOnHover(playButton, 'DarkOliveGreen1', 'SystemButtonFace')


def callFunctions():
    gamepad()
    playButton()


def main():
    global gameTurn
    gameTurn = GameTurn()
    global root
    root = tk.Tk()
    root.geometry('410x400')
    root.title("Tic Tac Toe")
    root.resizable(False, False)
    callFunctions()
    root.mainloop()

main()