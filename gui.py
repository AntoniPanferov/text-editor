import os
from tkinter import *
from tkinter import filedialog

class Gui:
    title = "Text editor"
    window = Tk()

    def __init__(self, is_full_screen):
        self.window.title(self.title)
        if is_full_screen:
            self.window.state("zoomed")

        self.frm_tools = Frame(self.window)
        self.frm_tools.pack(fill=X)

        self.create_tool_menu(self.frm_tools)

        self.frm_info = Frame(self.window)
        self.frm_info.pack(fill=X)

        self.frm_text = Frame(self.window)
        self.frm_text.pack(expand=True, fill='both')

        self.txt_content = Text(self.frm_text)
        self.txt_content.pack(expand=True, fill='both')

        self.window.mainloop()

    def create_tool_menu(self, root):
        self.btn_open = Button(root, text='Open', command=self.open_file).pack(side=LEFT)
        self.btn_save = Button(root, text='Save').pack(side=LEFT)
        self.btn_open_in_browser = Button(root, text='Open in Browser').pack(side=LEFT)
        pass

    def open_file(self):
        path = open(filedialog.askopenfilename())

        self.txt_content.delete(1.0, END)
        self.txt_content.insert(END, path.read())
        self.window.title(f'{path.name} --- {os.path.getsize(path.name)}')
'''
laden
speichern
browser
'''
