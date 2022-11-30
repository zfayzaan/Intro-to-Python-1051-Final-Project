import turtle
import time
import threading
import random
import tkinter as tk



wn = turtle.Screen() #makes background and sets color to white
wn.bgpic('gamebackground.gif')
wn.title("Owl Clicker")
#wn.bgcolor("white")

wn.register_shape("owl.gif") #first shape here is the normal owl, and then a smaller one so that on press, it looks animated
wn.register_shape("owl_90.gif")
wn.register_shape("rosen.gif")
wn.register_shape("rosen_90.gif")



owl = turtle.Turtle()
owlimage = "owl.gif"
owlSmaller = "owl_90.gif"
owl.shape(owlimage) #owlshape is now the image we selected
owl.penup()
#owl.setpos(-300,0)
owl.speed(4)

clicks = 0
starttime = time.time()
slowDown = False

double = False #this variable is set to False but when we press on the upgrade button it becomes True and then our clicks allows us to get 2x
quad =  False

clicksBackgroundx = -150
clicksBackgroundy = 297
clicksBackgroundLength = 300
clicksBackgroundWidth = 70

backgroundPen = turtle.Turtle() #this is the original clicks counter that is drawn
backgroundPen.hideturtle()
backgroundPen.color("white")

backgroundPen.penup()
backgroundPen.begin_fill()
backgroundPen.fillcolor('red')
backgroundPen.goto(clicksBackgroundx, clicksBackgroundy)
backgroundPen.goto(clicksBackgroundx + clicksBackgroundLength, clicksBackgroundy)
backgroundPen.goto(clicksBackgroundx + clicksBackgroundLength, clicksBackgroundy + clicksBackgroundWidth)
backgroundPen.goto(clicksBackgroundx, clicksBackgroundy + clicksBackgroundWidth)
backgroundPen.goto(clicksBackgroundx, clicksBackgroundy)
backgroundPen.end_fill()
backgroundPen.goto(clicksBackgroundx + 15, clicksBackgroundy + 15)

textPen = turtle.Turtle() #this is the original clicks counter that is drawn
textPen.hideturtle()
textPen.color("white")
textPen.penup()
textPen.goto(0, 300)
textPen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 50, "bold"))

def clickedOnOwl(x, y):
    global clicks
    global double
    global quad
    clicks += 1
    if double == True and quad == True:
        clicks += 7
    elif double == True:
        clicks += 1
    elif quad == True:
        clicks += 3 
    textPen.clear()
    textPen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 50, "bold")) #this is the updated clicks counter that is drawn after clicking on the owl
    owl.shape(owlimage)
    owl.shape(owlSmaller) #these two lines is what animates the owl

def autoClicker(n=1): #function for auto clicker. Adds one to clicks every second
    global clicks
    while True:
        clicks += 1
        time.sleep(n)
###################################################################################################################

ButtonPen = turtle.Turtle() #the pen used to make the button
ButtonPen.hideturtle()
ButtonPen.pencolor('black')
ButtonPen.fillcolor('white')

Button_x = -400
Button_y = -300
ButtonLength = 200
ButtonWidth = 50

Button2_x = -400
Button2_y = -360
Button2Length = 200
Button2Width = 50

Button3_x = -195
Button3_y = -360
Button3Length = 200
Button3Width = 50

ButtonR_x = 195
ButtonR_y = -300
ButtonRLength = 200
ButtonRWidth = 50

ButtonQuad_x = -195
ButtonQuad_y = -300
ButtonQuadLength = 200
ButtonQuadWidth = 50

def drawButton2x(ButtonPen, message = '2x Click Power | COST 30'): #makes the button with the message
    ButtonPen.penup()
    ButtonPen.begin_fill()
    ButtonPen.goto(Button_x, Button_y)
    ButtonPen.goto(Button_x + ButtonLength, Button_y)
    ButtonPen.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
    ButtonPen.goto(Button_x, Button_y + ButtonWidth)
    ButtonPen.goto(Button_x, Button_y)
    ButtonPen.end_fill()
    ButtonPen.goto(Button_x + 15, Button_y + 15)
    ButtonPen.write(message, font = ('Arial', 15, 'normal'))
