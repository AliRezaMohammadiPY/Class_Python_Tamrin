import tkinter as tk

def button_click():
    root = tk.Tk()
    root.title("Rooz Ha")
    root.geometry("300x375")
    a = mah.get()

    try:
        a = int(a)
    except ValueError:
        tk.Label(root, text="لطفا یک گزینه را انتخاب کنید ( دوباره امتحان کن )", font=("Aviny", 22), fg="red").pack()
    if a == 1:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(1, 91, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=30, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)

    elif a == 2:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(91, 181, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=30, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)

    elif a == 3:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(181, 271, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=30, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)

    elif a == 4:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(271, 361, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=30, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)

    elif a == 5:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(361, 451, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=30, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)

    elif a == 6:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(451, 541, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=30, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)

    elif a == 7:
        def spin_button():
            day = 1
            SB = spin_box.get()
            for safhe in range(541, 604, 3):
                if day == int(SB):
                    tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                    tk.Label(root, text=f"روز : {day}", font=("Aviny", 22), fg="Orange").pack()
                    tk.Label(root, text=f"صبح : {safhe} , ظهر : {safhe + 1} , شب : {safhe + 2}", font=("Aviny", 22), fg="Black").pack()
                    if day == 21:
                        tk.Label(root, text="صفحه ی آخر : 604", font=("Aviny", 22), fg="black").pack()
                        tk.Label(root, text="=-" * 15, font=("Aviny", 22), fg="aqua").pack()
                        tk.Label(root, text="[ پایان ]", font=("Aviny", 22), fg="Purple").pack()
                    break
                day += 1
        tk.Label(root, text="لطفا روز را وارد کنید :", font=("Aviny", 22), fg="red").pack()
        spin_box = tk.Spinbox(root, from_=1, to=21, font=("Aviny", 22), fg="Blue", width=10)
        spin_box.pack(padx=5, pady=5)
        button = tk.Button(root, text="ارسال", font=("Aviny", 16), padx=15, bg="green", fg="white", command=spin_button)
        button.pack(pady=10)
root = tk.Tk()
root.geometry('300x800')
root.title('Mah Ha')

mah = tk.StringVar(value="None")
tk.Radiobutton(root, text="ماه 1", variable=mah, value=1, font=("Aviny", 28)).pack(pady=10)
tk.Radiobutton(root, text="ماه 2", variable=mah, value=2, font=("Aviny", 28)).pack(pady=10)
tk.Radiobutton(root, text="ماه 3", variable=mah, value=3, font=("Aviny", 28)).pack(pady=10)
tk.Radiobutton(root, text="ماه 4", variable=mah, value=4, font=("Aviny", 28)).pack(pady=10)
tk.Radiobutton(root, text="ماه 5", variable=mah, value=5, font=("Aviny", 28)).pack(pady=10)
tk.Radiobutton(root, text="ماه 6", variable=mah, value=6, font=("Aviny", 28)).pack(pady=10)
tk.Radiobutton(root, text="ماه 7", variable=mah, value=7, font=("Aviny", 28)).pack(pady=10)

button = tk.Button(root, text="ارسال", font=("Aviny", 24), bg="green", fg="white", command=button_click)
button.pack(pady=10)
root.mainloop()
