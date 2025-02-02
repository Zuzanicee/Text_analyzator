TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
    """At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
"""]
#registrovaní uživatelé
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
#pokyn pro vyplnění přihlašovacích údajů
username = input("username: ")
password = input("password: ")
#ověření správnosti přihlašovacích údajů
if username in users and users[username] == password: 
    print("-"*50)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-"*50)
else:
    print("Unregistered user, ending app..")
    exit()
#pokyn pro výběr textu
choosen_text = 0
for number in range(3):
    choice = input(f"Enter a number btw. 1 and {len(TEXTS)} texts to select: ") #len(TEXTS) jsem zadala, kdyby se změnil počet textů
    if not choice.isdigit():
        print(f"{choice} is not a number. Ending app...")
        exit()
    choice = int(choice)
    if choice < 1 or choice > len(TEXTS):
        print(f"{choice} is not btw numbers 1 and {len(TEXTS)} Ending app...")
        exit()
    else:
        choosen_text = TEXTS[choice - 1]
    break
#odpovědi na otázky v zadání
splited_text = choosen_text.split()
splited_text_clear = [word.strip(',:.?!') for word in splited_text] #slova s pomlčkou beru jako jedno slovo
numbers_of_length = [len(word) for word in splited_text_clear]
title_case = [word for word in splited_text_clear
              if word.istitle() and word.isalpha()]
upper_case = [word for word in splited_text_clear
              if word.isupper() and word.isalpha()]
lower_case = [word for word in splited_text_clear
              if word.islower() and word.isalpha()]
numeric = [word for word in splited_text_clear
           if word.isnumeric()]
numeric_int = [int(number) for number in numeric]
num_words = len(splited_text_clear)
titlecase_words = len(title_case)
uppercase_words = len(upper_case)
lowercase_words = len(lower_case)
numeric_strings = len(numeric)
numbers_sum = sum(numeric_int)
#výpis odpovědí na zadání
print(f"{'-'*50}")
print(f"There are {num_words} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_strings} numeric strings.")
print(f"The sum of all the numbers: {numbers_sum}")
print(f"{'-'*50}")
length_count = {}
for length in numbers_of_length:
    length_count[length] = length_count.get(length, 0) + 1
#graf
print(f"LEN|  OCCURENCES  |NR.")
print(f"{'-'*50}")
for length in sorted(length_count.keys()):
    print(f" {length:>2}|{'*' * length_count[length]}{' ' * (12 - length_count[length])}|{length_count[length]}")