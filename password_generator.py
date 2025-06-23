import tkinter as tk
from tkinter import messagebox, filedialog
import string
import random
import pyperclip

# Password Strength Checker
def check_strength(length):
    if length <= 4:
        return 0  # Very Weak
    elif length <= 7:
        return 1  # Weak
    elif length <= 10:
        return 2  # Moderate
    elif length <= 13:
        return 3  # Strong
    else:
        return 4  # Very Strong
    
# Bar
def update_strength_bar(score):
    colors = ["red", "orange", "yellow", "lightgreen", "green"]
    texts = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    index = min(score, 4)
    bar["value"] = index * 20
    bar_label.config(text=texts[index], fg=colors[index])

# Password Generator Logic
def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Length must be a number.")
        return

    use_digits = digits_var.get()
    use_lower = lower_var.get()
    use_upper = upper_var.get()
    use_symbols = symbols_var.get()

    char_pool = ''
    if use_digits:
        char_pool += string.digits
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        char_pool = string.ascii_letters

    password = ''.join(random.choice(char_pool) for _ in range(length))
    result_var.set(password)
    toggle_button.config(state="normal")
    show_password()
    strength = check_strength(length)
    update_strength_bar(strength)

# Copy Password
def copy_password():
    password = result_var.get()
    if password:
        pyperclip.copy(password)
        top = tk.Toplevel(root)
        top.title("Copied")
        window_width = 200
        window_height = 80
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        top.geometry(f"{window_width}x{window_height}+{x}+{y}")
        top.resizable(False, False)
        top.configure(bg="#d1f7c4")
        tk.Label(top, text="✅ Password copied!", bg="#d1f7c4", font=("Helvetica", 11)).pack(pady=20)
        top.after(500, top.destroy)

# Save Password
def save_password():
    password = result_var.get()
    if not password:
        messagebox.showwarning("No Password", "Please generate a password first.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")], title="Save Password As")
    if file_path:
        try:
            with open(file_path, 'w') as f:
                f.write(password + "\n")
            messagebox.showinfo("Saved", f"Password saved to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Show/Hide Password
def show_password():
    entry.config(show="")
    toggle_button.config(text="🙈 Hide", command=hide_password)

def hide_password():
    entry.config(show="*")
    toggle_button.config(text="👁 Show", command=show_password)

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
window_width = 440
window_height = 460
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.resizable(False, False)
root.configure(bg="#2eebdb")

# Title
tk.Label(root, text="Secure Password Generator", font=("Helvetica", 16, "bold"), bg="#2eebdb").pack(pady=15)

# Input Frame
input_frame = tk.Frame(root, bg="#2eebdb")
input_frame.pack(pady=5)

tk.Label(input_frame, text="Password Length:", bg="#2eebdb", font=("Helvetica", 11)).grid(row=0, column=0, padx=5, sticky="e")
length_entry = tk.Entry(input_frame, width=10)
length_entry.grid(row=0, column=1, padx=5)

# Options Frame
options_frame = tk.Frame(root, bg="#2eebdb")
options_frame.pack(pady=5)

digits_var = tk.BooleanVar(value=False)
lower_var = tk.BooleanVar(value=False)
upper_var = tk.BooleanVar(value=False)
symbols_var = tk.BooleanVar(value=False)

tk.Checkbutton(options_frame, text="Include Digits", variable=digits_var, bg="#2eebdb").grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Include Lowercase", variable=lower_var, bg="#2eebdb").grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Include Uppercase", variable=upper_var, bg="#2eebdb").grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(options_frame, text="Include Symbols", variable=symbols_var, bg="#2eebdb").grid(row=3, column=0, sticky="w", padx=10)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Helvetica", 11), width=20).pack(pady=10)

# Result Entry + Toggle
result_var = tk.StringVar()
entry = tk.Entry(root, textvariable=result_var, font=("Courier", 12), justify="center", width=30, show="")
entry.pack(pady=5)

toggle_button = tk.Button(root, text="👁 Show", command=show_password, state="disabled")
toggle_button.pack(pady=2)

# Strength Meter
import tkinter.ttk as ttk
bar = ttk.Progressbar(root, length=200, mode='determinate', maximum=100)
bar.pack(pady=5)
bar_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#01141d")
bar_label.pack()

# Action Buttons
action_frame = tk.Frame(root, bg="#2eebdb")
action_frame.pack(pady=10)

tk.Button(action_frame, text="📋 Copy", command=copy_password, width=12, bg="#2196F3", fg="white").grid(row=0, column=0, padx=5)
tk.Button(action_frame, text="💾 Save", command=save_password, width=12, bg="#9C27B0", fg="white").grid(row=0, column=1, padx=5)

root.mainloop()