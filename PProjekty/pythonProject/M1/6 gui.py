import tkinter as tk

def dziejesie():

    a = 'no proszę xD'
    L2.config(text=str(a))

root = tk.Tk()

root.title('testowwwe okienko')
root.geometry("400x150")

button1 = tk.Button(root, text='można w to klikać joł')
button1.grid(sticky=None, padx=20, pady=10, row=0, column=0)

button2 = tk.Button(root, text='a tu już tak...', command=dziejesie)
button2.grid(padx=5, pady=10, row=1, column=0)

L1 = tk.Label(root, text=' i nic sie nie dzieje ')
L1.grid(sticky=None, padx=20, pady=10, row=0, column=2)

L2 = tk.Label(root, text='')
L2.grid(padx=5, pady=5, row=1, column=2)

En1 = tk.Entry(root, width=10)
En1.grid(sticky=None, padx=5, pady=5, row=0, column=1)

root.mainloop()