''' Simple form UI using Tkinter '''

import tkinter as tk
#from tkinter import *

def complete() :
    print(f"{name_val.get(), dob_val.get(), gender_val.get(), phone_val.get(), email_val.get(), confirm_val.get()}")

    with open("form.txt", "a") as f :
       # pass
       f.write(f"{name_val.get(), dob_val.get(), gender_val.get(), phone_val.get(), email_val.get(), confirm_val.get()}\n")

    print("Submission Successfull")

root = tk.Tk()

root.geometry("400x400")

root.title('About')

tk.Label(root, text = 'About You', font = 'comicsanms 13 bold', pady=15).grid(row=0, column=3)

name = tk.Label(root, text = 'Name : ')
dob = tk.Label(root, text = 'DOB : ')
gender = tk.Label(root, text = 'Gender : ')
phone = tk.Label(root, text = 'Phone : ')
email = tk.Label(root, text = 'E-mail : ')

name.grid(row=1, column=2, pady=5)
dob.grid(row=2, column=2, pady=5)
gender.grid(row=3, column=2, pady=5)
phone.grid(row=4, column=2, pady=5)
email.grid(row=5, column=2, pady=5)

name_val = tk.StringVar()
dob_val = tk.StringVar()
gender_val = tk.StringVar()
phone_val = tk.IntVar()
email_val = tk.StringVar()
confirm_val = tk.IntVar()

name_entry = tk.Entry(root, textvariable= name_val) 
dob_entry = tk.Entry(root, textvariable= dob_val) 
gender_entry = tk.Entry(root, textvariable= gender_val) 
phone_entry = tk.Entry(root, textvariable= phone_val) 
email_entry = tk.Entry(root, textvariable= email_val) 

name_entry.grid(row=1, column=3, padx=5)
dob_entry.grid(row=2, column=3, padx=5)
gender_entry.grid(row=3, column=3, padx=5)
phone_entry.grid(row=4, column=3, padx=5)
email_entry.grid(row=5, column=3, padx=5)

declare = tk.Checkbutton(text='I declare that the all above information provided are true !', variable=confirm_val)
declare.grid(row=6, column=3)

submit = tk.Button(root, text='Submit', command=complete)
submit.grid(row = 20, column = 10)                                                  # does not move that far

root.mainloop()