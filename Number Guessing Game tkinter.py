#       NUMBER GUESSING GAME
#
# Devloped By:- Vikas Laxman Dongare
# Versin:- 1.0

import tkinter as tk
import tkinter.font as font
import random
#set number of guesses to particular number
no_of_guesses = 10

#set hovers effects to the buttons
def playButtonHoverOn(e):
    play_button['bg'] = '#c2ffdf'

def playButtonHoverOff(e):
    play_button['bg'] = 'SystemButtonFace'

def howToPlayButtonHoverOn(e):
    howToPlay_button['bg'] = '#c2ffdf'

def howToPlayButtonHoverOff(e):
    howToPlay_button['bg'] = 'SystemButtonFace'

def quitButtonHoverOn(e):
    quit_button['bg'] = '#c2ffdf'

def quitButtonHoverOff(e):
    quit_button['bg'] = 'SystemButtonFace'

def submitButtonHoverOn(e):
    submit_button['bg'] = '#c2ffdf'

def submitButtonHoverOff(e):
    submit_button['bg'] = 'SystemButtonFace'

def retryButtonHoverOn(e):
    retry_button['bg'] = '#c2ffdf'

def retryButtonHoverOff(e):
    retry_button['bg'] = 'SystemButtonFace'

def backButtonHoverOn(e):
    backButton['bg'] = '#c2ffdf'

def backButtonHoverOff(e):
    backButton['bg'] = 'SystemButtonFace'

#How to play buttons functionality is implemented in these function
def howToPlay():
    #to access backbutton outside the class variable is declared as the global
    global backButton

    #here two strings are created one is title and other is the instructions about the game.
    title_string = "HOW TO PLAY?"
    string = '''1) I will select one random number from 0-100.\n2) You have to just enter your guess.\n3) If your guess is correct then you will win the game.\nNote:- In the right bottom corner remaining chances are shown.'''

    #here new frame created to aquire new texts and buttons
    howToPlayFrame = tk.Frame(canvas, bg="white")
    howToPlayFrame.place(relheight = 0.5, relwidth = 0.8, relx = 0.1, rely = 0.4)

    #backbutton which lets user to get back to the menu is created and gave it some hover effects
    backButton = tk.Button(howToPlayFrame, text="Back", command=menu, relief="flat" , activebackground="light green", font=("Comic Sans MS", 12))
    backButton.pack(anchor='nw', side='left')
    backButton.bind('<Enter>', backButtonHoverOn)
    backButton.bind('<Leave>', backButtonHoverOff)

    #these labels displays the title and instructions to the user
    howToPlayTitleLabel = tk.Label(howToPlayFrame, text=title_string, bg='white', justify='center', font=menuButtonFont, pady=10)
    howToPlayTitleLabel.pack(anchor='n')
    
    howToPlayLabel = tk.Message(howToPlayFrame, text=string, bg='white', justify='center', font=("Comic Sans MS", 12), width=300)
    howToPlayLabel.pack(ipady=10)
    
#this function returns message at particular condition of user's guess
def game_message(string, random_number):   
    try:
        user_guess = int(string)
    except:
        return  "!!! Wrong input, you lost one guess !!!"
    if(user_guess == random_number):
        msg="!!! Congratulations, Your guess is correct !!!"  
    elif(abs(user_guess-random_number)<=5):
        msg="!!! You are too close to number !!!"
    elif(abs(user_guess-random_number)<=10):
        msg="!!! You are close to number !!!"
    elif(abs(user_guess-random_number)<=30):
        msg="!!! You are far to number !!!"
    else:
        msg="!!! You are to far to number !!!"
    return msg

