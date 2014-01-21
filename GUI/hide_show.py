#Hide the root window with:
root.withdraw()

#Bring the root window back up with:
root.update()
root.deiconify()

#Remove root window border and title bar with:
root.overrideredirect(True)

#Bring the border and title bar back after 5000 milliseconds:
root.after(5000, root.overrideredirect, False)
