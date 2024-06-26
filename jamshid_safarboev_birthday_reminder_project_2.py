# -*- coding: utf-8 -*-
"""Jamshid_Safarboev_Birthday_reminder_project_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-85S6Ot1R_udg7JwrT6x-bfqgmRy-qjN
"""

import csv  # I imported the CSV module for handling CSV files
from abc import ABC, abstractmethod  # it is importing ABC (Abstract Base Class) and abstractmethod for defining abstract classes and methods
import datetime  # We are importing the datetime module for working with dates and times
#Polymorphism: This is when a subclass provides a different implementation of a method that is already provided by its parent class. In your code, the send_notification and print_reminders methods in the Reminder class are overridden in the BirthdayReminder class. Also, the EmailNotificationDecoratorclass overrides the send_notification method
class Reminder(ABC):  # Defining an abstract base class Reminder
    @abstractmethod  # it is a decorator to define an abstract method
    def send_notification(self):  # Abstract method to send notifications
        pass

    @abstractmethod  # Decorator to define another abstract method
    def print_reminders(self):  # Abstract method to print reminders
        pass

class BirthdayReminder(Reminder):  # Define a concrete class BirthdayReminder that inherits from Reminder
    def __init__(self, user):  # Constructor method
        self.user = user  # we are nitializing the user attribute with the provided user name
        self.birthdays = {}  # we are initializing an empty dictionary to store birthdays

    def add_birthday(self, name, date):  # Method to add a birthday to the reminders
        self.birthdays[name] = date  # Add the provided name and date to the birthdays dictionary

    def remove_birthday(self, name):  # Method to remove a birthday from the reminders
        if name in self.birthdays:  # We can check if the name exists in the birthdays dictionary
            del self.birthdays[name]  # If yes, delete the birthday associated with the name

    def print_reminders(self):  # Method to print all reminders
        """Prints all birthdays."""
        for name, date in self.birthdays.items():  # Iterate through the birthdays dictionary
            print(f"{name}'s birthday is on {date}")  # Print each name and associated birthday date

    def send_notification(self):  # Method to send notifications for birthdays
        """Sends notifications for birthdays today."""
        today = datetime.date.today()  # we can get the current date
        for name, date in self.birthdays.items():  # we can iterate by the birthdays dictionary
            b_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()  # Convert the birthday date string to a date object
            if b_date.month == today.month and b_date.day == today.day:  # we are checking if the birthday is today
                print(f"Notification: Today is {name}'s birthday!")  # If it is yes, it prints a notification message

class ReminderFactory:  # Define a class to create reminder objects
    @staticmethod  # Decorator to define a static method
    def create_reminder(reminder_type, user):  # Static method to create a reminder based on type
        if reminder_type == "Birthday":  # we check if the reminder type is "Birthday"
            return BirthdayReminder(user)  # If it is yes, it creates a BirthdayReminder object with the provided user name
        else:  # If the reminder type is not recognized
            raise ValueError("Invalid reminder type")  # Raise a ValueError indicating an invalid reminder type

class CSVHandler:  # We are defining a class to handle CSV file operations
    @staticmethod  # Shows decorator to define a static method
    def export_to_csv(filename, data):  # Static method to export data to a CSV file
        with open(filename, 'w', newline='') as file:  # Open the file in write mode, 'w' means write
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerows(data)  # Write all rows of data to the CSV file

    @staticmethod  # Decorator to define another static method
    def import_from_csv(filename):  # Static method to import data from a CSV file
        data = []  # Initialize an empty list to store imported data
        with open(filename, 'r') as file:  # Open the file in read mode, 'r' means read
            reader = csv.reader(file)  # Create a CSV reader object
            for row in reader:  # Iterate through each row in the CSV file
                data.append(row)  # Append the row to the data list
        return data  # Return the imported data

