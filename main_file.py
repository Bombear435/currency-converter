import tkinter as tk
from tkinter import ttk
from web_scraping import update_xrates, lista_valute
from convertitore import invio
import pyperclip


def ottieni_output():
    output = invio(e.get(), conv_from.get(), conv_to.get())
    label.config(state='normal')
    label.delete(0, 'end')
    label.insert(0, output)
    label.configure(state='readonly')


def copy_output():
    pyperclip.copy(label.get())
    pyperclip.paste()


if __name__ == '__main__':
    update_xrates()

    win = tk.Tk()
    img = tk.PhotoImage(file='./files/coin.gif')
    win.tk.call('wm', 'iconphoto', win._w, img)
    win.title('Currency Converter')
    win.geometry('500x300')     # dimensioni finestra
    win.resizable(False, False)


    nomi_valute = lista_valute()
    font = ('Helvetica', 16)

    # raggruppo tutto in un unico frame
    main_frame = tk.Frame(win)

    # valore inserito dall'utente
    label_e = tk.Label(main_frame, text="Quantity", font=font, anchor='w')
    e = tk.Entry(main_frame, borderwidth='5', font=font)

    # menù a tendina da cui si vuole convertire
    label_from = tk.Label(main_frame, text="From", font=font, anchor='w')
    conv_from = ttk.Combobox(main_frame, values=nomi_valute, state='readonly')
    conv_from.current(0)
    conv_from.config(font=font)

    # menù a tendina in cui si vuole convertire
    label_to = tk.Label(main_frame, text="To", font=font, anchor='w')
    conv_to = ttk.Combobox(main_frame,values=nomi_valute, state='readonly')
    conv_to.current(1)
    conv_to.config(font=font)

    # tasto di invio
    submit_button = tk.Button(main_frame, text='Submit', bg='#ffffff', command=ottieni_output)

    # etichetta con l'output
    label = tk.Entry(main_frame, bd=0, font=font, fg='#ff0000', width='75')
    label.config(state='readonly')

    # tasto per copiare l'output
    copy_button = tk.Button(main_frame, text='Copy', bg='#ffffff', width='8', height='2', command=copy_output).place(x = 365, y = 245)

    # inizializzo tutti i widget
    main_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=tk.YES)
    label_e.pack(fill=tk.X, padx='25')
    e.pack(fill=tk.X, padx='25')
    label_from.pack(fill=tk.X, padx='25')
    conv_from.pack(fill=tk.X, padx='25')
    label_to.pack(fill=tk.X, padx='25')
    conv_to.pack(fill=tk.X, padx='25')
    submit_button.pack(ipadx='8', ipady='4', pady='10')
    label.pack(padx='20', pady='15')


    win.mainloop()
