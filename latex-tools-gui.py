import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as fd


class LatexToolsGui:
    filename_label: tk.Label | None
    root: tk.Tk

    def __init__(self, root_tk):
        """
        Constructor. Initializes the GUI class.
        """
        self.filename_label = None
        self.filename = None
        self.root = root_tk  # Object variable
        self.init_gui()

    def get_root(self):
        return self.root

    def init_gui(self):
        self.root.title('LaTeX-Tools')
        self.root.geometry('600x400')
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Öffnen', command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label='Beenden', command=self.root.destroy)
        menubar.add_cascade(label='Datei', menu=file_menu)
        self.root.config(menu=menubar)
        frame = ttk.Frame(self.root, padding=10)
        frame.grid()
        prop_frame = ttk.Labelframe(frame, text='Eigenschaften',
                                    width=300, height=400,
                                    borderwidth=2, relief=tk.GROOVE,
                                    padding=5)
        prop_frame.grid(column=0, row=0, sticky=tk.NSEW)
        ttk.Label(prop_frame, text='Datei:').grid(column=0, row=0)
        self.filename_label = ttk.Label(prop_frame, text='... noch keine Datei geöffnet ...')
        self.filename_label.grid(column=1, row=0)

        settings_frame = ttk.Labelframe(frame, text='Einstellungen',
                                        width=300, height=400,
                                        borderwidth=2, relief=tk.GROOVE,
                                        padding=5)
        settings_frame.grid(column=1, row=0, sticky=tk.NSEW)
        ttk.Label(settings_frame, text='Einstellungen').grid(column=0, row=0)

    def open_file(self):
        self.filename = tk.filedialog.askopenfilename(filetypes=[('CSV-Files', '.csv .txt')])
        self.filename_label.config(text=self.filename if len(self.filename) < 20 else f"...{self.filename[-20:]:.20s}")


if __name__ == '__main__':
    gui = LatexToolsGui(tk.Tk())
    gui.get_root().mainloop()
