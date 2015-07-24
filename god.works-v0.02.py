import tkinter as tk

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

calc = tk.Tk()
calc.title("God.Works")

FRONT_PAGE = ['Old Testament','New Testament']

buttons = [
'OT',  'NT']
"""
,  '9',  '*',  'C',
'4',  '5',  '6',  '/',  'Neg',
'1',  '2',  '3',  '-',  '$',
'0',  '.',  '=',  '+',  '@' ]
"""

# set up GUI
row = 1
col = 0
for i in FRONT_PAGE:
    button_style = 'raised'
    action = lambda x = i: click_event(x)
    tk.Button(calc, text = i, width = 17, height = 10, relief = button_style, command = action) \
    .grid(row = row, column = col, sticky = 'nesw')
    col += 1
    if col > 0: # if col > 4
        col = 0
        row += 1

display = tk.Entry(calc, width = 40, bg = "white")
display.grid(row = 0, column = 0, columnspan = 1) # columnspan = 5

def click_event(key):

    # = -> calculate results
    if key == '=':
        # safeguard against integer division
        if '/' in display.get() and '.' not in display.get():
            display.insert(tk.END, ".0")
            
        # attempt to evaluate results
        try:
            result = eval(display.get())
            display.insert(tk.END, " = " + str(result))
        except:
            display.insert(tk.END, "   Error, use only valid chars")
            
    # C -> clear display        
    elif key == 'C':
        display.delete(0, tk.END)
        
        
    # $ -> clear display        
    elif key == '$':
        display.delete(0, tk.END)
        display.insert(tk.END, "$$$$C.$R.$E.$A.$M.$$$$")
        

    # @ -> clear display        
    elif key == '@':
        display.delete(0, tk.END)
        display.insert(tk.END, "wwwwwwwwwwwwwwwwebsite")        

        
    # neg -> negate term
    elif key == 'neg':
        if '=' in display.get():
            display.delete(0, tk.END)
        try:
            if display.get()[0] == '-':
                display.delete(0)
            else:
                display.insert(0, '-')
        except IndexError:
            pass

    # clear display and start new input     
    else:
        if '=' in display.get():
            display.delete(0, tk.END)
        display.insert(tk.END, key)

# RUNTIME
center(calc)
calc.mainloop()

import tkinter  # Python 3

# if __name__ == '__main__':
#     root = tkinter.Tk()
#     root.attributes('-alpha', 0.0)
#     menubar = tkinter.Menu(root)
#     filemenu = tkinter.Menu(menubar, tearoff=0)
#     filemenu.add_command(label="Exit", command=root.destroy)
#     menubar.add_cascade(label="File", menu=filemenu)
#     root.config(menu=menubar)
#     frm = tkinter.Frame(root, bd=4, relief='raised')
#     frm.pack(fill='x')
#     lab = tkinter.Label(frm, text='Hello World!', bd=4, relief='sunken')
#     lab.pack(ipadx=4, padx=4, ipady=4, pady=4, fill='both')
#     center(root)
#     root.attributes('-alpha', 1.0)
#     root.mainloop()