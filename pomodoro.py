#!/usr/bin/env python
# coding: utf-8

# In[4]:


# IMPORT REQUIRED MODULES
from tkinter import *
import math



## GLOBAL VARIABLES
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps=0
timer=None



#---------------------------------------RESET_TIMER----------------------------------------------------------------------------#
# CREATE RESET TIMER FUNCTION TO RESET THE TIMER
def reset_timer():
    root.after_cancel(timer)  # stop the timer
    canvas.itemconfig(timer_set,text="00:00") 
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps=0

#---------------------------------------START_TIMER----------------------------------------------------------------------------#
# CREATE START TIMER TO START TIMER
def start_timer():
    global reps
    reps+=1
    
    if reps%8==0:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Break",fg=RED)
        
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text="Break",fg=PINK)
        
    else:
        count_down(WORK_MIN)
        timer_label.config(text="Work",fg=GREEN)
        
        
#-------------------------------------------COUNT_DOWN-------------------------------------------------------------------------#        
        
# CREATE COUNT DOWN FUNCTION        
def count_down(count):
    count_min=math.floor(count/60) # convert to minutes
    count_sec=count%60             # convert seconds
    
    if count_sec<10:
        count_sec=f"0{count_sec}"
    
    if count_sec==0:
        count_sec="00"
    
    
    
    canvas.itemconfig(timer_set,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=root.after(1000,count_down,count-1)  # start the timer 


    else:
        start_timer()
        marks=""
        work_sess=math.floor(reps/2)
        for _ in range(work_sess):
            marks+="✓"
        check_mark.config(text=marks)
        
################################################################################################################################
# CREATE WINDOW
root=Tk()
root.title("pomodoro")
root.config(padx=100,pady=50,bg=YELLOW)
################################################################################################################################
# CREATE CANVAS

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")       # LOAD IMAGE
canvas.create_image(100,112,image=img)  # SET IMAGE TO CANVAS

timer_set=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))  # CREATE TIMER

canvas.grid(row=2,column=2)

#---------------------------------------------------------------------------------------------------------------------------------#
# CREATE TIMER LABEL

timer_label=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
timer_label.grid(row=1,column=2)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++================================================#
# CREATE START BUTTON
start=Button(text="Start",highlightthickness=0,command=start_timer,width=10)
start.grid(row=3,column=1)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# CREATE RESET BUTTON
reset=Button(text="Reset",highlightthickness=0,command=reset_timer,width=10)
reset.grid(row=3,column=3)

#--------------------------------------------------------------------------------------------------------------------------------#
# CREATE CHECK MARKS

check_mark=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"bold"))

check_mark.grid(row=3,column=2)
################################################################################################################################
root.mainloop()

