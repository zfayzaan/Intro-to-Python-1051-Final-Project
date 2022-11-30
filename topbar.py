from tkinter import *

ws = Tk()
ws.geometry('600x600')
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
