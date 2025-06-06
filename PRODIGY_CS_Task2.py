import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os

def encrypt_decrypt_image(path, key, output_path):
    img = Image.open(path)
    data = np.array(img)

    # Apply XOR operation
    encrypted_data = data ^ key

    result = Image.fromarray(encrypted_data.astype('uint8'))
    result.save(output_path)
    return output_path

def browse_file():
    file_path.set(filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]))
    if file_path.get():
        load_preview(file_path.get())

def load_preview(image_path):
    try:
        img = Image.open(image_path)
        img.thumbnail((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        preview_label.config(image=img_tk)
        preview_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Error", f"Could not open image: {e}")

def perform_operation(mode):
    path = file_path.get()
    try:
        key_value = int(key.get())
        if not path or not os.path.exists(path):
            messagebox.showerror("Error", "No valid image selected.")
            return

        filename = os.path.basename(path)
        name, ext = os.path.splitext(filename)

        output_filename = f"{name}_{mode}{ext}"
        output_path = os.path.join(os.path.dirname(path), output_filename)

        result_path = encrypt_decrypt_image(path, key_value, output_path)
        messagebox.showinfo("Success", f"{mode.title()}ion complete. Saved as:\n{result_path}")
        load_preview(result_path)
    except ValueError:
        messagebox.showerror("Error", "Key must be an integer.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
app = tk.Tk()
app.title("Image Encryption/Decryption")
app.geometry("400x450")
app.resizable(False, False)

file_path = tk.StringVar()
key = tk.StringVar()

# Widgets
tk.Label(app, text="Image Encryption Tool", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Button(app, text="Browse Image", command=browse_file).pack(pady=5)
tk.Entry(app, textvariable=file_path, width=45, state='readonly').pack(pady=5)

tk.Label(app, text="Enter Key (integer):").pack(pady=5)
tk.Entry(app, textvariable=key).pack(pady=5)

tk.Button(app, text="Encrypt Image", bg="#4CAF50", fg="white", command=lambda: perform_operation("encrypt")).pack(pady=10)
tk.Button(app, text="Decrypt Image", bg="#f44336", fg="white", command=lambda: perform_operation("decrypt")).pack(pady=5)

preview_label = tk.Label(app)
preview_label.pack(pady=10)

app.mainloop()