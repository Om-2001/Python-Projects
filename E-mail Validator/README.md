# Email Validator GUI

This repository contains a simple Python script that implements a basic email validation functionality using Tkinter, a standard Python GUI library.

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python and Tkinter installed.
3. Run the script `email_validator.py`.
4. Enter an email address in the provided input field.
5. Click the "Validate" button to check if the email address is valid.
6. The result will be displayed below the input field.

## Email Validation Rules

The script checks for the following criteria to consider an email address as valid:

1. The email address must have a length of at least 6 characters.
2. The first character must be a lowercase alphabet.
3. The email address must contain exactly one '@' symbol.
4. The '.' symbol must be present either at the 3rd last or 4th last position.
5. Only the following characters are allowed in the email address: lowercase alphabets (a-z), numbers (0-9), underscore (_), period (.), and '@'.

## Limitations

The code provided here is a basic email validation script and has several limitations:

1. **Limited Validation**: While the script checks for some basic email address rules, it does not cover all possible valid email formats. Advanced email validation requires a more comprehensive and complex regular expression pattern.
2. **No Domain Validation**: The script does not check if the domain of the email address is valid or exists.
3. **No MX Record Check**: The script does not perform an MX (Mail Exchange) record check to verify the existence of the domain's mail servers.
4. **No Real-Time Check**: The script only checks the validity of the email address based on the provided rules. It does not actually send an email to verify if it can be delivered.
5. **GUI Limitations**: The graphical user interface (GUI) is very basic and lacks any advanced design elements or error handling.

For a production-level email validation solution, consider using robust email validation libraries or services that can handle a wider range of email address formats and perform more rigorous checks to ensure the validity of email addresses.

## License

No License - This is an open-source project.