def drawButtonQuad(ButtonPen, message = '4x Click Power | COST 90'):
    ButtonPen.penup()
    ButtonPen.begin_fill()
    ButtonPen.goto(ButtonQuad_x, ButtonQuad_y)
    ButtonPen.goto(ButtonQuad_x + ButtonQuadLength, ButtonQuad_y)
    ButtonPen.goto(ButtonQuad_x + ButtonQuadLength, ButtonQuad_y + ButtonQuadWidth)
    ButtonPen.goto(ButtonQuad_x, ButtonQuad_y + ButtonQuadWidth)
    ButtonPen.goto(ButtonQuad_x, ButtonQuad_y)
    ButtonPen.end_fill()
    ButtonPen.goto(ButtonQuad_x + 15, ButtonQuad_y + 15)
    ButtonPen.write(message, font = ('Arial', 15, 'normal'))
    
def drawButtonAuto(ButtonPen, message = 'Auto Click #1 | COST 60'): #makes the button with the message
    ButtonPen.penup()
    ButtonPen.begin_fill()
    ButtonPen.goto(Button2_x, Button2_y)
    ButtonPen.goto(Button2_x + Button2Length, Button2_y)
    ButtonPen.goto(Button2_x + Button2Length, Button2_y + Button2Width)
    ButtonPen.goto(Button2_x, Button2_y + Button2Width)
    ButtonPen.goto(Button2_x, Button2_y)
    ButtonPen.end_fill()
    ButtonPen.goto(Button2_x + 15, Button2_y + 15)
    ButtonPen.write(message, font = ('Arial', 15, 'normal'))

def drawButtonSlower(ButtonPen, message = 'Slow Down Owl | COST 15'): #makes the button with the message
    ButtonPen.penup()
    ButtonPen.begin_fill()
    ButtonPen.goto(Button3_x, Button3_y)
    ButtonPen.goto(Button3_x + Button3Length, Button3_y)
    ButtonPen.goto(Button3_x + Button3Length, Button3_y + Button3Width)
    ButtonPen.goto(Button3_x, Button3_y + Button3Width)
    ButtonPen.goto(Button3_x, Button3_y)
    ButtonPen.end_fill()
    ButtonPen.goto(Button3_x + 15, Button3_y + 15)
    ButtonPen.write(message, font = ('Arial', 15, 'normal'))

def drawRosenbutton(ButtonPen, message = 'Click for a Suprise'):
    ButtonPen.penup()
    ButtonPen.begin_fill()
    ButtonPen.goto(ButtonR_x, ButtonR_y)
    ButtonPen.goto(ButtonR_x + ButtonRLength, ButtonR_y)
    ButtonPen.goto(ButtonR_x + ButtonRLength, ButtonR_y + ButtonRWidth)
    ButtonPen.goto(ButtonR_x, ButtonR_y + ButtonRWidth)
    ButtonPen.goto(ButtonR_x, ButtonR_y)
    ButtonPen.end_fill()
    ButtonPen.goto(ButtonR_x + 15, ButtonR_y + 15)
    ButtonPen.write(message, font = ('Arial', 15, 'normal'))

