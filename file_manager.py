import os
from tkinter import *
from tkinter import filedialog, messagebox
import webbrowser
class FileManager:
    file_types = [('HTML File', '*.html'),
                  ('Text Document', '*.txt'),
                  ('All files', '*.*')]

    def __init__(self):
        self.content = ''
        self.path = ''

    def open_file(self, gui):
        path = filedialog.askopenfilename()
        if path:
            try:
                self.content = open(path, 'r').read()
                self.path = path
                gui.txt_content.delete(1.0, END)
                gui.txt_content.insert(END, self.content)
                gui.window.title(self.build_label(gui.title))
            except IOError as e:
                messagebox.showerror('Error', f'Failed to open file: {e}')
        else:
            messagebox.showinfo('Info', 'File not selected')

    def open_file_in_browser(self, gui):
        self.save_file(gui)
        #webbrowser.open('file://' + os.path.realpath('C:\\Users\\panan\\OneDrive\\Desktop\\index.html'))
        webbrowser.open(f'file://{self.path}')

    def save_file(self, gui):
        if self.path:
            try:
                open(self.path, 'w').write(gui.txt_content.get(1.0, END))
                gui.window.title(self.build_label(gui.title))
            except IOError as e:
                messagebox.showerror('Error', f'Failed to save file: {e}')
        else:
            self.save_as_file(gui)

    def save_as_file(self, gui):
        path = filedialog.asksaveasfilename(defaultextension='.html', filetypes=self.file_types)
        if path:
            try:
                open(path, 'w').write(gui.txt_content.get(1.0, END))
                self.path = path
                gui.window.title(self.build_label(gui.title))
            except IOError as e:
                messagebox.showerror('Error', f'Failed to save file: {e}')
                
    def build_label(self, default_label):
        return f'{default_label} | {os.path.basename(self.path)} --- {os.path.getsize(self.path)} bytes'
