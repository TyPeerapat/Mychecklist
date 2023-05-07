from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI=Tk() #This is the home screen
GUI.title("My checklist") #This is name of programe
GUI.geometry("500x500") #This is size

L1 = Label(GUI,text = "My Investment checklist ",font = ("Angsana New",16),fg = "white")
L1.place(x=5,y=0)
L1.pack(ipady = 10)



#B1 = ttk.Button(GUI,text = "Investment checklist")
#B1.pack(ipadx=50,ipady=25)

#FB1 = Frame(GUI) # Like a board

def checklist1():
    text = "DE < 1.5"
    messagebox.showinfo("DE Ratio",text)

B2 = ttk.Button(GUI,text = "DE Ratio",command = checklist1)
B2.pack(ipadx=19,ipady=19)

def checklist2():
    text = "PE < 15%"
    messagebox.showinfo("PE Ratio",text)

B3 = ttk.Button(GUI,text = "PE Ratio",command = checklist2 )
B3.pack(ipadx=19,ipady=19)

def checklist3():
    text = "ROE > 20%"
    messagebox.showinfo("ROE Ratio",text)

B4 = ttk.Button(GUI,text = "ROE Ratio",command = checklist3)
B4.pack(ipadx=15,ipady=19)

def checklist4():
    text = "CFO + and CFI - and CFF -"
    messagebox.showinfo("CFO CFI CFF",text)

B5 = ttk.Button(GUI,text = "CFO CFI CFF ",command = checklist4)
B5.pack(ipadx=6,ipady=19)

B6 = ttk.Button(GUI,text = "PESTEL")
B6.place(x=20,y=360)

B7 = ttk.Button(GUI,text = "Five Forces Model")
B7.place(x=173,y=360)

B8 = ttk.Button(GUI,text = "BMC")
B8.place(x=380,y=360)



GUI.mainloop()
