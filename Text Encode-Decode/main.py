import random
import string
import tkinter as tk
from tkinter import messagebox

def encode(txt):
    l = txt.split(' ')
    for i in range(len(l)):
        if len(l[i]) < 3:
            new = l[i].lower()
            new = new[::-1]
            resF = ''.join(random.sample(string.ascii_lowercase, k=3))
            resE = ''.join(random.sample(string.ascii_lowercase, k=3))
            new = resF + new + resE
            l[i] = new
        else:
            new = l[i].lower()
            new = new[1:] + new[0]
            resF = ''.join(random.sample(string.ascii_lowercase, k=3))
            resE = ''.join(random.sample(string.ascii_lowercase, k=3))
            new = resF + new + resE
            l[i] = new
    txt = ' '.join(l)
    return txt

def decode(txt):
    l = txt.split(' ')
    for i in range(len(l)):
        if len(l[i]) < 3:
            new = l[i]
            new = new[3:-3]
            new = new[::-1]
            l[i] = new
        else:
            new = l[i]
            new = new[3:-3]
            new = new[-1] + new[:-1]
            l[i] = new
    txt = ' '.join(l)
    return txt

def on_encode():
    input_text = input_text_entry.get("1.0", tk.END).strip()
    if input_text:
        encoded_text = encode(input_text)
        output_text_entry.delete("1.0", tk.END)
        output_text_entry.insert(tk.END, encoded_text)
    else:
        messagebox.showwarning("Input Error", "Please enter text to encode.")

def on_decode():
    input_text = input_text_entry.get("1.0", tk.END).strip()
    if input_text:
        decoded_text = decode(input_text)
        output_text_entry.delete("1.0", tk.END)
        output_text_entry.insert(tk.END, decoded_text)
    else:
        messagebox.showwarning("Input Error", "Please enter text to decode.")

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("Text Encoder/Decoder")

input_label = tk.Label(root, text="Enter Text:")
input_label.pack()

input_text_entry = tk.Text(root, height=4, width=50)
input_text_entry.pack()

encode_button = tk.Button(root, text="Encode", command=on_encode)
encode_button.pack()

decode_button = tk.Button(root, text="Decode", command=on_decode)
decode_button.pack()

output_label = tk.Label(root, text="Output:")
output_label.pack()

output_text_entry = tk.Text(root, height=4, width=50)
output_text_entry.pack()

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack()

root.mainloop()
