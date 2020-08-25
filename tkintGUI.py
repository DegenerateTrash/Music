import mus
import tkinter as tk
from PIL import ImageTk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        root.geometry("640x360")
        root.title("Spunkify")
        root['bg'] = '#181818'

    def create_widgets(self):
        sdbare = ImageTk.PhotoImage(file="assets/sidebar.png")
        self.sidebr = tk.Label(root, image = sdbare)
        self.sidebr.pack(side="left", position="-anchor")
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()