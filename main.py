
import random
import pandas
import datetime as dt
import smtplib
my_email ="krish260659@gmail.com"
password="ehpczzdhihtrckpo"
# 1. Update the birthdays.csv
now=dt.datetime.now()
month=now.month
today=now.day
birth=(month,today)
birthdays = pandas.read_csv("birthdays.csv")
bd = {(row.month,row.day):row for (index,row) in birthdays.iterrows()}
print(bd)
if birth in bd:
    pick = random.randint(1,3)
    with open(f"./letter_templates/letter_{pick}.txt") as file:
        content=file.read()
        content=content.replace("[NAME]",bd[birth]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # securing connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=f"{bd[birth]["email"]}", msg="Subject:Birthday Wish \n\n"
                                                                                          f"{content}")




# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