#play function is contains main structure and logic of the game
def play():
    #set variables to global so that it can be accessed from anywhere
    global count
    global submit_button
    count=0

    #creates main frame in the canvas which performs all the action of the game
    gameFrame = tk.Frame(canvas, bg="white")
    gameFrame.place(relheight = 0.5, relwidth = 0.8, relx = 0.1, rely = 0.4)

    entry_string = "I have selected a number,\nCan you guess it?"
    #selects random number to be guessed
    random_number = random.randint(0,100)

    #displays message to the
    entry_msg = tk.Message(gameFrame, text=entry_string, bg="White", justify="center", width=250, pady=15)
    entry_msg['font'] = entryTextFont
    entry_msg.pack()

    #display the string to identify which action to be performed
    input_string = "Enter Guess:"
    input_msg = tk.Message(gameFrame, text=input_string, bg="White", justify="center", font=entryTextFont, width=250)
    input_msg.pack()

    #get user input through Entry 
    user_in = tk.Entry(gameFrame, text="Enter", font=('Arial', 14), justify="center", relief='flat')
    user_in.pack()
    user_in.focus_set()

    #created label so that give user a hint
    msg1 = tk.Label(gameFrame, text="", bg="White", justify="center", pady= 20, font=('Arial', 13))
    msg1.pack()

    #displays remaining guesses to the user
    count_label = tk.Label(gameFrame, text="Remaining Guess: "+str(no_of_guesses), justify="center", bg="white")
    count_label.pack(anchor='se')
    
    def printtext():
        global count
        global msg

        #returns the string which user has put in the Entry
        string = user_in.get()

        #count is used so that determine remaining guesses
        count = count + 1

        #wipes out previos user input
        user_in.delete(0,tk.END)

        #in these line previous hint is changed to the new hint
        msg1.config(text=game_message(string, random_number))
        
        #in below line new remaining guess is updated
        count_label.config(text="Remaining Guess: "+str(no_of_guesses-count))

        v=game_message(string, random_number)
        
        #here condition is checked weather user got correct guess or number of guesses are over
        #if user got correct guess then two strings are passed to the retry function so that two labels are created
        #similarily, if user uses all chances of guesses then return another two strings for same purpose.
        if (v == "!!! Congratulations, Your guess is correct !!!"): 
            string="!!! CONGRATULATIONS !!!"
            string1="!!! Your Guess Is Correct !!!"
            retry(string, string1)
        if (count>=no_of_guesses):
            string="!!! SORRY !!!"
            string1="!!! You Number of Guesses are Over !!!"
            retry(string, string1)

    #submit button is created in game frame and hover effects are binded to that button
    submit_button = tk.Button(gameFrame, text = "Submit", command=printtext, width=60, font=buttonFont)
    submit_button.pack(side='bottom')
    submit_button.bind("<Enter>", submitButtonHoverOn)
    submit_button.bind("<Leave>", submitButtonHoverOff)
    
    def retry(string, string1):
        global retry_button
        global quit_button
        #all the message, button and other things are disabled so that new things to be created
        entry_msg.pack_forget()
        input_msg.pack_forget()
        user_in.pack_forget()
        msg1.pack_forget()
        submit_button.pack_forget()

        #two strings which are passed from printtext function are displayed in the following function
        congo_msg = tk.Label(gameFrame, text=string, bg="white", justify="center", pady=30, font=('Arial', 20, "bold"))
        congo_msg.pack()
        congo_msg1 = tk.Label(gameFrame, text=string1, bg="white", justify="center", font=('Arial', 15))
        congo_msg1.pack()

        #two buttons are created for try again and quit the game
        retry_button = tk.Button(gameFrame, text = "Try Again!", command=play, font=buttonFont, width=18)
        retry_button.pack(side='left', anchor='sw')
        retry_button.bind("<Enter>", retryButtonHoverOn)
        retry_button.bind("<Leave>", retryButtonHoverOff)
        quit_button = tk.Button(gameFrame, text = "Quit", command=root.destroy, font=buttonFont, width=30)
        quit_button.pack(side='left', anchor='se')
        quit_button.bind("<Enter>", quitButtonHoverOn)
        quit_button.bind("<Leave>", quitButtonHoverOff)

root = tk.Tk(className="Game")
#all basic functionalities are defined here such as title text and font style for various texts and buttons
title = "Number Guessing Game"
titlefont = font.Font(family='Comic Sans MS', size=30, weight='bold')
entryTextFont = font.Font(family="Helvetica", size=15, weight="bold")
menuButtonFont = font.Font(family="Comic Sans MS", size=20)
buttonFont = font.Font(family="Courier New", size=14)
endFont = font.Font(family="MS Sans Serif", size=10, weight="bold")

#created one canvas to play game
canvas = tk.Canvas(root, bg="light Green", height= 500, width=500)
canvas.pack()

#created frame to display title
frame = tk.Frame(canvas, bg="#484d4b")
frame.place(relheight = 0.17, relwidth = 1, relx = 0, rely = 0.12)

#to display game title below message field is created
msg = tk.Message(frame, text=title, fg="#b0f3ff", bg="#484d4b", justify="center", pady=15, width=500)
msg['font'] = titlefont
msg.pack()

#menu function created to hold the structure of menu
def menu():
    global play_button
    global howToPlay_button
    global quit_button
    
    #in these gamePlayFrame all the buttons and messages are shown
    gamePlayFrame = tk.Frame(canvas, bg="light Green")
    gamePlayFrame.place(relheight = 0.5, relwidth = 0.8, relx = 0.1, rely = 0.4) 

    #here play button which starts the game is created and binded to hover effect
    play_button = tk.Button(gamePlayFrame, text="Play!", command=play, font=menuButtonFont, pady=1, width=41, relief="flat" , activebackground="light green")
    play_button.pack()
    play_button.bind("<Enter>", playButtonHoverOn)
    play_button.bind("<Leave>", playButtonHoverOff)

    #here how to play button which gives the details about game to the user is created and binded to hover effect
    howToPlay_button = tk.Button(gamePlayFrame, text="How To Play?", command=howToPlay, font=menuButtonFont, pady=1, width=41, relief="flat" , activebackground="light green")
    howToPlay_button.pack()
    howToPlay_button.bind("<Enter>", howToPlayButtonHoverOn)
    howToPlay_button.bind("<Leave>", howToPlayButtonHoverOff)

    #here quit button which exits the game is created and binded to hover effect
    quit_button = tk.Button(gamePlayFrame, text="Quit", command=root.destroy, font=menuButtonFont, pady=1, width=41, relief="flat" , activebackground="light green")
    quit_button.pack()
    quit_button.bind("<Enter>", quitButtonHoverOn)
    quit_button.bind("<Leave>", quitButtonHoverOff)

    #these frame consists of my name and lies at bottom of the canvas
    end_frame = tk.Frame(canvas, bg='#ecc2ff')
    end_frame.place(relheight=0.07, relwidth=1, relx=0, rely=0.93)
    end_text = tk.Message(end_frame, text="Developed By:- Vikas Laxman Dongare", font=endFont, justify='center', bg='#ecc2ff', width=500, pady=10)
    end_text.pack(anchor='center')

menu()
root.mainloop()
