import tkinter as tk
import random

# GAME WINDOW
root = tk.Tk()  # Initialize Tkinter to create main window
root.title('Rock, Paper, Scissors - The Game')  # Set the title of the window
root.geometry('400x400')  # Sets the window width and height
root.resizable(False, False)  # Fix the size of the window
root.configure(bg='seashell3')  # Set the color of the background
tk.Label(root, text='Rock, Paper, Scissors', font=('Verdana', 30), bg="seashell2").pack()  # Set Window heading

# USER CHOICE
# String type variable that stores the choice that the user enters
user_take = tk.StringVar()
# Set user prompt
tk.Label(root, text='Choose one: rock, paper, scissors', font=('Verdana', 15, 'bold'), bg='seashell2').place(x=20, y=70)
# Create an input text field
tk.Entry(root, font=('Verdana', 15, 'bold'), textvariable=user_take, bg='seashell2').place(x=90, y=130)

Result = tk.StringVar()


# FUNCTION TO PLAY GAME
def play_game():
    # COMPUTER CHOICE
    # random.randint() function will randomly take any number from the given number.
    # Here we give the if-else() condition to play rock paper scissors
    # If the computer choose 1 then the rock will set to comp_pick variable
    # If the computer choose 2 then the paper will set to comp_pick variable
    # If the computer choose 3 then scissors will set to comp_pick variable
    comp_pick = random.choice([1, 2, 3])
    if comp_pick == 1:
        comp_pick = 'rock'
    elif comp_pick == 2:
        comp_pick = 'paper'
    else:
        comp_pick = 'scissors'

    user_pick = user_take.get()  # user_take is a string type variable that stores the choice that the user enters.
    if user_pick == comp_pick:  # We give if-else() condition to check who wins between user choice and computer choice.
        Result.set('Tie, you both selected the same.')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('You lose, computer selected paper.')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You win, computer selected scissors.')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('You lose, computer selected scissors.')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You win, computer selected rock.')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('You lose, computer selected rock.')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You win, computer selected paper.')
    else:
        Result.set('Invalid: choose either rock, paper or scissors.')


# Function for resetting the game
def reset_game():
    Result.set("")
    user_take.set("")


# Function for ending the game
def exit_game():
    root.destroy()  # root.destroy() will quit the rock paper scissors program by stopping the mainloop().


# Button() widget used when we want to display a button.
# command calls the specific function when the button is clicked.
tk.Entry(root, font=('Verdana', 10, 'bold'), textvariable=Result, width=50, ).place(x=25, y=250)
tk.Button(root, font=('Verdana', 13, 'bold'), text='PLAY', padx=5, command=play_game).place(x=150, y=190)
tk.Button(root, font=('Verdana', 13, 'bold'), text='RESET', padx=5, command=reset_game).place(x=70, y=310)
tk.Button(root, font=('Verdana', 13, 'bold'), text='EXIT', padx=5, command=exit_game).place(x=230, y=310)

# Method to run the program.
root.mainloop()
