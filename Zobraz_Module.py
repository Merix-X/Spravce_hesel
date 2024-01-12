import tkinter as tk


def graphic_module():
    window = tk.Tk(className=" Graphic_Module.py")
    window.geometry("1000x700")           #první číslo je ŠÍŘKA a druhé číslo je VÝŠKA
    window.config(bg="gray")

    text_array = tk.Text(window, bg="black", fg="dark orange", height=700, width=1000)
    text_array.pack()

    with open('Graphic_Module.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)

    window.mainloop()


def main():
    window = tk.Tk(className="main.py")
    window.geometry("1000x700")
    window.config(bg="gray")

    text_array = tk.Text(window, bg="black", fg="dark orange", height=700, width=1000)
    text_array.pack()

    with open('main.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)

    window.mainloop()


def string_modifications():
    window = tk.Tk(className=" Search_String.py")
    window.geometry("1000x700")
    window.config(bg="gray")

    text_array = tk.Text(window, bg="black", fg="dark orange", height=700, width=1000)
    text_array.pack()

    with open('Search_String.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)

    window.mainloop()


def readme():
    window = tk.Tk(className=" README.txt")
    window.geometry("840x780")
    window.config(bg="gray")

    text_array = tk.Text(window, bg="white", fg="black", height=780, width=840)
    text_array.pack()

    with open('README.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)

    window.mainloop()

def jak_pridat_heslo():
    window = tk.Tk(className=" Jak správně přidat heslo?")
    window.geometry("865x500")
    window.config(bg="gray")

    text_array = tk.Text(window, bg="white", fg="black", height=500, width=865)
    text_array.pack()

    with open('jak_pridat_heslo.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)

    window.mainloop()


def zobraz_module():
    window = tk.Tk(className=" View_Module.py")
    window.geometry("1000x700")
    window.config(bg="gray")

    text_array = tk.Text(window, bg="black", fg="dark orange", height=700, width=1000)
    text_array.pack()

    with open('Zobraz_Module.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)

    window.mainloop()

def zobraz_hesla():
    window = tk.Tk(className=" Seznam uložených hesel")
    window.geometry("1000x700")
    window.config(bg="gray")

    text_array = tk.Text(window, bg="gray", fg="yellow", height=700, width=1000)
    text_array.pack()

    with open('Hesla.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()

    text_array.insert(tk.END, obsah)