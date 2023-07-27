import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def num_details(num):
  if num.isnumeric():
    num_format = phonenumbers.parse(num, "IN")
    possible = phonenumbers.is_possible_number(num_format)
    if possible:
        valid = phonenumbers.is_valid_number(num_format)
        if valid:
            region = geocoder.description_for_number(num_format, 'en')
            timezone_info = timezone.time_zones_for_number(num_format)
            carrier_name = carrier.name_for_number(num_format, 'en')
            details = f"Number : {num_format}\nPossible : YES\nValid : YES\nRegion : {region}\nTimezone : {timezone_info}\nCarrier : {carrier_name}"
            return details
        else:
            return "Number is Possible But Not Valid"
    else:
        return "Not A Possible Number"
  else:
    return "Enter only Numeric Number"
    
def on_submit():
    phone_number = entry.get()
    result = num_details(phone_number)
    messagebox.showinfo("Number Details", result)

# Create the main window
root = tk.Tk()
root.title("Phone Number Details")

# Create and place widgets
label = tk.Label(root, text="Enter a phone number (India only):")
label.pack(pady=10)

entry = tk.Entry(root, width=20)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

# Run the main event loop
root.mainloop()
