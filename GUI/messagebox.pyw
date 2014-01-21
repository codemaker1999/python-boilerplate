from Tkinter import Tk
import tkMessageBox as mbox

root = Tk()
root.wm_withdraw()
w,h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('1x1+%d+%d'%(w/2,h/2))

#askokcancel ('title','msg')
#askquestion
#askretrycancel
#askyesno
#askyesnocancel
#showerror
#showinfo
#showwarning
