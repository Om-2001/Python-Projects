import tkinter as tk
def val_email(email):
  flag = False
  allowed_val = "abcdefghijklmnopqrstuvwxyz0123456789_.@"
  if len(email) >= 6:
    if email[0].isalpha():
      if ('@' in email) and (email.count('@') == 1):
        if (email[-3] == '.') ^ (email[-4] == '.'):
          for i in email:
            if i in allowed_val and email.isspace() == False:
              pass
            else:
              flag = True
              break
          if flag == False:
            return "Valid Email"
          else:
            return "Restricted Values or Space Used"
        else:
          return "\".\" must be present on 3rd last OR 4th last char"
      else:
        return "@ Must Be Present and Count of It Must Be 1"
    else:
      return "1st Char Must Be Lower Alphabet"
  else:
    return "Length Of Mail Must Be AtLeast 6"

def check_email():
    email = entry_email.get()
    result = val_email(email)
    label_result.config(text=result)

# Create the main Tkinter window
root = tk.Tk()
root.title("Email Validator")

# Design the GUI elements
label_email = tk.Label(root, text="Enter Email Address:")
label_email.pack(pady=10)

entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

button_validate = tk.Button(root, text="Validate", command=check_email)
button_validate.pack(pady=5)

label_result = tk.Label(root, text="", fg="red")
label_result.pack(pady=10)

# Run the Tkinter main event loop
root.mainloop()
