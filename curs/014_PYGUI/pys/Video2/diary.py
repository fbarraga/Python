"""My Diary Application in Tkinter"""

import tkinter as tk

# First line
root = tk.Tk()

# configure root
root.title('My Diary')
root.geometry('800x600')
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# subject
subject_label = tk.Label(root, text='Subject: ')
subject_label.grid(sticky='we', padx=5, pady=5)
subject_inp = tk.Entry(root)
subject_inp.grid(row=0, column=1, sticky=tk.E + tk.W)

# category
categories = ['Work', 'Hobbies', 'Health', 'Bills']
cat_label = tk.Label(root, text='Category: ')
cat_label.grid(row=1, column=0, sticky=tk.E + tk.W, padx=5, pady=5)
cat_inp = tk.Listbox(root, height=1)
cat_inp.grid(row=1, column=1, sticky=tk.E + tk.W, padx=5, pady=5)

for category in categories:
    cat_inp.insert(tk.END, category)

# message
message_inp = tk.Text(root)
message_inp.grid(row=2, column=0, columnspan=2, sticky='nesw')

# save button
save_btn = tk.Button(root, text='Save')
save_btn.grid(row=99, column=1, sticky=tk.E, ipadx=5, ipady=5)

# Status bar

status_bar = tk.Label(root, text='')
status_bar.grid(row=100, column=0, columnspan=2, ipadx=5, ipady=5)

# Functions and bindings
def save():
    """Save the data to a file"""

    subject = subject_inp.get()
    selected = cat_inp.curselection()
    if not selected:
        category = 'Misc'
    else:
        category = categories[selected[0]]

    message = message_inp.get('1.0', tk.END)

    filename = f'{category} - {subject}.txt'
    with open(filename, 'w') as fh:
        fh.write(message)

    status_bar.configure(text='File saved')

save_btn.configure(command=save)


    

# Last line
root.mainloop()


