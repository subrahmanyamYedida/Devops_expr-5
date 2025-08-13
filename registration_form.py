import tkinter as tk
from tkinter import ttk

def submit_form():
    firstname = entry_firstname.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    contactnumber = entry_contactnumber.get()
    password = entry_password.get()
    gender = gender_var.get()
    result_label.config(
        text=f"Registration Form Successfully Created!\n"
             f"First Name: {firstname}\n"
             f"Last Name: {lastname}\n"
             f"Email: {email}\n"
             f"Contact Number: {contactnumber}\n"
             f"Password: {password}\n"
             f"Gender: {gender}",
        foreground="blue"
    )

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg="lightgreen")

# Labels
ttk.Label(root, text="First Name", foreground="purple").grid(row=0, column=0, padx=10, pady=5, sticky="w")
ttk.Label(root, text="Last Name", foreground="purple").grid(row=1, column=0, padx=10, pady=5, sticky="w")
ttk.Label(root, text="Email", foreground="purple").grid(row=2, column=0, padx=10, pady=5, sticky="w")
ttk.Label(root, text="Contact Number", foreground="purple").grid(row=3, column=0, padx=10, pady=5, sticky="w")
ttk.Label(root, text="Password", foreground="purple").grid(row=4, column=0, padx=10, pady=5, sticky="w")
ttk.Label(root, text="Gender", foreground="purple").grid(row=5, column=0, padx=10, pady=5, sticky="w")

# Entry widgets
entry_firstname = ttk.Entry(root)
entry_lastname = ttk.Entry(root)
entry_email = ttk.Entry(root)
entry_contactnumber = ttk.Entry(root)
entry_password = ttk.Entry(root, show="*")

entry_firstname.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_lastname.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_email.grid(row=2, column=1, padx=10, pady=5, sticky="w")
entry_contactnumber.grid(row=3, column=1, padx=10, pady=5, sticky="w")
entry_password.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Gender Combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, textvariable=gender_var, values=["Male", "Female"], state="readonly")
gender_combobox.set("Male")
gender_combobox.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Submit Button
style = ttk.Style()
style.configure("TButton", foreground="red")
submit_button = ttk.Button(root, text="Submit", command=submit_form, style="TButton")
submit_button.grid(row=6, column=0, columnspan=2, pady=10)

# Result Label
result_label = ttk.Label(root, text="", foreground="blue")
result_label.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
