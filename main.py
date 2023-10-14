import tkinter as tk

base = tk.Tk()

base.geometry("750x750")
base.title("Test")
base.configure(bg="grey")

label = tk.Label(base, text="Hello World!", font=('Arial', 25))
label.pack(padx=10, pady=10)

label2 = tk.Label(base, text="This is free text that does nothing", font=('Arial', 14))
label2.pack(padx=10, pady=10)

textbox = tk.Text(base, height=3, font=('Arial', 15))
textbox.pack(padx=10, pady=10)

label3 = tk.Label(base, text="Enter the path to the excel file you want to process", font=('Arial', 15))
label3.pack(padx=10, pady=10)

userEntry = tk.Entry(base)
userEntry.pack(padx=10, pady=10)

button = tk.Button(base, text="Click to Submit", font=('Arial', 15))
button.pack(padx=10, pady=10)

base.mainloop()