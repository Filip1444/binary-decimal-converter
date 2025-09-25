import tkinter as tk

def center_window(window1, width, height):
    screen_width = window1.winfo_screenwidth()
    screen_height = window1.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window1.geometry(f"{width}x{height}+{x}+{y}")

def submission():
    binary = binaryEnter.get()
    if binary != "":
        binary=int(binary)
        decimal, power = 0, 0
        while binary:
            decimal += (binary % 10) * (2 ** power)
            binary //= 10
            power += 1
        outputDecimal.config(text=decimal)
    else:
        outputDecimal.config(text="")

    number = decimalEnter.get()
    if number != "":
        number=int(number)
        binary = ""
        while number > 0:
            binary = str(number % 2) + binary
            number //= 2
        outputbinary.config(text=binary)


window = tk.Tk()
main_frame = tk.Frame(window, bg="#8dc2c4")
main_frame.pack(expand=True)

title = tk.Label(
    main_frame,
    text="BINARY-DECIMAL CONVERTER",
    font=("bahnschrift semicondensed", 40),
    relief="solid",

)
title.grid(row=1, column=0, columnspan=3, ipadx=65, pady=20)

binaryPrompt = tk.Label(main_frame, text="ENTER BINARY:", justify="center", font=("bahnschrift semicondensed", 20), bg="#8dc2c4")
binaryPrompt.grid(row=2, column=0, sticky="s")

binaryEnter = tk.Entry(main_frame,justify="center", font=("bahnschrift semicondensed", 20), relief="solid", bd=2)
binaryEnter.grid(row=3, column= 0, padx=10, sticky="n", ipady=10)

decimalLabel = tk.Label(main_frame, text="DECIMAL:", justify="center", font=("bahnschrift semicondensed", 20), bg="#8dc2c4" )
decimalLabel.grid(row=4, column=0, sticky="s")

outputDecimal = tk.Label(
    main_frame,
    text="",
    background="white",
    font=("bahnschrift semicondensed", 20),
    width=binaryEnter.cget("width"),
    anchor="center",
    relief="solid",
)
outputDecimal.grid(row=5, column=0, sticky="n", ipady=10)

submit = tk.Button(
    main_frame,
    text = "SUBMIT",
    command = submission,
    font=("bahnschrift semicondensed", 20),
    relief="flat",
    bd=0,
    bg="white",
    fg="black",
    activebackground="white",
    activeforeground="black",
    height=1,
    width=10
)
submit.grid(row=3, column=2, )

decimalPrompt = tk.Label(main_frame, text="ENTER DECIMAL:", justify="center", font=("bahnschrift semicondensed", 20), bg="#8dc2c4")
decimalPrompt.grid(row=2, column=1, sticky="s")

decimalEnter = tk.Entry(main_frame, justify="center", font=("bahnschrift semicondensed", 20), relief="solid", bd=2)
decimalEnter.grid(row=3, column= 1, sticky="n", ipady=10)

binaryLabel= tk.Label(main_frame, text="BINARY:", justify="center", font=("bahnschrift semicondensed", 20), bg="#8dc2c4" )
binaryLabel.grid(row=4, column=1, sticky="s", )

outputbinary = tk.Label(
    main_frame,
    text="",
    background="white",
    font=("bahnschrift semicondensed", 20),
    width=decimalEnter.cget("width"),
    anchor="center",
    relief="solid",
)
outputbinary.grid(row=5, column=1, sticky="n", ipady=10)

window.iconbitmap("binary.ico")
center_window(window,1000, 550)
window.title("Binary converter")
window.config(background="#8dc2c4")
window.geometry("1000x500")
window.mainloop()