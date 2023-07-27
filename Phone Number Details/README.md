# Phone Number Details Application

This repository contains a simple Python application that allows users to enter a phone number (Indian numbers only) and retrieve various details related to the phone number. The application is built using the Tkinter library for the graphical user interface and the phonenumbers library to validate and extract information from the phone number.

## Features

The phone number details application offers the following features:

1. Input Validation: The application checks whether the provided phone number is numeric or not. It only accepts numeric inputs.

2. Number Formatting: The input phone number is formatted using the phonenumbers library to ensure it follows the standard international format.

3. Number Validation: The application verifies whether the formatted phone number is a possible and valid number for India using the phonenumbers library.

4. Information Retrieval: If the phone number is possible and valid, the application retrieves the following details:
   - Region: The geographical region associated with the phone number.
   - Timezone: The timezone in which the phone number is registered.
   - Carrier: The name of the carrier or telecom operator associated with the phone number.

## How to Use

1. Clone the Repository: Clone this repository to your local machine.

2. Install Dependencies: The application relies on the `tkinter` and `phonenumbers` libraries. Make sure you have them installed. If not, you can install them using `pip`.

3. Run the Application: Navigate to the project directory and run the `main.py` script.

4. Enter a Phone Number: The application will prompt you to enter a phone number. Please provide a numeric phone number without any spaces or special characters.

5. Click Submit: After entering the phone number, click the "Submit" button to retrieve the details.

6. View Results: If the provided phone number is valid and possible, a message box will display the details, including the region, timezone, and carrier. Otherwise, an appropriate message will be shown for invalid or impossible phone numbers.

## Limitations

This phone number details application has the following limitations:

1. Only Indian Numbers: The application is specifically designed to handle Indian phone numbers. It may not work as intended for phone numbers from other countries.

2. Basic Functionality: The application offers basic functionality to validate and retrieve details of Indian phone numbers. It does not include more advanced features such as live API lookups or extensive error handling.

3. Graphical User Interface: The application uses Tkinter to create a simple GUI for user interaction. However, the GUI design is minimal and may not have an appealing appearance.

4. Single Number Input: The application allows users to enter and check details for only one phone number at a time. It does not support batch processing or handling multiple numbers simultaneously.

