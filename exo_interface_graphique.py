from tkinter import *

coord = [(10, 10), (210, 10), (410, 10), (110,100), [310,100]]

def circle1():
    global x1, y1 
    x1, y1 = coord[0]
    can.create_oval(x1, y1, x1 + 200, y1 + 200, width = 2, outline = 'blue')

def circle2():
    global x1, y1 
    x1, y1 = coord[1]
    can.create_oval(x1, y1, x1 + 200, y1 + 200, width = 2, outline = 'black')

def circle3():
    global x1, y1 
    x1, y1 = coord[2]
    can.create_oval(x1, y1, x1 + 200, y1 + 200, width = 2, outline = 'red')

def circle4():
    global x1, y1 
    x1, y1 = coord[3]
    can.create_oval(x1, y1, x1 + 200, y1 + 200, width = 2, outline = 'yellow')

def circle5():
    global x1, y1 
    x1, y1 = coord[4]
    can.create_oval(x1, y1, x1 + 200, y1 + 200, width = 2, outline = 'green')

fen1 = Tk()
can = Canvas(fen1, bg = 'white', height = 500, width =1000)
can.pack()
bou1 = Button(fen1, text ='quit', height = 10, width = 20, command = fen1.quit)
bou1.pack(side=RIGHT)
bou2 = Button(fen1, text ='1', command = circle1)
bou2.pack(side=LEFT)
bou3 = Button(fen1, text='2', command=circle2)
bou3.pack(side=LEFT)
bou4 = Button(fen1, text='3', command = circle3)
bou4.pack(side=LEFT)
bou5 = Button(fen1, text='4', command = circle4)
bou5.pack(side=LEFT)
bou6 = Button(fen1, text='5', command =circle5)
bou6.pack(side=LEFT)

fen1.mainloop()
# démarrage du réceptionnaire d’événements
fen1.destroy()
# destruction (fermeture) de la fenêtre