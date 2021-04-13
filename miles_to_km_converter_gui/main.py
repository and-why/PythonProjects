import tkinter as tk


window = tk.Tk()
window.title("Mile to KM converter")
window.config(padx=10, pady=10)


# TODO create 4 labels

label_miles = tk.Label(text="Miles")
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

label_km = tk.Label(text="Km")
label_km.grid(column=2, row=2)
label_km.config(padx=10, pady=10)

label_answer = tk.Label(text="0.0")
label_answer.grid(column=1, row=2)
label_answer.config(padx=10, pady=10, font=("Helvetica", 24, "bold"))

label_equal_to = tk.Label(text="is equal to")
label_equal_to.grid(column=0, row=2)
label_equal_to.config(padx=10, pady=10)

direction = "mtok"

# TODO create an Entry for the conversion, convert to integer
def calculate_conversion():
    if direction == "mtok":
        entry = float(entry_data.get())
        answer = round((entry * 1.60934), 1)
        label_answer.config(text=answer)
    else:
        entry = float(entry_data.get())
        answer = round((entry / 1.60934), 1)
        label_answer.config(text=answer)

def swap_conversion():
    global direction
    if direction == "mtok":
        direction = "other"
        label_km.grid(column=2, row=0)
        label_miles.grid(column=2, row=2)
        calculate_conversion()
    else:
        direction = "mtok"
        label_km.grid(column=2, row=2)
        label_miles.grid(column=2, row=0)
        calculate_conversion()


entry_data = tk.Entry(width="10", justify="left")
entry_data.insert(tk.END, string="0")
entry_data.grid(column=1, row=0)

#  function to convert value and config to one of the labels

conversion_button = tk.Button(text="Convert", command=calculate_conversion)
conversion_button.grid(column=1, row=3)
conversion_button.config(font=("Helvetica", 24, "bold"))


swap_function_button = tk.Button(text="SWAP", command=swap_conversion)
swap_function_button.grid(column=2, row=1)







window.lift()
window.call('wm', 'attributes', '.', '-topmost', '1')
window.mainloop()