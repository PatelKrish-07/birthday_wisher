import os
import random
import pandas
import datetime as dt
import smtplib
my_email =os.environ["MY_EMAIL"]
passwords=os.environ["MY_PASSWORD"]
now=dt.datetime.now(ZoneInfo("Asia/Kolkata"))
month=now.month
today=now.day
birth=(month,today)
birthdays = pandas.read_csv("birthdays.csv")
bd = {(row.month,row.day):row for (index,row) in birthdays.iterrows()}
if birth in bd:
    pick = random.randint(1,3)
    with open(f"./letter_templates/letter_{pick}.txt") as file:
        content=file.read()
        content=content.replace("[NAME]",bd[birth]["name"])
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()  # securing connection
        connection.login(user=my_email, password=passwords)
        connection.sendmail(from_addr=my_email, to_addrs=f"{bd[birth]["email"]}", msg="Subject:Birthday Wish \n\n"
                                                                                          f"{content}")









