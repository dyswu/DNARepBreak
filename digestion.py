# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:59:52 2021

@author: derew
"""

from tkinter import *

class Demo:
    def __init__(self, root):

        self.originalpath = ""
        self.treatmentpath = ""
        self.file1= StringVar()
        self.file2= StringVar()

        self.setup()
        
        self.file1.set("No treatment data")
        self.file2.set("No original data")
        
    def setup(self):
        frame_e = Frame(root)
        frame_e.pack()
        
        #text = Entry(frame_e, textvariable=self.t_name, bg="white")
        #text.pack()
        #text.focus_force()

        button_exit = Button(frame_e, text="Exit", command=self.exit)
        button_exit.pack(side=BOTTOM, anchor=S)
        
        button_auto = Button(frame_e,
                             text = "Find Best",
                             command = self.automatic)
        button_auto.pack(side=BOTTOM, anchor=S)
        
        button_manual = Button(frame_e,
                             text = "Manual Digest",
                             command = self.manual)
        button_manual.pack(side=BOTTOM, anchor=S)
        
        label_file_explorer = Label(frame_e,
                                    textvariable = self.file1,
                                    width = 100, height = 2,
                                    fg = "blue")
        label_file_explorer.pack(side= BOTTOM, anchor = S)
        
        button_explore = Button(frame_e,
                                text = "Treatment data:",
                                command = self.browseFiles)
        button_explore.pack(side=BOTTOM, anchor=S)
        
        label_file_explorer2 = Label(frame_e,
                                    textvariable = self.file2,
                                    width = 100, height = 2,
                                    fg = "blue")
        label_file_explorer2.pack(side= BOTTOM, anchor = S)
        
        button_explore2 = Button(frame_e,
                                text = "Original data:",
                                command = self.browseFiles2)
        button_explore2.pack(side=BOTTOM, anchor=S)
    
    def exit(self):
       root.destroy()

    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("csv files", "*.csv"), ("All", "*.*")))
        self.treatmentpath = filename;
        # Change label contents
        self.file1.set(filename);
    
    def browseFiles2(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("csv files", "*.csv"), ("All", "*.*")))
        self.originalpath = filename;
        # Change label contents
        self.file2.set(filename);
    
    def automatic(self):
        originalpath = self.file2.get()
        treatmentpath - self.file1.get()
        
        
    def manual(self):
        originalpath = self.file2.get()
        treatmentpath - self.file1.get()
        

#Set up root window
root = Tk()
root.title("Digestion")
root.geometry=("500x250")
root.config(background="white")

D=Demo(root)


root.mainloop()

print ("name retrieved was", D.name)