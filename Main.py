import Graphic_Module as gm
import tkinter as tk
import time as tm
print("3 řádek")

class Login:
    def log(self):
        window2 = tk.Tk(className=" Správce hesel")
        window2.geometry("550x310+500+250")
        window2.configure(bg="gray")
        print("10 řádek")

        def name():
            entry_name = tk.Entry(font=("arial", 17), bg="orange", width=25)
            entry_name.place(x=112, y=100)
            background_text = "Uživatelské jméno"
            entry_name.insert(0, background_text)

            def on_entry_click(event):
                if entry_name.get() == background_text:
                    entry_name.delete(0, tk.END)  # Odebrání textu na pozadí

            entry_name.bind("<FocusIn>", on_entry_click)
            A = entry_name.get()
            return A

        def passwd():
            entry = tk.Entry(font=("arial", 17), bg="orange", width=25)
            entry.place(x=112, y=150)
            background_text = "Heslo"
            entry.insert(0, background_text)

            def on_entry_click(event):
                if entry.get() == background_text:
                    entry.delete(0, tk.END)  # Odebrání textu na pozadí

            entry.bind("<FocusIn>", on_entry_click)
            B = entry.get()
            return B

        print("40 řádek")

        C = name()
        D = passwd()
        print(D)

        labelfalse = tk.Label(window2, text="Uživatelské jméno nebo heslo není správné! Zkuste to znovu.", bg="gray")

        def controll():
            if D == "Heslo":
                gm.Graphic.graphic("Grafika")
                window2.destroy()
            else:
                labelfalse.place(x=112, y=230)

        controllbutton = tk.Button(window2, text="Pokračovat do Správce", command=controll, bg="orange")
        controllbutton.place(x=112, y=200)
        window2.mainloop()
        print("55 řádek")

print("57 řádek")
Login.log("Login")