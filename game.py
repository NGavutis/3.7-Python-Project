### Modules ###
import random #Imports the random module for use when picking numbers from list
import csv #Imports the csv module for handling the file that stores the high scores
from tkinter import * #Imports the tkinter module for the GUI
###

### Global Variables ###
windowWidth = 1000 #Sets the width of the window
windowHeight = 700 #Sets the height of the window
bgColour = "orange" #Sets the background colour
fgColour = "white" #Sets the foreground colour
###

class MainMenu: #Main menu class

    ### Menu UI ###
    def __init__(self,window,c): #Initializing function
        ### Variables ###
        c.delete(ALL) #Deletes all elements off the canvas
        self.window = window #Allows window to be used in this class
        self.c = c #Allows canvas to be used in this class
        windowWidthHalf = windowWidth/2 #Sets up variable
        windowHeightHalf = windowHeight/2 #Sets up variable
        bottomButtonWidthHalf = (windowWidthHalf-125)/2 #For putting text in the middle of a button (only for the main menu screen)
        fontSize = 40 #Sets up variable
        c.tag_bind("easy","<Button-1>",self.easy) #Binds left click to the "Easy" button and runs corresponding function
        c.tag_bind("medium","<Button-1>",self.medium) #Binds left click to the "Medium" button and runs corresponding function
        c.tag_bind("hard","<Button-1>",self.hard) #Binds left click to the "Hard" button and runs corresponding function
        c.tag_bind("score","<Button-1>",self.score) #Binds left click to the "Score" button and runs corresponding function
        c.tag_bind("quit","<Button-1>",self.end) #Binds left click to the "Quit" button and runs corresponding function
        ###

        ### Title ###
        c.create_rectangle(100,50,windowWidth-100,150,
                           fill = fgColour,
                           outline = fgColour) #Creates a rectangle
        c.create_text(windowWidthHalf,100,
                      anchor = CENTER,
                      font = ("Arial",fontSize,"bold"),
                      fill = bgColour,
                      text = "Basic Facts Tester") #Creates text
        ###

        ### Options ###
        c.create_rectangle(100,200,windowWidth-100,windowHeight-200,
                           fill = fgColour,
                           outline = fgColour) #Creates a rectangle
        c.create_text(125,windowHeightHalf-75,
                      anchor = W,
                      font = ("Arial",fontSize,"bold"),
                      fill = bgColour,
                      text = "Easy",
                      tags = "easy") #Creates text
        c.create_text(125,windowHeightHalf,
                      anchor = W,
                      font = ("Arial",fontSize,"bold"),
                      fill = bgColour,
                      text = "Medium",
                      tags = "medium") #Creates text
        c.create_text(125,windowHeightHalf+75,
                      anchor = W,
                      font = ("Arial",fontSize,"bold"),
                      fill = bgColour,
                      text = "Hard",
                      tags = "hard") #Creates text
        ###

        ### Score ###
        c.create_rectangle(100,windowHeight-150,windowWidthHalf-25,windowHeight-50,
                           fill = fgColour,
                           outline = fgColour,
                           tags = "score") #Creates a rectangle
        c.create_text(bottomButtonWidthHalf+100,windowHeight-100,
                      anchor = CENTER,
                      font = ("Arial",fontSize,"bold"),
                      fill = bgColour,
                      text = "Score",
                      tags = "score") #Creates text
        ###

        ### Quit ###
        c.create_rectangle(windowWidthHalf+25,windowHeight-150,windowWidth-100,windowHeight-50,
                           fill = fgColour,
                           outline = fgColour,
                           tags = "quit") #Creates a rectangle
        c.create_text(windowWidthHalf+25+bottomButtonWidthHalf,windowHeight-100,
                      anchor = CENTER,
                      font = ("Arial",fontSize,"bold"),
                      fill = bgColour,
                      text = "Quit",
                      tags = "quit") #Creates text
        ###

    ### Easy Mode Button Function ###
    def easy(self,*args):
        game = Game(self.window,self.c,"easy") #Creates "Game" object and gives it "easy"
    ###

    ### Medium Mode Button Function ###
    def medium(self,*args):
        game = Game(self.window,self.c,"medium") #Creates "Game" object and gives it "medium"
    ###

    ### Hard Mode Button Function ###
    def hard(self,*args):
        game = Game(self.window,self.c,"hard") #Creates "Game" object and gives it "hard"
    ###

    ### Score Button Function ###
    def score(self,*args):
        score = Score(self.window,self.c) #Creates "Score" object
    ###

    ### Quit Button Funtion ###        
    def end(self,*args):
        self.window.destroy() #Closes window
        exit() #Closes shell
    ###

