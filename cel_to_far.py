from tkinter import *
from click import command
r=Tk()
r.title("converter")
r.geometry("470x170")
r.config(bg="lightgreen",pady=30,padx=20)
def logic():
    if((en.get().isalpha())or(en.get().isspace())):
     ans.config(text="invalid input")
    else:
        
        var=float(en.get())
        a=var*1.8+32
        a =round(a,1)
        ans.config(text=f"{a}")

btn=Button(r,text="Calculate",font=("arial",15,"bold"),background="red",command=logic).grid(row=2,column=1)
en=Entry(r,width=50)
en.grid(row=0,column=1,sticky=W)
ans=Label(r,text="0",font=("arial",15,"bold"))
ans.grid(row=1,column=1)
eq=Label(r,text="IS EQUAL TO->").grid(row=1,column=0)
f=Label(r,text="Farenheit").grid(row=1,column=2)
c=Label(r,text="Celcuis").grid(row=0,column=2)

r.mainloop()
