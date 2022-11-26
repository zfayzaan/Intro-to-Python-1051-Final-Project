import turtle

wn = turtle.Screen() #makes background and sets color to white
wn.title("Owl Clicker")
wn.bgcolor("white")

wn.register_shape("owl.gif") #first shape here is the normal owl, and then a smaller one so that on press, it looks animated
wn.register_shape("owl_90.gif")

owl = turtle.Turtle()
owl.shape("owl.gif") #owlshape is now the image we selected
owl.speed(0)

clicks = 0
double = False #this variable is set to False but when we press on the upgrade button it becomes True and then our clicks allows us to get 2x

textPen = turtle.Turtle() #this is the original clicks counter that is drawn
textPen.hideturtle()
textPen.color("black")
textPen.penup()
textPen.goto(0, 300)
textPen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clickedOnOwl(x, y):
    global clicks
    global double
    clicks += 1 + 1 * double # multiplying by boolean value of double. if double is true then our mouseclicks will yield 2x
    textPen.clear()
    textPen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal")) #this is the updated clicks counter that is drawn after clicking on the owl
    owl.shape("owl_90.gif")
    owl.shape("owl.gif") #these two lines is what animates the owl

###################################################################################################################

ButtonPen = turtle.Turtle() #the pen used to make the 2x button
ButtonPen.hideturtle()
ButtonPen.pencolor('white')
ButtonPen.fillcolor('black')

Button_x = -400
Button_y = -300
ButtonLength = 130
ButtonWidth = 50

def drawButton2x(ButtonPen, message = '2x Click Power'): #makes the button with the message
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

def buttonClick2x(x, y):
    global double
    if Button_x <= x <= Button_x + ButtonLength:
        if Button_y <= y <= Button_y + ButtonWidth:
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

###################################################################################################################

wn.onclick(buttonClick2x)

drawButton2x(ButtonPen)

owl.onclick(clickedOnOwl)

wn.mainloop()