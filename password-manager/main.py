from tkinter import *
import random, string
from tkinter import messagebox
import json

FONT = ("Helvetica", 14, "normal")


# ---------------------------------- SEARCH ------------------------------------- #
def search():
    search_query = input_website.get().lower()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            item = data[search_query]
    except KeyError:
        messagebox.showinfo(title="Oops", message=f"No details for {search_query} doesn't exist in the database")
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data found. Please add your first Email/Username and Password")
    else:
        messagebox.showinfo(title=search_query, message=f"Email: {item['email']}\n"
                                                        f"Password: {item['password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    input_password.delete(0, END)
    symbols = "/,.?[]{};:!@€#$%^&*()"
    characters = string.ascii_letters + string.digits + symbols

    password = ""
    for _ in range(0, 13):
        password += random.choice(characters)

    input_password.insert(0, password)
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = str(input_website.get().lower())
    user_email = str(input_email_user.get())
    password = str(input_password.get())
    new_data = {website: {
        "email": user_email,
        "password": password
    }}

    if len(website) == 0 or len(user_email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Some information is missing. Please fill in all information")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
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
input_website = Entry(width=21)
input_website.grid(column=1, row=1)
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

button_search = Button(text="Search", width=13, font=FONT, command=search)
button_search.grid(column=2, row=1)


window.mainloop()