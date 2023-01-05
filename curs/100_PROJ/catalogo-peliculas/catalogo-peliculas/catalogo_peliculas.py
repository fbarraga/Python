import tkinter as tk
from client.gui_app import Frame, barra_menu
import sys,os

def main():
    root = tk.Tk()
    root.title('Catálogo de Películas')
    program_directory=sys.path[0]
    root.iconphoto(True,tk.PhotoImage(file=os.path.join(program_directory,"img/cp-logo.png")))
    #root.iconbitmap("cp-logo.ico")
    root.resizable(0,0)
    
    barra_menu(root)

    app = Frame(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()
