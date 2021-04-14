from tkinter import *
import random, string
from tkinter import messagebox

FONT = ("Helvetica", 14, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0, END)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for _ in range(0, 13):
        password += random.choice(characters)

    input_password.insert(0, password)
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = input_website.get()
    user_email = input_email_user.get()
    password = input_password.get()

    print(len(website))

    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Some information is missing. Please fill in all information")
    else:
        is_okay = messagebox.askokcancel(title=f"Information for {website}", message=f"There are the details entered:"
                                                                                     f"\n"f"Email: {user_email}"
                                                                                     f"\nPassword: {password}\n\n"
                                                                                     f"Is it okay to save?")
        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {user_email} | {password}\n")
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
background_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background_image)
canvas.grid(column=1, row=0)


# --- Labels --- #
label_website = Label(text="Website:", font=FONT)
label_website.grid(column=0, row=1)

label_email_user = Label(text="Email/Username:", font=FONT)
label_email_user.grid(column=0, row=2)

label_password = Label(text="Password:", font=FONT)
label_password.grid(column=0, row=3)

# --- Inputs --- #
input_website = Entry(width=37)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()

input_email_user = Entry(width=37)
input_email_user.grid(column=1, row=2, columnspan=2)
input_email_user.insert(0, "work@andysmith.is")

input_password = Entry(width=21)
input_password.grid(column=1, row=3)

# --- Buttons --- #
button_generate = Button(text="Generate Password", width=13, font=FONT, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", width=35, command=save)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()