class Game: #Game class

    ### Game UI
    def __init__(self,window,c,difficulty): #Initializing function
        ### Variables ###
        self.window = window #Allows window to be used in this class
        self.c = c #Allows canvas to be used in this class
        self.fontSize = 40 #Sets up variable
        self.difficulty = difficulty #Sets up variable
        self.timer = 60 #Sets up variable
        self.stopCount = 0 #Sets up variable
        self.stopGame = 0 #Sets up variable
        self.score = 0 #Sets up variable
        self.incorrect = 0 #Sets up variable
        c.focus_set() #Focuses on window for keyboard events
        c.bind("<space>",self.start) #Binds spacebar to corresponding function
        c.tag_bind("menu","<Button-1>",self.menu) #Binds left click to corresponding function
        ###
        
        ### Set Difficulty ###
        if self.difficulty == "easy":
            self.numbers = (1,2,3,5,10) #Sets up variable
        elif self.difficulty == "medium":
            self.numbers = (1,2,3,4,5,6,7,8,9,10,11,12)#Sets up variable
        elif self.difficulty == "hard":
            self.numbers = (1,2,3,4,5,6,7,8,9,10,11,12,25,50,100)#Sets up variable
        ###
            
        ### Background Elements ###
        c.delete(ALL) #Deletes all elements off the canvas
        c.create_rectangle(100,50,windowWidth-100,windowHeight-50,
                           fill = fgColour,
                           outline = fgColour) #Creates a rectangle
        c.create_rectangle(150,100,windowWidth-150,300,
                           fill = bgColour,
                           outline = bgColour) #Creates text
        ###
        
        ### Start Text ###
        self.startText = c.create_text(200,200,
                                       anchor = W,
                                       font = ("Arial",self.fontSize,"bold"),
                                       fill = fgColour,
                                       text = "Press Space To Start",) #Creates text
        ###
        
        ### Menu Button ###
        c.create_text(150,350,
                      anchor = W,
                      font = ("Arial",self.fontSize,"bold"),
                      fill = bgColour,
                      text = "Menu",
                      tags = "menu") #Creates text
        ###
    ###
        
    ### Game Start ###
    def start(self,*args):
        ### Delete Start Text ###
        self.c.itemconfigure(self.startText,text = "") #Changes text for "startText"
        ###

        ### Answer Box ###
        self.answer = Entry(bg = bgColour,
                            bd = 0,
                            highlightthickness=0,
                            font = ("Arial",self.fontSize,"bold"),
                            fg = fgColour) #Creates an entry box to input answers
        self.answer.place(x = 150,
                          y = windowHeight-200,
                          width = windowWidth-300,
                          height = 100) #Places entry box in a certain position
        self.answer.bind("<Return>",self.checkAnswer) #Binds enter to corresponding function
        ###

        ### Timer ###
        self.timerText = self.c.create_text(windowWidth/2,350,
                                            anchor = CENTER,
                                            font = ("Arial",self.fontSize,"bold"),
                                            fill = bgColour,
                                            text = ("Time:",self.timer)) #Creates text
        ###

        ### User Score ###
        self.userScore = self.c.create_text(windowWidth-150,350,
                                            anchor = E,
                                            font = ("Arial",self.fontSize,"bold"),
                                            fill = bgColour,
                                            text = ("Score:",self.score)) #Creates text
        ###

        self.stopGame = 1 #Sets variable to 1
        self.count() #Runs function
        self.question() #Runs function
    ###

    ### Timer ###
    def count(self):
        if self.timer >= 0:
            if self.stopCount == 1:
                return #Stops counter if stopCount is 1
            elif self.timer == 0:
                self.gameEnd() #Runs function if timer is at 0
            self.c.itemconfigure(self.timerText,text = ("Time:",self.timer)) #Changes text for "timerText" to the current time
            self.c.after(1000,self.count) #Makes canvas wait 1 second
            self.timer -= 1 #Takes one off the timer
    ###

    ### Generate Question ###  
    def question(self):
        self.a = random.choice(self.numbers) #Picks one random number from list
        self.b = random.choice(self.numbers) #Picks another random number from list
        self.c.itemconfigure(self.startText,text = (self.a,"x",self.b)) #Changes text for "startText" to show the two numbers picked
        self.answer.focus() #Focuses the input on the answer box
    ###

    ### Answer Checker ###
    def checkAnswer(self,event=None):
        try:
            userAnswer = int(self.answer.get())
            if userAnswer == (self.a*self.b):
                self.score += 1
                self.c.itemconfigure(self.userScore,text = ("Score:",self.score))
            else:
                self.incorrect += 1
            self.answer.delete(0,'end')
        except ValueError:
            self.answer.delete(0,'end')
        self.question()
    ###

    ### Game Over Screen ###
    def gameEnd(self):
        ### Screen Clear ###
        self.c.delete(ALL)
        self.answer.destroy()
        ###

        ### Name Box ###
        self.name = Entry(bg = bgColour,
                          bd = 0,
                          highlightthickness=0,
                          font = ("Arial",self.fontSize,"bold"),
                          fg = fgColour)
        self.name.place(x = 150,
                        y = windowHeight-200,
                        width = windowWidth-300,
                        height = 100)
        self.name.bind("<Return>",self.userInfo)
        self.name.focus()
        ###

        ### Final Stats ###
        self.c.create_rectangle(100,50,windowWidth-100,windowHeight-50,
                                fill = fgColour,
                                outline = fgColour)
        self.c.create_text(windowWidth/2,150,
                           anchor = CENTER,
                           font = ("Arial",self.fontSize,"bold"),
                           fill = bgColour,
                           text = ("Your Score: "+str(self.score)))
        self.c.create_text(windowWidth/2,250,
                           anchor = CENTER,
                           font = ("Arial",self.fontSize,"bold"),
                           fill = bgColour,
                           text = ("Incorrect: "+str(self.incorrect)))
        self.c.create_text(windowWidth/2,350,
                           anchor = CENTER,
                           font = ("Arial",self.fontSize,"bold"),
                           fill = bgColour,
                           text = ("Enter Name:"))
        ###
    ###

    ### Save User Data ###
    def userInfo(self,*args):
        self.userName = self.name.get()
        self.name.destroy()
        ### Write To File ###
        userData = [self.userName,self.difficulty,self.score]
        with open('highScore.csv','a',newline="") as f:
            writer = csv.writer(f)
            writer.writerow(userData)
        score = Score(self.window,self.c)
        ###
    ###

    ### Menu Button Function ###
    def menu(self,*args):
        self.stopCount = 1
        mainMenu = MainMenu(self.window,self.c)
        if self.stopGame == 1:
            self.answer.destroy()
    ###

