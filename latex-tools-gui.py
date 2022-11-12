import tkinter as tk
import tkinter.ttk as ttk


class LatexToolsGui:
    root: tk.Tk

    def __init__(self, root_tk):
        """
        Constructor. Initializes the GUI class.
        """
        self.root = root_tk  # Object variable
        self.init_gui()

    def get_root(self):
        return self.root

    def init_gui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid()
        ttk.Label(frame,
                  text='Hello World!').grid(row=0, column=0)
        ttk.Button(frame,
                   text='Quit',
                   command=self.root.destroy).grid(row=1, column=0)


if __name__ == '__main__':
    gui = LatexToolsGui(tk.Tk())
    gui.get_root().mainloop()