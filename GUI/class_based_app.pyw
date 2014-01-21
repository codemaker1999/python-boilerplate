import Tkinter as tk
from Tkinter import N,E,S,W
#import tkMessageBox as mbox
#    askokcancel
#    askquestion
#    askretrycancel
#    askyesno
#    askyesnocancel
#    showerror
#    showinfo
#    showwarning

#import tkFileDialog as fdialog
#   askdirectory
#   askopenfile
#   askopenfilename
#   askopenfilenames
#   askopenfiles
#   asksaveasfile
#   asksaveasfilename

class GUIapp():
    def __init__(self,root):
        self.root = root

def main():
    root = tk.Tk()
    #tk.wm_withdraw()
    root.title('Title')
    w,h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry('{}x{}+{}+{}'.format(600,400,w/2,h/2))
    app = GUIapp(root,)
    tk.mainloop()

if __name__ == '__main__':
    main()
