"""My Diary Application in Tkinter"""

import tkinter as tk
import hashlib
from pathlib import Path

# First line
root = tk.Tk()

# configure root
root.title('My Diary')
root.geometry('800x600')
root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# subject
subj_frame = tk.Frame(root)
subj_frame.columnconfigure(1, weight=1)
subject_var = tk.StringVar()
tk.Label(subj_frame, text='Subject: ').grid(sticky='we', padx=5, pady=5)
tk.Entry(subj_frame, textvariable=subject_var).grid(row=0, column=1, sticky=tk.E + tk.W)
subj_frame.grid(sticky='ew')

# category
cat_frame = tk.Frame(root)
cat_frame.columnconfigure(1, weight=1)
cat_var = tk.StringVar()
categories = ['Work', 'Hobbies', 'Health', 'Bills']
cat_label = tk.Label(cat_frame, text='Category: ')
cat_label.grid(sticky=tk.E + tk.W, padx=5, pady=5)
cat_inp = tk.OptionMenu(cat_frame, cat_var, *categories)
cat_inp.grid(row=0, column=1, sticky=tk.E + tk.W, padx=5, pady=5)
cat_frame.grid(sticky='ew')

# Private
private_var = tk.BooleanVar(value=False)
private_inp = tk.Checkbutton(root, variable=private_var, text='Private?')
private_inp.grid(ipadx=5, ipady=5, stick='e')

# message
message_frame = tk.LabelFrame(root, text='Message')
message_frame.columnconfigure(0, weight=1)
message_inp = tk.Text(message_frame)
message_inp.grid(sticky='nesw')

scrollbar = tk.Scrollbar(message_frame)
scrollbar.grid(row=0, column=1, sticky='nse')
message_frame.grid(sticky='nsew')

scrollbar.configure(command=message_inp.yview)
message_inp.configure(yscrollcommand=scrollbar.set)

# save button
save_btn = tk.Button(root, text='Save')
save_btn.grid(sticky=tk.E, ipadx=5, ipady=5)

# Status bar
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var)
status_bar.grid(row=100, ipadx=5, ipady=5)

# Functions and bindings
def save():
    """Save the data to a file"""

    subject = subject_var.get()
    category = cat_var.get()
    private = private_var.get()
    message = message_inp.get('1.0', tk.END)

    if private:
        message = hashlib.md5(message.encode()).hexdigest()


    filename = f'{category} - {subject}.txt'
    with open(filename, 'w') as fh:
        fh.write(message)

    status_var.set(f'Message was saved to {filename}')

save_btn.configure(command=save)

def check_filename(*args):
    """Check if a filename is already in use"""
    subject = subject_var.get()
    category = cat_var.get()
    filename = f'{category} - {subject}.txt'

    if Path(filename).exists():
        status_var.set(f'WARNING: {filename} already exists!')
    else:
        status_var.set('')


subject_var.trace_add('write', check_filename)
cat_var.trace_add('write', check_filename)

# Last line
root.mainloop()


