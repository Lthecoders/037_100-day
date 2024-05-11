# print("Hello Nikhil")

import os
import time

green = "\033[32m"
yellow = "\033[33m"
ceyen = "\033[35m"
blue = "\033[34m"
white = "\033[0m"
red = "\033[31m"
#
print(
    blue,
    "\n🤺⚔️ ----------------> Star Wars Name Generater <-----------------🤺⚔️",
    white)
print(ceyen, "                     <----------------------------->\n\n", white)
first_name = input("\nEnter your FIRST name ---> ").strip().title()
last_name = input("\n\nEnter your SURNAME name -----> ").strip().title()

first_3_first_name = first_name[0:3]
first_3_last_name = last_name[0:3]

together = f"{first_3_first_name}{first_3_last_name}".capitalize()
# print(f'''{green}\nthis is user's star wars first name "{together}{white}"''')

mothers_maiden_name = input(
    "\n\nEnter your Mom's maiden name -------------------> ").strip().title()

mothers_city_name = input(
    "\n\nEnter your Mom's city name where she was born ---->  ").strip().title(
    )

first_2_mother_maiden = mothers_maiden_name[0:2]
last_3_city = mothers_city_name[-3:]  # -3:  it means print last 3

mum_together = f"{first_2_mother_maiden}{last_3_city}"

os.system("clear")
print(yellow, "\n\n\nSaving your inputs....", white)
time.sleep(4)
os.system("clear")
print(
    blue,
    "\n🤺⚔️ ----------------> Star Wars Name Generater <-----------------🤺⚔️",
    white)
print(ceyen, "                     <----------------------------->\n", white)
print(
    f"{green}\n\n\n --------> Your Star Wars name is {together} {mum_together}{white}  🥵 😎 🔥"
)
