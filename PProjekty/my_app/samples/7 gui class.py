import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super(App, self).__init__(master)
        self.grid(padx=45, pady=10, row=1, column=0)
        self.klik = 0
        self.start()

    def start(self):
        self.bttn = tk.Button(self)
        self.bttn["text"] = "nie klikano"
        self.bttn["command"] = self.rob_cos
        self.bttn.grid(padx=45, pady=10, row=1, column=0)

    def rob_cos(self):
        self.klik += 1
        self.bttn["text"] = "Liczba kliknięć: " + str(self.klik)
        self.bttn.grid(padx=30, pady=10, row=1, column=0)

root = tk.Tk()
root.title('klikacz')
root.geometry("250x50")
root.resizable(width=False, height=False)

a = App(root)

root.mainloop()

