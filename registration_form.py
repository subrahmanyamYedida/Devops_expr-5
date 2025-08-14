import sys

# --- CLI MODE FOR JENKINS ---
def run_cli():
    print("Starting registration process (CLI mode)...")
    name = "John Doe"
    email = "john@example.com"
    password = "secure123"
    print(f"User Registered: {name}, Email: {email}")
    print("Registration completed successfully!")

# --- GUI MODE FOR LOCAL TESTING ---
def run_gui():
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.title("Registration Form")

    tk.Label(root, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1)

    tk.Label(root, text="Email").grid(row=1, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=1, column=1)

    tk.Label(root, text="Password").grid(row=2, column=0)
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=2, column=1)

    def register():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        messagebox.showinfo("Success", f"User Registered:\n{name}\n{email}")

    tk.Button(root, text="Register", command=register).grid(row=3, column=1)
    root.mainloop()

# --- MAIN ---
if __name__ == "__main__":
    # If "cli" argument is passed, run CLI mode (Jenkins)
    if len(sys.argv) > 1 and sys.argv[1] == "cli":
        run_cli()
    else:
        run_gui()

