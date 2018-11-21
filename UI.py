
import os
import tkinter as tk

window = tk.Tk()
# Judul dari Window
window.title("Pendataan Barang Kacamata")
# Ukuran Window ketika pertama kali muncul, dihitung dalam pixel
window.geometry("400x400")

#-----LABELS-----
title = tk.Label(text="Uji Coba. \nMembuat GUI", font=("Calibri", 20))
title.grid(column=0, row=0)
#-----ENTRY FIELDS-----
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=1)
#-----BUTTONS-----
button1 = tk.Button(text="Click me!", bg="red")
button1.grid(column=1, row=1)
#-----TEXT FIELDS-----
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

# Perintah agar frame muncul di layar
window.mainloop()