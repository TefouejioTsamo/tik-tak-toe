from tkinter import *
import random


def next_turn(row, column):
    global player

    if but[row][column]['text'] == ""  and check_winner() is False:
        if player == players[0]:
            but[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=f"player {players[1]}'s turns")
            elif check_winner() is True:
                label.config(text=f"player {players[0]} wins")
            elif check_winner() == "tie":
                label.config(text="tie")
        else:
            but[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=f"player {players[0]}'s turns")
            elif check_winner() is True:
                label.config(text=f"player {players[1]} wins")
            elif check_winner() == "tie":
                label.config(text="Tie!")

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
           if but[row][column]['text'] != "":
               spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def restartgame():
    global player

    player = random.choice(players)
    label.config(text=f"player {player}'s turn")

    for row in range(3):
        for column in range(3):
            but[row][column].config(text="", bg="#f0f0f0")



def check_winner():
    for row in range(3):
        if but[row][0]['text'] == but[row][1]['text'] == but[row][2]['text'] != "":
            but[row][0].config(bg="green")
            but[row][1].config(bg="green")
            but[row][2].config(bg="green")
            return True
    for column in range(3):
        if but[0][column]['text'] == but[1][column]['text'] == but[2][column]['text'] != "":
            but[0][column].config(bg="green")
            but[1][column].config(bg="green")
            but[2][column].config(bg="green")
            return True
    if but[0][0]['text'] == but[1][1]['text'] == but[2][2]['text'] != "":
        but[0][0].config(bg="green")
        but[1][1].config(bg="green")
        but[2][2].config(bg="green")
        return True
    elif but[0][2]['text'] == but[1][1]['text'] == but[2][0]['text'] != "":
        but[0][2].config(bg="green")
        but[1][1].config(bg="green")
        but[2][0].config(bg="green")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                but[row][column].config(bg="red")
        return "tie"
    else:
        return False

window = Tk()
window.geometry("500x650")
window.resizable(False, False)

players = ["X","O"]
player = random.choice(players)
but = [[0,0,0],
       [0,0,0],
       [0,0,0]]


label = Label(window, text=f"player {player}'s turn", bg="white", font=("consolas", 20), width=500)
label.pack()

button = Button(window, text="Restart",font=("consolas", 20),width=10, height=1,  command = restartgame)
button.pack()

Label(window, width=500, height=2).pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        but[row][column] = Button(frame, text="", width=5, height=2,
                                  font=("consolas", 40),
                                  command=lambda row=row, column=column: next_turn(row, column))
        but[row][column].grid(row=row, column=column)



Label(window, width=500, height=2).pack()

window.mainloop()
