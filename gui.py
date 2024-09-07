from tkinter import *
from tkinter import messagebox
from file_manager import FileManager

class Gui:
    title = 'Text editor'

    def __init__(self, is_full_screen):
        self.window = Tk()
        self.window.title(self.title)
        if is_full_screen:
            self.window.state('zoomed')

        self.fm = FileManager()

        self.frm_tools = Frame(self.window)
        self.frm_tools.pack(fill=X)

        self.create_tool_menu(self.frm_tools)

        self.frm_text = Frame(self.window)
        self.frm_text.pack(expand=True, fill='both')

        self.txt_content = Text(self.frm_text)
        self.txt_content.pack(expand=True, fill='both')

        self.window.protocol('on_closing', self.on_closing)

        self.window.mainloop()

    def create_tool_menu(self, root):
        self.btn_open = Button(root, text='Open', command=self.open_file).pack(side=LEFT)
        self.btn_save = Button(root, text='Save', command=self.save_file).pack(side=LEFT)
        self.btn_save_as = Button(root, text='Save As', command=self.save_as_file).pack(side=LEFT)
        self.btn_open_in_browser = Button(root, text='Open in Browser', command=self.open_file_in_browser).pack(side=LEFT)

    def open_file(self):
        self.fm.open_file(self)

    def save_file(self):
        self.fm.save_file(self)

    def save_as_file(self):
        self.fm.save_as_file(self)

    def open_file_in_browser(self):
        self.fm.open_file_in_browser(self)

    def on_closing(self):
        if self.fm.path and messagebox.askokcancel('Quit', 'Do you want to save changes?'):
            self.fm.save_file(self)
        self.window.destroy()
