from datetime import datetime
import pandas
import random
import smtplib

# email login information
email = "" # <- TYPE YOUR EMAIL BEWTEEN THE " "
password = "" # <- TYPE YOUR PASSWORD BEWTEEN THE " "

# Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

# Using pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Using dictionary comprehension to create a dictionary from birthday.csv
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


#Compare and see if today's month/day tuple matches one of the keys in birthday_dict
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# Send the letter generated to that person's email address.
    with smtplib.SMTP("") as connection: # <- TYPE YOUR EMAIL PROVIDERS SMTP SERVER ADDRESS HERE *NOTE: FOR GMAIL USE:("smtp.gmail.com", 587)*
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
