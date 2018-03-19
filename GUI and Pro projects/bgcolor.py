try:
    import tkinter
except:
    import Tkinter as tkinter

root = tkinter.Tk()

def grey(*args,**kwargs):
    root.configure(background="grey")

def bthing():
    root.configure(background="red")
    root.after(1000, grey)

tkinter.Button(text="OK", command=bthing).pack()

root.configure(background="grey")
root.geometry("400x400")

root.mainloop()