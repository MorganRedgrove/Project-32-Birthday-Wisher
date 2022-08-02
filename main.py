import datetime as dt
import pandas
from random import randint
import smtplib



list_birthday = []

add_birthday = input("Would you like to add any Birthdays today? y/n ")
if add_birthday == "y":
    list_birthday.append(input("name "))
    list_birthday.append(input("email "))
    list_birthday.append(input("year "))
    list_birthday.append(input("month "))
    list_birthday.append(input("day "))
    # print(list_birthday)

    df_birthday_read = pandas.read_csv("birthdays.csv")
    df_additions = pandas.Series(list_birthday, index=df_birthday_read.columns)


    df_birthday_write = df_birthday_read.append(df_additions, ignore_index=True)
    # print(df_birthday_write)

    with open("birthdays.csv", "w") as file:
        df_birthday_write.to_csv(file, index=False)

now = dt.datetime.now()
day = now.day
month = now.month

df_birthday_read = pandas.read_csv("birthdays.csv")
df_month = df_birthday_read[df_birthday_read.month == month]
df_today = df_month[df_month.day == day]

list = df_today.name.to_list()

for name_l in list:
    name = name_l
    email = df_today.email[df_today.name == name_l].to_string(index=False)

    num = randint(1,3)

    with open(f"letter_templates/letter_{num}.txt","r") as file:
        read = file.read()
    replace = read.replace("[NAME]", f"{name}")
    with open("letter.txt","w") as file:
        file.write(replace)
    with open("letter.txt","r") as file:
        text = file.read()

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="", password="")
    connection.sendmail(from_addr="",
                        to_addrs=email,
                        msg=f"Subject:Happy Birthday {name}!\n\n{text}")
    connection.close()