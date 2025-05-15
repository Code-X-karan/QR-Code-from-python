from tkinter import *
from tkinter import messagebox
import qrcode
window = Tk()
window.title("QR Code Generator")
window.geometry("400x500")
window.minsize(400, 550)
window.maxsize(400, 500)
user_input = StringVar()  #declare input variable
def submit():
    if user_input.get() == "":  ## check whether input is blank or not
        messagebox.showerror("QR Code Generator", "Input field can't be blank")  # if yes
    else:
        img = qrcode.make(user_input.get())  # if no
        img.show()
Label(window, text="QR Code Generator", font=("Calibri", 18, "bold")).pack(pady=(40, 10))  #main heading
Label(window, text="Enter a valid URL", font=("Calibri", 12)).pack(pady=(10, 7))  #sub heading
Entry(window, textvariable=user_input, width=50,relief="groove", font=("Arial", 10), bd=2 ).pack(pady=(5, 15))## input box
Button(window, text="Generate", command=submit, width=15, height=2, font=("Arial", 12, "bold"), bg="#12850c", fg="white", bd=0, relief="sunken").pack(pady=(10, 20))  ##button
window.mainloop()
