"""My Diary Application in Tkinter"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkmb
from tkinter import simpledialog as tksd
from tkinter import filedialog as tkfd
from pathlib import Path
from datetime import datetime

# First line
root = tk.Tk()
font_size = tk.IntVar(value=12)

# configure root
root.title('My Diary TTK')
root.geometry('800x600+300+300')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(bg='#888')

style = ttk.Style()

style.configure('TLabel', font='Arial 18 bold')
style.configure('TCheckbutton', font='Arial 16 bold', background='silver')
style.configure('TRadiobutton', font='Arial 16', background='lightblue')
style.configure('TLabelframe.Label', font='Arial 18 bold', background='lightblue')

style.configure('Status.TLabel', font='Arial 12', background='white')

style.map(
    'TRadiobutton',
    font=[('selected', 'Arial 16 bold')]
)
style.map(
    'TCheckbutton',
    background=[
        ('selected', 'pink'),
        ('active', 'red'),
        ('disabled', 'grey')
    ]
)

theme_var = tk.StringVar()

notebook = ttk.Notebook(root)
notebook.grid(sticky=tk.N + tk.E + tk.W + tk.S, padx=5, pady=5)
notebook.enable_traversal()

# Sub-frame for form
form_frame = ttk.Frame(notebook)
form_frame.columnconfigure(0, weight=1)
form_frame.rowconfigure(5, weight=1)
notebook.add(form_frame, text='Diary Entry', underline=0)


# subject
subj_frame = ttk.Frame(form_frame)
subj_frame.columnconfigure(1, weight=1)
subject_var = tk.StringVar()
ttk.Label(
    subj_frame,
    text='Subject: '
).grid(sticky='we', padx=5, pady=5)
ttk.Entry(
    subj_frame,
    textvariable=subject_var
).grid(row=0, column=1, sticky=tk.E + tk.W)
subj_frame.grid(sticky='ew')

# category
cat_frame = ttk.Frame(form_frame)
cat_frame.columnconfigure(1, weight=1)
cat_var = tk.StringVar()
categories = ['Work', 'Hobbies', 'Health', 'Bills']
ttk.Label(
    cat_frame,
    text='Category: '
).grid(sticky=tk.E + tk.W, padx=5, pady=5)
ttk.Combobox(
    cat_frame,
    textvariable=cat_var,
    values=categories
).grid(row=0, column=1, sticky=tk.E + tk.W, padx=5)
cat_frame.grid(sticky='ew')

ttk.Separator(form_frame, orient=tk.HORIZONTAL).grid(sticky='ew')

# Private
private_var = tk.BooleanVar(value=False)
ttk.Checkbutton(
    form_frame,
    variable=private_var,
    text='Private?'
).grid(ipadx=5, ipady=2, sticky='w')

# Datestamp
datestamp_var = tk.StringVar(value='none')
datestamp_frame = tk.Frame(form_frame)
for value in ('None', 'Date', 'Date+Time'):
    ttk.Radiobutton(
        datestamp_frame,
        text=value,
        value=value,
        variable=datestamp_var
    ).pack(side=tk.LEFT)
datestamp_frame.grid(row=3, sticky='e')

# message
message_frame = ttk.LabelFrame(form_frame, text='Message')
message_frame.columnconfigure(0, weight=1)
message_frame.rowconfigure(0, weight=1)
message_inp = tk.Text(message_frame, fg='navy', bg='khaki')
message_inp.grid(sticky='nesw')

scrollbar = ttk.Scrollbar(message_frame)
scrollbar.grid(row=0, column=1, sticky='nse')
message_frame.grid(row=5, sticky='nsew')
scrollbar.configure(command=message_inp.yview)
message_inp.configure(yscrollcommand=scrollbar.set)

# save button
save_btn = ttk.Button(
    form_frame,
    text='Save'
)
save_btn.grid(sticky=tk.E, ipadx=5, ipady=5)

# open button
#open_btn = tk.Button(
#    root,
#    text='Open'
#)
#open_btn.grid(sticky=tk.E, ipadx=5, ipady=5)

# Status bar
status_var = tk.StringVar()
ttk.Label(
    root,
    textvariable=status_var,
    style='Status.TLabel'
).grid(row=100, ipadx=5, ipady=5, padx=5, pady=5, sticky='we')

##############
# Files View #
##############

files_frame = ttk.Frame(notebook)
notebook.add(files_frame, text='Files', underline=0)
files_frame.columnconfigure(0, weight=1)
files_frame.rowconfigure(0, weight=1)


file_tree = ttk.Treeview(files_frame)
file_tree.grid(sticky='nsew')

ft_columns = ('Name', 'Type', 'Created')
file_tree.configure(columns=ft_columns)

for heading in ft_columns:
    file_tree.heading(heading, text=heading)

file_tree.configure(show='headings')


##########################
# Functions and bindings #
##########################

def set_theme(*args):

    theme = theme_var.get()
    style.theme_use(theme)

theme_var.trace_add('write', set_theme)

def populate_treeview(*args):
    """Look for txt and secret files to populate the treeview"""

    children = file_tree.get_children()
    if children:
        file_tree.delete(*children)

    txt_files = list(Path('.').rglob("*.txt"))
    sec_files = list(Path('.').rglob('*.secret'))

    for f in (txt_files + sec_files):
        created = datetime.fromtimestamp(f.stat().st_ctime).strftime('%Y-%m-%d')
        file_tree.insert(
            '', tk.END, iid=f.name,
            values=(
                f.stem,
                f.suffix,
                created
            )
        )

populate_treeview()


def treeview_sort_column(treeview, col, reverse):
    """Sort a treeview by the clicked column"""

    data = [
       (treeview.set(iid, col), iid)
       for iid in treeview.get_children('')
    ]

    data.sort(reverse=reverse)

    for index, (sort_val, iid) in enumerate(data):
        treeview.move(iid, '', index)

    treeview.heading(
        col,
        command=lambda c=col: treeview_sort_column(treeview, c, not reverse)
    )

for col in ft_columns:
    file_tree.heading(
        col,
        text=col,
        command=lambda c=col: treeview_sort_column(file_tree, c, False)
    )

def weaksauce_encrypt(text, password):
    """Weakly and insecurely encrypt some text"""

    offset = sum([ord(x) for x in password])
    encoded = ''.join(
        chr(min(ord(x) + offset, 2**20))
        for x in text
    )
    return encoded

def weaksauce_decrypt(text, password):
    """Decrypt weakly and insecurely encrypted text"""
    offset = sum([ord(x) for x in password])
    decoded = ''.join(
        chr(max(ord(x) - offset, 0))
        for x in text
    )
    return decoded

def open_file():
    """Open a diary file"""

    file_path = tkfd.askopenfilename(
        title='Select a file to open',
        filetypes=[('Secret', '*.secret'), ('Text', "*.txt")],
    )
    if not file_path:
        return
    fp = Path(file_path)
    filename = fp.stem
    category, subject = filename.split(' - ')
    message = fp.read_text()
    if fp.suffix == '.secret':
        password = tksd.askstring(
            'Enter Password',
            'Enter the password used to '
            'encrypt the file.'
        )
        message = weaksauce_decrypt(message, password)

    cat_var.set(category)
    subject_var.set(subject)
    message_inp.delete('1.0', tk.END)
    message_inp.insert('1.0', message)

#open_btn.configure(command=open_file)

def save():
    """Save the data to a file"""

    subject = subject_var.get()
    category = cat_var.get()
    private = private_var.get()
    message = message_inp.get('1.0', tk.END)
    datestamp_type = datestamp_var.get()

    extension = 'txt' if not private else 'secret'
    filename = f'{category} - {subject}.{extension}'

    # Apply optional datestamp in message
    if datestamp_type == 'Date':
        datestamp = datetime.today().strftime('%Y-%m-%d')
    elif datestamp_type == 'Date+Time':
        datestamp = datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    else:
        datestamp = ''
    if datestamp:
        message = f'{message}\n\n{datestamp}'

    if private:
        password = tksd.askstring(
            'Enter password',
            'Enter a password to encrypt the message.'
        )
        message = weaksauce_encrypt(message, password)

    with open(filename, 'w') as fh:
        fh.write(message)

    status_var.set(f'Message was saved to {filename}')
    tkmb.showinfo('Saved', f'Message was saved to {filename}')
    populate_treeview()


save_btn.configure(command=save)

def private_warn(*arg):
    """Warn the user about the consequences of private"""
    private = private_var.get()

    if private:
        response = tkmb.askokcancel(
            "Are you sure?",
            "Do you really want to encrypt this message?"
        )
        if not response:
            private_var.set(False)

private_var.trace_add('write', private_warn)


def check_filename(*args):
    """Check if a filename is already in use"""
    subject = subject_var.get()
    category = cat_var.get()
    private = private_var.get()

    extension = 'txt' if not private else 'secret'
    filename = f'{category} - {subject}.{extension}'

    if Path(filename).exists():
        status_var.set(f'WARNING: {filename} already exists!')
    else:
        status_var.set('')

subject_var.trace_add('write', check_filename)
cat_var.trace_add('write', check_filename)
private_var.trace_add('write', check_filename)

def set_font_size(*args):
    """Set the size of the text widget font from font_size"""
    size = font_size.get()
    message_inp.configure(font=f'TKDefault {size}')

set_font_size()
font_size.trace_add('write', set_font_size)


########
# Menu #
########

menu = tk.Menu(root)
root.configure(menu=menu)

file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=root.destroy)

options_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Options', menu=options_menu)
options_menu.add_checkbutton(label='Private', variable=private_var)

help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(
    label='About',
    command=lambda: tkmb.showinfo('About', 'My Tkinter Diary')
)
menu.add_cascade(label='Help', menu=help_menu)

size_menu = tk.Menu(options_menu, tearoff=0)
for size in range(6, 33, 2):
    size_menu.add_radiobutton(label=size, value=size, variable=font_size)

options_menu.add_cascade(menu=size_menu, label='Font Size')

theme_menu = tk.Menu(options_menu, tearoff=0)
options_menu.add_cascade(menu=theme_menu, label='Theme')

for theme in style.theme_names():
    theme_menu.add_radiobutton(
        label=theme,
        value=theme,
        variable=theme_var
    )



# Last line

root.mainloop()