class Score: #Score class

    ### Score UI ###
    def __init__(self,window,c): #Initializing function
        ### Variables ###
        self.window = window
        self.c = c
        self.fontSize = 40
        c.tag_bind("menu","<Button-1>",self.menu)
        ###
        
        ### Background ###
        c.delete(ALL)
        c.create_rectangle(100,50,windowWidth-100,windowHeight-50,
                           fill = fgColour,
                           outline = fgColour)
        c.create_rectangle(150,100,windowWidth-150,windowHeight-150,
                           fill = bgColour,
                           outline = bgColour)
        ###
        
        ### Menu Button ###
        c.create_text(150,windowHeight-100,
                      anchor = W,
                      font = ("Arial",self.fontSize,"bold"),
                      fill = bgColour,
                      text = "Menu",
                      tags = "menu")
        ###
        
        self.score()
    ###
        
    ### Show Scores ###
    def score(self):
        fontSize = 15
        ### Open and Read File ###
        with open('highScore.csv', 'r') as f:
            reader = csv.reader(f)
            highScore = [row for row in reader if len(row) > 1]
        for index,cols in enumerate(highScore):
            highScore[index][2] = int(cols[2])
        highScore.sort(reverse = True,key=lambda x: x[2])
        ###

        ### Print Scores ###
        for i in range(10):
            self.c.create_text(200,windowHeight-550+(i*40),
                               anchor = W,
                               font = ("Arial",fontSize,"bold"),
                               fill = fgColour,
                               text = (str(i+1)+"."),
                               tags = "menu")
            self.c.create_text(250,windowHeight-550+(i*40),
                               anchor = W,
                               font = ("Arial",fontSize,"bold"),
                               fill = fgColour,
                               text = (highScore[i][0]),
                               tags = "menu")
            self.c.create_text(windowWidth-400,windowHeight-550+(i*40),
                               anchor = W,
                               font = ("Arial",fontSize,"bold"),
                               fill = fgColour,
                               text = (highScore[i][1]),
                               tags = "menu")
            self.c.create_text(windowWidth-250,windowHeight-550+(i*40),
                               anchor = W,
                               font = ("Arial",fontSize,"bold"),
                               fill = fgColour,
                               text = (highScore[i][2]),
                               tags = "menu")
            i += 1
        ###
    ###
            
    ### Menu Button Function ###
    def menu(self,*args):
        mainMenu = MainMenu(self.window,self.c)
    ###
        
class Gui: #GUI class
    
    ### GUI ###
    def __init__(self): #Initializing function
        window = Tk()
        c = Canvas(window,
                   width = windowWidth,height = windowHeight,
                   bd=0,
                   highlightthickness=0,
                   bg = bgColour)
        mainMenu = MainMenu(window,c)
        c.pack()
        window.mainloop()
    ###

Gui()
