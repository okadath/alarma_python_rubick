from tkinter import *
from tkinter import messagebox
import winsound 
import time
from threading import *
import random

tkWindow = Tk()  
tkWindow.wm_attributes("-topmost", True)
# tkWindow.geometry('400x150')  
tkWindow.title('PythonExamples.org - Tkinter Example')


start=False

# https://stackoverflow.com/questions/16745507/tkinter-how-to-use-threads-to-preventing-main-event-loop-from-freezing
# hay que agregar una cola para que siga trabajando pero con la ventana no lockeada
# https://stackoverflow.com/questions/22596975/terminate-the-thread-by-using-button-in-tkinter
def Threading(start): 
    # start=True
    t1=Thread(target=alarm(start)) 
    t1.start() 
    print("start")
    print(start)
  


def alarm(start):
    while start: 
        a=int(w1.get())*60
        timee=random.randint(15,a)
        time.sleep(timee) 
        # if current_time == set_alarm_time: 
        print("Time to Wake up")
        print(start)
 
        tkWindow.deiconify()
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC) 
        tkWindow.wm_attributes("-topmost", True)
        start=False

  
        

# def inicia():  
def oculta(event=None):
    start=True  
    tkWindow.wm_attributes("-topmost", False)
    tkWindow.withdraw()
    print("OCULTA")
    print(start)
    t1=Thread(target=alarm(start)) 
    t1.start() 


def oculta_no_trabaja(event=None):
    start=True  
    tkWindow.wm_attributes("-topmost", False)
    tkWindow.withdraw()
    print("OCULTA2")
    print(start)
    t1=Thread(target=alarm(start)) 
    t1.start() 



# from datetime import datetime

# # print(datetime.today())

# def escribe_sesion():
#     f=open(datetime.today()+".txt","a+")
#     dictionary ={
    
#     "rollno" : 56,
#     "cgpa" : 8.6, 
#     }
# # v = 
# Label(master, textvariable=v).pack()

# v.set("New Text!")


# def muestra():  
#     start=False
#     tkWindow.wm_attributes("-topmost", False)
#     print("muestra")
#     print(start)



# b_start = Button(tkWindow,
#     text = 'Start',
#     command = Threading(start)).pack() 

b_hide = Button(tkWindow,
    text = 'Estoy Trabajando',
    command = oculta).pack() 
b_hide_2 = Button(tkWindow,
    text = 'Ups, estaba haciendo otra cosa',
    command = oculta).pack() 
# b_show = Button(tkWindow,
#     text = 'Stop',
#     command = muestra).pack() 
tkWindow.bind('<Return>', oculta)
tkWindow.bind('<Shift-Return>', oculta_no_trabaja)


# escribe_sesion()
w1 = Scale(tkWindow, from_=2, to=20, tickinterval=2, orient=HORIZONTAL,length=200)
w1.set(15)
w1.pack()
tkWindow.mainloop()