class EmailNotificationDecorator(Reminder):  # Define a decorator class EmailNotificationDecorator inheriting from Reminder
    def __init__(self, wrapped_reminder):  # Constructor method with a parameter wrapped_reminder
        self.wrapped_reminder = wrapped_reminder  # Assign the wrapped reminder object to an attribute

    def send_notification(self):  # Method to send notifications
        self.wrapped_reminder.send_notification()  # Call the original send_notification method of the wrapped reminder object
        self.send_email_notification()  # Call the custom send_email_notification method

    def send_email_notification(self):  # Method to send email notifications
        # Implement email notification functionality here
        print("Email notification sent for birthdays today")  # Print a notification message for sending email

# Examples for the test
reminder = ReminderFactory.create_reminder("Birthday", "Leyla")  # We are reating a BirthdayReminder object for user "Leyla"
reminder.add_birthday('James', '2000-05-10')  # Adding James's birthday to the reminder
reminder.add_birthday('Leyla', '2001-06-15')  # Adding Leyla's birthday to the reminder

reminder.print_reminders()  # Printing all reminders
reminder.send_notification()  # Sending notifications for today's birthdays

data_to_export = [['James', '2000-05-10'], ['Leyla', '2001-06-15']]  # Sample data to export to CSV
CSVHandler.export_to_csv('reminders.csv', data_to_export)  # Exporting data to a CSV file

imported_data = CSVHandler.import_from_csv('reminders.csv')  # we are importing data from the CSV file
print(imported_data)  # Print the imported data

"""```python
import csv  # I imported the CSV module for handling CSV files
from abc import ABC, abstractmethod  # it is importing ABC (Abstract Base Class) and abstractmethod for defining abstract classes and methods
import datetime  # We are importing the datetime module for working with dates and times

class Reminder(ABC):  # Defining an abstract base class Reminder
    @abstractmethod  # it is a decorator to define an abstract method
    def send_notification(self):  # Abstract method to send notifications
        pass

    @abstractmethod  # Decorator to define another abstract method
    def print_reminders(self):  # Abstract method to print reminders
        pass

class BirthdayReminder(Reminder):  # Define a concrete class BirthdayReminder that inherits from Reminder
    def init(self, user):  # Constructor method
        self.user = user  # we are initializing the user attribute with the provided user name
        self.birthdays = {}  # we are initializing an empty dictionary to store birthdays

    def add_birthday(self, name, date):  # Method to add a birthday to the reminders
        self.birthdays[name] = date  # Add the provided name and date to the birthdays dictionary

    def remove_birthday(self, name):  # Method to remove a birthday from the reminders
        if name in self.birthdays:  # We can check if the name exists in the birthdays dictionary
            del self.birthdays[name]  # If yes, delete the birthday associated with the name

    def print_reminders(self):  # Method to print all reminders
        '''Prints all birthdays.'''
        for name, date in self.birthdays.items():  # Iterate through the birthdays dictionary
            print(f"{name}'s birthday is on {date}")  # Print each name and associated birthday date

    def send_notification(self):  # Method to send notifications for birthdays
        '''Sends notifications for birthdays today.'''
        today = datetime.date.today()  # we can get the current date
        for name, date in self.birthdays.items():  # we can iterate by the birthdays dictionary
            b_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()  # Convert the birthday date string to a date object
            if b_date.month == today.month and b_date.day == today.day:  # we are checking if the birthday is today
                print(f"Notification: Today is {name}'s birthday!")  # If it is yes, it prints a notification message

class ReminderFactory:  # Define a class to create reminder objects
    @staticmethod  # Decorator to define a static method
    def create_reminder(reminder_type, user):  # Static method to create a reminder based on type
        if reminder_type == "Birthday":  # we check if the reminder type is "Birthday"
            return BirthdayReminder(user)  # If it is yes, it creates a BirthdayReminder object with the provided user name
        else:  # If the reminder type is not recognized
            raise ValueError("Invalid reminder type")  # Raise a ValueError indicating an invalid reminder type

class CSVHandler:  # we are defining a class to handle CSV file operations
    @staticmethod  # Shows decorator to define a static method
    def export_to_csv(filename, data):  # Static method to export data to a CSV file
        with open(filename, 'w', newline='') as file:  # Open the file in write mode, 'w' means write
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerows(data)  # Write all rows of data to the CSV file

    @staticmethod  # Decorator to define another static method
    def import_from_csv(filename):  # Static method to import data from a CSV file
        data = []  # Initialize an empty list to store imported data
        with open(filename, 'r') as file:  # Open the file in read mode, 'r' means read
            reader = csv.reader(file)  # Create a CSV reader object
            for row in reader:  # Iterate through each row in the CSV file
                data.append(row)  # Append the row to the data list
        return data  # Return the imported data

class EmailNotificationDecorator(Reminder):  # Define a decorator class EmailNotificationDecorator inheriting from Reminder
    def init(self, wrapped_reminder):  # Constructor method with a parameter wrapped_reminder
        self.wrapped_reminder = wrapped_reminder  # Assign the wrapped reminder object to an attribute

    def send_notification(self):  # Method to send notifications
        self.wrapped_reminder.send_notification()  # Call the original send
"""

