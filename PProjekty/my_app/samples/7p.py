import tkinter as tk

class Aplikacja(tk.Frame):
	def __init__(self, master):
		super(Aplikacja, self).__init__(master)
		self.grid()
		self.bttn_clicks = 0
		self.create_widget()

	def create_widget(self):
		self.bttn = tk.Button(self)
		self.bttn["text"] = "Liczba klikniec: 0"
		self.bttn["command"] = self.update_count
		self.bttn.grid()

	def update_count(self):
		self.bttn_clicks += 1
		self.bttn["text"] = "Liczba klikniec: " + str(self.bttn_clicks)

root = tk.Tk()
root.title("Licznik klikniec")
root.geometry("200x50")


app = Aplikacja(root)

root.mainloop()