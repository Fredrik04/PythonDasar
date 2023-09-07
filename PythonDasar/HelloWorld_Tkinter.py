import tkinter as tk #import modul tkinter
root = tk.Tk() #membuat jendela utama (root window)
label = tk.Label(root, text="Hello World") #membuat elemen label
button = tk.Button(root, text="Click Here") #membuat elemen button
label.pack() #mengatur tata letak label
button.pack() #mengatur tata letak button
root.mainloop() #menjalankan jendala utama dengan mainloop()
