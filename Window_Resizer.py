'''
Create a GUI window which takes an input width and height and upon clicking on a button, say apply, it changes its size as per given input.
'''


from tkinter import *


class window_resize :

    def __init__(self):
         self.root = Tk()
         self.root.title('Window Resizer')
         self.root.geometry('400x300')

         self.cont = Frame(self.root)

         Label(self.cont, text="Enter Height :").grid(row=1, column=1,padx=10,pady=10)
         Label(self.cont, text="Enter Width :").grid(row=2, column=1,padx=10,pady=10)

    
         self.width_val = IntVar()
         self.height_val = IntVar()

         self.width_input = Entry(self.cont, textvariable=self.width_val)
         self.height_input = Entry(self.cont, textvariable=self.height_val)

         self.width_input.grid(row=1,column=2,padx=10, pady=10)
         self.height_input.grid(row=2,column=2,padx=10, pady=10)

         #resize = Canvas(root, width=width_input, height=height_input)
         #resize.pack()

         self.cont.pack(pady=10, padx=10)

         Button(self.root, text='Apply', command=self.change, relief='sunken').pack(pady=10)

         self.root.mainloop()

    def change(self) :
         x=self.width_input.get()
         y=self.height_input.get()
         self.root.geometry(f'{x}x{y}') 

obj = window_resize()