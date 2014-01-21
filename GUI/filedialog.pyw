from Tkinter import Tk
import tkFileDialog as fdialog

root = Tk()
root.wm_withdraw()
w,h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('1x1+%d+%d'%(w/2,h/2))

#askdirectory
#askopenfile
#askopenfilename
#askopenfilenames
#askopenfiles
#asksaveasfile
#asksaveasfilename
