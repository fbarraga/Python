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


# Last line
root.mainloop()


