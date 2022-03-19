from tkinter import *
from tkinter import messagebox

tkWindow = Tk()  
tkWindow.wm_attributes("-topmost", True)
# tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')

def muestra():  
    tkWindow.wm_attributes("-topmost", True)

def oculta():  
    tkWindow.wm_attributes("-topmost", False)

button = Button(tkWindow,
	text = 'Show',
	command = muestra)  
button2 = Button(tkWindow,
	text = 'hide',
	command = oculta)  
button.pack() 
button2.pack()  
  
tkWindow.mainloop()