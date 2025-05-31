from tkinter import *
import os

def Resatrt():
    os.system("shutdown /r /t 1")
def Resatrt_time():
    os.system("shutdown /r /t 20")
def LogOut():
    os.system("shutdown -1")
def Shutdown():
    os.system("shutdown /s /t 1")        
    

st= Tk()
st.title("ShutDown_App")
st.geometry("600x600")
st.config(bg="red")


    

r_button= Button (st,text="RESTART",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Resatrt)
r_button.place(x=160,y=100,height=50,width=250,)
rt_button= Button (st,text="RESTART_TIME",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Resatrt_time)
rt_button.place(x=160,y=200,height=50,width=250,)
l_button= Button (st,text="LOG-OUT",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=LogOut)
l_button.place(x=160,y=300,height=50,width=250,)
st_button= Button (st,text="SHUTDOWN",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=Shutdown)
st_button.place(x=160,y=400,height=50,width=250,)


 

st.mainloop()




