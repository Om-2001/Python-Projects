import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

# Function to generate the QR code
def generate_qr():
    data = data_entry.get().strip()
    filename = filename_entry.get().strip()

    if not data or not filename:
        messagebox.showerror("Error", "Data and Filename fields are required.")
        return

    fill_color = fill_color_entry.get().strip() or "black"
    bg_color = bg_color_entry.get().strip() or "white"

    qr = qrcode.QRCode(version=1, 
                       error_correction = qrcode.constants.ERROR_CORRECT_H, 
                       box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color=fill_color, back_color=bg_color)

    qr_filename = f"{filename}.png"
    qr_image.save(qr_filename)

    image = Image.open(qr_filename)
    image.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(image)

    qr_label.configure(image=photo)
    qr_label.image = photo

    messagebox.showinfo("Success", "QR code generated successfully.")

# Create the Tkinter window
window = tk.Tk()
window.title("QR Code Generator")
window.geometry("650x550")

# Create and position the input fields and labels
data_label = tk.Label(window, text="Data:")
data_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
data_entry = tk.Entry(window, width=40)
data_entry.grid(row=0, column=1, padx=10, pady=5)

filename_label = tk.Label(window, text="Filename:")
filename_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
filename_entry = tk.Entry(window, width=40)
filename_entry.grid(row=1, column=1, padx=10, pady=5)

fill_color_label = tk.Label(window, text="Fill Color (optional):")
fill_color_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
fill_color_entry = tk.Entry(window, width=40)
fill_color_entry.grid(row=2, column=1, padx=10, pady=5)

bg_color_label = tk.Label(window, text="Background Color (optional):")
bg_color_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
bg_color_entry = tk.Entry(window, width=40)
bg_color_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and position the generate button
generate_button = tk.Button(window, text="Generate QR", command=generate_qr)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Create and position the QR image label
qr_label = tk.Label(window)
qr_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()







