import tkinter as tk

def accoin():
    etiquta.config(text="pu pu pu ")
vantana = tk.Tk()

tk.Button(vantana,text="puslsme si te atraves",command=accoin).pack(padx=10,pady=10)

etiquta = tk.Label(text="has pulsado el butoon")
etiquta.pack(padx=10,pady=10)






vantana.mainloop() # No te salgas


