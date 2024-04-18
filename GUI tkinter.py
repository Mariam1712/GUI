import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Data Entry Form')

frame = tkinter.Frame(window)
frame.pack()

user_info = tkinter.LabelFrame(frame, text='User information')
user_info.grid(row=0, column=0, padx=20, pady=10)

first_name = tkinter.Label(user_info, text='First Name')
first_name.grid(row=0, column=0)

last_name = tkinter.Label(user_info, text="Last Name")
last_name.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info)
last_name_entry = tkinter.Entry(user_info)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title = tkinter.Label(user_info, text='title')
title_combo = ttk.Combobox(user_info, values=["", 'Mr.', 'Mrs.', 'Mast',
                                              'Ms.', 'Divorced', 'Dr.'])
title.grid(row=0, column=2)
title_combo.grid(row=1, column=2)

age = tkinter.Label(user_info, text='Age')
age_spinbox = tkinter.Spinbox(user_info, from_=16, to=100)
age.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

window.mainloop()
