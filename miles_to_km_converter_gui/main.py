import tkinter as tk


window = tk.Tk()
window.title("Mile to KM converter")
# window.minsize(400,300)


# TODO create 4 labels

label_miles = tk.Label(text="Miles")
label_miles.grid(column=2, row=0)
label_miles.config(padx=10, pady=10)

label_km = tk.Label(text="Km")
label_km.grid(column=2, row=1)
label_km.config(padx=10, pady=10)

label_answer = tk.Label(text="0.0")
label_answer.grid(column=1, row=1)
label_answer.config(padx=10, pady=10, font=("Helvetica", 24, "bold"))

label_equal_to = tk.Label(text="is equal to")
label_equal_to.grid(column=0, row=1)
label_equal_to.config(padx=10, pady=10)


# TODO create an Entry for the conversion, convert to integer
def calculate_conversion():
    entry = int(entry_data.get())
    answer = round((entry * 1.60934), 1)
    label_answer.config(text=answer)


entry_data = tk.Entry(width="10", justify="left")
entry_data.insert(tk.END, string="0")
entry_data.grid(column=1, row=0)

# TODO function to convert value and config to one of the labels

conversion_button = tk.Button(text="Convert", command=calculate_conversion, width="10")
conversion_button.grid(column=1, row=2)
conversion_button.config(padx=10, pady=10, font=("Helvetica", 24, "bold"))










window.lift()
window.call('wm', 'attributes', '.', '-topmost', '1')
window.mainloop()