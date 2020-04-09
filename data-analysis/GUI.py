"""
how to make executables with pyinstaller
on Mac: pyinstaller
--onefile
--icon=icons/mac.png
--add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk'
--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl'
GUI.py
on Windows:

"""

import tkinter as tk
from tkinter import filedialog as fd
import os


class MainWindow:
    """ Initialization """

    def set_variables(self):
        self.gui_height = 100
        self.gui_width = 200

    def define_gui_elements(self):
        self.root.title("File Converter")
        self.canvas = tk.Canvas(self.root, height=self.gui_height, width=self.gui_width)
        self.frame = tk.Frame(self.root)
        self.convert_button = tk.Button(
            self.frame, text="Convert file", command=self.convert_file
        )

    """ Main program elements """

    def load_file(self):
        self.load_filename = fd.askopenfilename()

    def save_file(self):
        self.save_filename = fd.asksaveasfilename()

    def convert_file(self):
        self.load_file()
        self.save_file()
        self.convert_command = f"ffmpeg -i {self.load_filename} {self.save_filename}"
        os.system(self.convert_command)

    def activate_gui_elements(self):
        self.canvas.pack()
        self.frame.place(relwidth=1, relheight=1)
        self.convert_button.place(relx=0.5, rely=0.5, anchor="center")

    """Execution as script"""

    def main(self):
        self.set_variables()
        self.run()

    def run(self):
        self.root = tk.Tk()
        self.define_gui_elements()
        self.activate_gui_elements()
        self.root.mainloop()


if __name__ == "__main__":
    program = MainWindow()
    program.main()
