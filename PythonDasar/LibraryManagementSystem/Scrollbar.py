from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

ListBooks=["Atomic Habit","How To Win Friends & Influence People", "Think Fast and Slow", "Meditations", "Good Vibes Good Life", "Man Search for Meaning","Autobiography M.K Gandhi", "Meditations","Letter from Stoic","Filosofi Teras","Laut Bercerita","You Do You","Healing is the New High","Now and Again","7 Habit of Highly Effective People","101 Essays that Will Change the Way You Think","Psychology of Money"]

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for item in ListBooks:
            mylist.insert(END, item)

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()