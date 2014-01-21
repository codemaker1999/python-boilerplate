import Tkinter as tk

# Callback function for button
def button_fn(callback=None):
    '''Print whatever entry holds to standard output'''
    txtinput = entry.get()
    entry.delete(0,tk.END)
    print txtinput

# Set up tkinter environment
root = tk.Tk()
w,h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('350x26+%d+%d'%(w/2,h/2))
root.bind('<Return>',button_fn)

# Label
label = tk.Label(root,text='Enter Something :',anchor=tk.E)
label.grid(row=1,column=1,sticky=tk.E)

# Entry
entry = tk.Entry(root)
entry.grid(row=1,column=2,sticky=tk.E+tk.W)
entry.focus_set()

# Button
button = tk.Button(root,text="Go",command=button_fn)
button.grid(row=1,column=3,sticky=tk.W)

# Weight middle column
root.columnconfigure(2,weight=1)

if __name__ == '__main__':
    tk.mainloop()
