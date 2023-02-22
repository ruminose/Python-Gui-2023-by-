#Fist ep gui python
from tkinter import *

GUI = Tk()
GUI.title('Pet Shop Pos')
GUI.geometry('800x500')
c=Canvas(GUI)
filename=PhotoImage(file="\\python gui\\Cat and dog-pana.png")
background_label=Label(GUI,image=filename)
background_label.place (x=20,y=10,relwidth=1,relheight=1)

L = Label(GUI,text='Happy',font=('Angsana New',100,'bold'))
#L.pack()
L.place(x=300,y=300)
c.pack()
GUI.mainloop()