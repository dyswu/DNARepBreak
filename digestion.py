# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:59:52 2021

@author: derew
"""

from tkinter import *
from methods import *

totalpatterns = np.empty(10, dtype = str);
totallist = []

class digestion:
    def __init__(self, root):

        self.file1= StringVar()
        self.file2= StringVar()

        self.setup()
        
        self.file1.set("No treatment data")
        self.file2.set("No original data")
        
    def setup(self):
        frame_e = Frame(root)
        frame_e.pack()

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
        
        button_pattern = Button(frame_e,
                                text = "Set up files",
                                command = self.setup_data)
        button_pattern.pack(side=BOTTOM, anchor=S)
        
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
        # Update treatment path
        self.file1.set(filename);
    
    def browseFiles2(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("csv files", "*.csv"), ("All", "*.*")))
        # Update original path
        self.file2.set(filename);
    def setup_data(self):
        global totalpatterns, totallist
        originalpath = self.file2.get()
        treatmentpath = self.file1.get()
        
        dfOrig, dfTreat = loaddata(originalpath, treatmentpath)
        
        #Get unique patterns and total patterns sorted
        origPat, origSep = simplify(dfOrig)
        treatPat, treatSep= simplify(dfTreat)
        
        totalpatterns = np.unique(np.concatenate((origPat, treatPat), axis=None))
        print(totalpatterns)
        
        labelpatterns()

        
    def automatic(self):
        originalpath = self.file2.get()
        treatmentpath = self.file1.get()
        
        
    def manual(self):
        originalpath = self.file2.get()
        treatmentpath = self.file1.get()
        m = manualdigest(root, originalpath, treatmentpath)
        
        global totallist

    
class manualdigest:
    def __init__(self, root, originalpath, treatmentpath):
        choose_mode();
        choose_params();

        
#Set up root window
root = Tk()
root.title("Digestion")
root.geometry=("500x250")
root.config(background="white")

def labelpatterns():
    global totalpatterns
    window = Toplevel()
        
    window.title("Assign patterns")
    optionList = tuple(totalpatterns)
        
    labelorigin = Label(window, text = "Origin")
    labelorigin.grid(column=0, row=0)
    

    origin = StringVar()
    origin.set(optionList[0])
    om1 = OptionMenu(window, origin, *optionList)
    om1.grid(column=1, row=0)
    
    labelterminated = Label(window, text = "Terminated")
    labelterminated.grid(column=0, row=1)
    
    terminated = StringVar()
    terminated.set(optionList[0])
    om2 = OptionMenu(window, terminated, *optionList)
    om2.grid(column=1, row=1)
    
    labelongoing = Label(window, text = "Ongoing")
    labelongoing.grid(column=0, row=2)
    
    ongoing = StringVar()
    ongoing.set(optionList[0])
    om3 = OptionMenu(window, ongoing, *optionList)
    om3.grid(column=1, row=2)
    
    labeldiverged = Label(window, text = "Diverged")
    labeldiverged.grid(column=0, row= 3)
    
    diverged = StringVar()
    diverged.set(optionList[0])
    om4 = OptionMenu(window, diverged, *optionList)
    om4.grid(column=1, row=3)
    
    labelconverged = Label(window, text = "Converged")
    labelconverged.grid(column=0, row=4)
    
    converged = StringVar()
    converged.set(optionList[0])
    om5 = OptionMenu(window, converged, *optionList)
    om5.grid(column=1, row=4)
    
    confirm = Button(window, text= 'Save', command = lambda: save_results(origin.get(),
                                                                          terminated.get(),
                                                                          ongoing.get(),
                                                                          diverged.get(),
                                                                          converged.get()))
    confirm.grid(columnspan=2, column=0, row=5)
    
    exitbutton = Button(window, text= 'Exit', command = window.destroy)
    exitbutton.grid(columnspan=2, column=0, row=6)
    
def save_results(origin, terminated, ongoing, diverged, converged):
    global totallist
    totallist = [origin, terminated, ongoing, diverged, converged]

d = digestion(root)

root.mainloop()

print ("name retrieved was", D.name)