def buttonClicks(x, y):
    global double
    global quad
    global clicks
    global slowDown
    global autoClicker
    global owlimage
    global owlSmaller
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
            if clicks >= 30:
                ButtonPen.fillcolor('green') #makes the button green because we have now purchased
                ButtonPen.pencolor('black')
                ButtonPen.penup()
                ButtonPen.begin_fill()
                ButtonPen.goto(Button_x, Button_y)
                ButtonPen.goto(Button_x + ButtonLength, Button_y)
                ButtonPen.goto(Button_x + ButtonLength, Button_y + ButtonWidth)
                ButtonPen.goto(Button_x, Button_y + ButtonWidth)
                ButtonPen.goto(Button_x, Button_y)
                ButtonPen.end_fill()
                ButtonPen.goto(Button_x + 15, Button_y + 15)
                ButtonPen.write("PURCHASED", font=('Arial', 15, 'bold'))
                double = True #double becomes true here after the user presses on the button. So now pressing on the owl will give 2x
                clicks = clicks - 30
    if ButtonQuad_x <= x <= ButtonQuad_x + ButtonQuadLength:
        if ButtonQuad_y <= y <= ButtonQuad_y + ButtonQuadWidth:
            if clicks >= 90:
                ButtonPen.fillcolor('green') #makes the button green because we have now purchased
                ButtonPen.pencolor('black')
                ButtonPen.penup()
                ButtonPen.begin_fill()
                ButtonPen.goto(ButtonQuad_x, ButtonQuad_y)
                ButtonPen.goto(ButtonQuad_x + ButtonQuadLength, ButtonQuad_y)
                ButtonPen.goto(ButtonQuad_x + ButtonQuadLength, ButtonQuad_y + ButtonQuadWidth)
                ButtonPen.goto(ButtonQuad_x, ButtonQuad_y + ButtonQuadWidth)
                ButtonPen.goto(ButtonQuad_x, ButtonQuad_y)
                ButtonPen.end_fill()
                ButtonPen.goto(ButtonQuad_x + 15, ButtonQuad_y + 15)
                ButtonPen.write("PURCHASED", font=('Arial', 15, 'bold'))
                quad = True
                clicks = clicks - 90
    if Button2_x <= x <= Button2_x + Button2Length: #checking if user has pressed the second button labeled "Auto Click #1"
        if Button2_y <= y <= Button2_y + Button2Width:
            if clicks >= 60:
                ButtonPen.fillcolor('green')
                ButtonPen.pencolor('black')
                ButtonPen.penup()
                ButtonPen.begin_fill()
                ButtonPen.goto(Button2_x, Button2_y)
                ButtonPen.goto(Button2_x + Button2Length, Button2_y)
                ButtonPen.goto(Button2_x + Button2Length, Button2_y + Button2Width)
                ButtonPen.goto(Button2_x, Button2_y + Button2Width)
                ButtonPen.goto(Button2_x, Button2_y)
                ButtonPen.end_fill()
                ButtonPen.goto(Button2_x + 15, Button2_y + 15)
                ButtonPen.write("PURCHASED", font=('Arial', 15, 'bold'))
                clicks = clicks - 60
                thread = threading.Thread(target=autoClicker,) #starts the autoclicker
                thread.start()
    if Button3_x <= x <= Button3_x + Button3Length:
        if Button3_y <= y <= Button3_y + Button3Width:
            if clicks >= 15:
                ButtonPen.fillcolor('green')
                ButtonPen.pencolor('black')
                ButtonPen.penup()
                ButtonPen.begin_fill()
                ButtonPen.goto(Button3_x, Button3_y)
                ButtonPen.goto(Button3_x + Button3Length, Button3_y)
                ButtonPen.goto(Button3_x + Button3Length, Button3_y + Button3Width)
                ButtonPen.goto(Button3_x, Button3_y + Button3Width)
                ButtonPen.goto(Button3_x, Button3_y)
                ButtonPen.end_fill()
                ButtonPen.goto(Button3_x + 15, Button3_y + 15)
                ButtonPen.write("PURCHASED", font=('Arial', 15, 'bold'))
                clicks = clicks - 15
                slowDown = True
    if ButtonR_x <= x <= ButtonR_x + ButtonRLength:
        if ButtonR_y <= y <= ButtonR_y + ButtonRWidth:
            ButtonPen.fillcolor('green')
            ButtonPen.pencolor('black')
            ButtonPen.penup()
            ButtonPen.begin_fill()
            ButtonPen.goto(ButtonR_x, ButtonR_y)
            ButtonPen.goto(ButtonR_x + ButtonRLength, ButtonR_y)
            ButtonPen.goto(ButtonR_x + ButtonRLength, ButtonR_y + ButtonRWidth)
            ButtonPen.goto(ButtonR_x, ButtonR_y + ButtonRWidth)
            ButtonPen.goto(ButtonR_x, ButtonR_y)
            ButtonPen.end_fill()
            ButtonPen.goto(ButtonR_x + 15, ButtonR_y + 15)
            ButtonPen.write("PURCHASED", font=('Arial', 15, 'bold'))
            owlimage = "rosen.gif"
            owlSmaller = "rosen_90.gif"
            owl.shape(owlimage)


###################################################################################################################
wn.onclick(buttonClicks)

drawButton2x(ButtonPen)
drawButtonQuad(ButtonPen)
drawButtonAuto(ButtonPen)
drawButtonSlower(ButtonPen)
drawRosenbutton(ButtonPen)

owl.onclick(clickedOnOwl)

owl.penup() #makes owl go left and right
i = 0
distance =(random.randint(25,300))
turndegree= random.randint(30,360)
leftorright= ["R","L"]
choicejawn = random.choice(leftorright)
while i < 5000:
    distance
    turndegree
    choicejawn
    if (owl.xcor() > -450 and owl.xcor() <450) and (owl.ycor() >-350 and owl.ycor() <350):   #found on stackoverflow
        owl.forward(distance)
        
        if choicejawn == "R":
            owl.right(turndegree)
        if choicejawn == "L":
            owl.left(turndegree)
        if slowDown == False:
            owl.speed(4)
        elif slowDown == True:
            owl.speed(1)
    else:
        owl.right(180)
        owl.forward(distance)
        if slowDown == False:
            owl.speed(4)
        elif slowDown == True:
            owl.speed(1)
        i += 1

###############cursor picture jawn







wn.mainloop()
turtle.mainloop()