# We import the unittest module. This is a built-in Python module for writing and running tests.
import unittest

# We import the io and sys modules, which provide tools for working with input/output in Python, and the contextlib module, which provides utilities for working with context managers.
import io
import sys
from contextlib import redirect_stdout

# We define a new test case class TestBirthdayReminder. This class inherits from unittest.TestCase, which means it's a test case that can be run by the unittest test runner.
class TestBirthdayReminder(unittest.TestCase):

    # The setUp method is a special method that is run before each test. Here, we use it to create a new BirthdayReminder instance that will be used in the tests.
    def setUp(self):
        self.reminder = BirthdayReminder('User1')

    # This is a test method. Each method in a TestCase subclass that starts with "test_" is a test that will be run by the test runner.
    def test_add_birthday(self):
        # We call the add_birthday method of the BirthdayReminder instance, and then check that the birthday was added correctly.
        self.reminder.add_birthday('John Doe', '2000-01-01')
        self.assertEqual(self.reminder.birthdays['John Doe'], '2000-01-01')

    # This is another test method. It tests the remove_birthday method.
    def test_remove_birthday(self):
        # We add a birthday, remove it, and then check that it was removed correctly.
        self.reminder.add_birthday('John Doe', '2000-01-01')
        self.reminder.remove_birthday('John Doe')
        self.assertNotIn('John Doe', self.reminder.birthdays)

    # This test method tests the print_reminders method.
    def test_print_reminders(self):
        # We add a birthday, and then check that the print_reminders method prints it correctly.
        self.reminder.add_birthday('John Doe', '2000-01-01')
        expected_output = "John Doe's birthday is on 2000-01-01\n"
        # We use the io.StringIO class to create a "file-like" object that we can use to capture the output of the print_reminders method.
        with io.StringIO() as buf, redirect_stdout(buf):
            self.reminder.print_reminders()
            output = buf.getvalue()
        # We check that the output of the print_reminders method matches the expected output.
        self.assertEqual(output, expected_output)

    # This test method tests the send_notification method.
    def test_send_notification(self):
        # We add a birthday for today, and then check that the send_notification method sends a notification for it.
        today = datetime.date.today().strftime('%Y-%m-%d')
        self.reminder.add_birthday('John Doe', today)
        expected_output = f"Notification: Today is John Doe's birthday!\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            self.reminder.send_notification()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

# We create a TestSuite object that includes all the tests from the TestBirthdayReminder test case.
suite = unittest.TestLoader().loadTestsFromTestCase(TestBirthdayReminder)

# We create a TextTestRunner object and use it to run the test suite.
unittest.TextTestRunner().run(suite)

