# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:59:52 2021

@author: derew
"""

from tkinter import *
from methods import *

totalpatterns = np.empty(10, dtype = str);

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
        
        create_window()
        
        print(totallist)
        
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

def create_window():
    global totalpatterns
    window = Toplevel()
        
    window.title("Assign patterns")
    
    labelorigin = Label(window, text = "Origin").pack()
    optionList = tuple(totalpatterns)
    origin = StringVar()
    origin.set(optionList[0])
    om1 = OptionMenu(window, origin, *optionList).pack()
    
    labelorigin = Label(window, text = "Terminated").pack()
    terminated = StringVar()
    terminated.set(optionList[0])
    om2 = OptionMenu(window, terminated, *optionList).pack()
    
    labelorigin = Label(window, text = "Ongoing").pack()
    ongoing = StringVar()
    ongoing.set(optionList[0])
    om3 = OptionMenu(window, ongoing, *optionList).pack()
    
    labelorigin = Label(window, text = "Diverged").pack()
    diverged = StringVar()
    diverged.set(optionList[0])
    om4 = OptionMenu(window, diverged, *optionList).pack()
    
    labelorigin = Label(window, text = "Converged").pack()
    converged = StringVar()
    converged.set(optionList[0])
    om5 = OptionMenu(window, converged, *optionList).pack()
    
    confirm = Button(window, text= 'Confirm and Exit', command = save_results).pack()
    
def save_results(self):
    totallist = [origin, terminated, ongoing, diverged, converged]
    print(totallist)
    window.destroy()
    
d = digestion(root)

root.mainloop()

print ("name retrieved was", D.name)