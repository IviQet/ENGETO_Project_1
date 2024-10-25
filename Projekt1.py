'''
projekt_1.py = "První projekt do Engeto Online Python Akademie"
author = Ivana Květoňová
email = ivana.setmanukova@seznam.cz
discord = Ivana Q. #52959
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#new dictionary with registred users
reg_user = {
"bob": "123",
"ann": "pass123",
"mike": "password123",
"liz": "pass123"
}

#variables
nr_words = 0
tittle_words = []
nr_tittle_words = 0
tittle_whole_words = []
nr_tittle_whole_words = 0
lower_words = []
nr_lower_words = 0
numbers = []
nr_number = 0
suma = 0
words = []
len_word = {}

#enter name and password
user_name = input("Enter your username:")
password = input("Enter your password:")
print("-" * 40)

#condition of reg. user vs not reg. user
if user_name in reg_user.keys() and password in reg_user.values():
    print("Welcome to the app,", user_name)
    print("We have three texts to be analyzed")
    print("-" * 40)

    #text selection
    selected_text = input("Enter a number btw. 1 and 3 to select:")
    print("-" * 40) 
    if selected_text.isalpha():
        print("Please, enter the number:")
    elif int(selected_text) not in range(1,4): 
        print("Please, select the number from interval between 1 and 3!")
    #statistics
    else:
        words = TEXTS[(int(selected_text) - 1)].split()
        nr_words = len(words)
        print("There are", nr_words, "words in the selected text.")
        for word in words:
            if word[0].isupper():
                tittle_words.append(word)
                nr_tittle_words = len(tittle_words)
            elif word.isupper():
                tittle_whole_words.append(word)
                nr_tittle_whole_words = len(tittle_whole_words)
            elif word.islower():
                lower_words.append(word)
                nr_lower_words = len(lower_words)
            elif word.isnumeric():
                nr_number += 1
                numbers.append(int(word))
                suma = sum(numbers)
        print("There are", nr_tittle_words, "tittlecase words.")
        print("There are", nr_tittle_whole_words, "uppercase words.")
        print("There are", nr_lower_words, "lowercase words.")
        print("There are", nr_number, "numerics strings.")
        print("The sum of all the numbers is", suma)
    
    #diagram
    for word in words:
        length = len(word)
        if length > 0:
            if length in len_word:
                len_word[length] += 1
            else:
                len_word[length] = 1
    print("-" * 40) 
    print("LEN|", "OCCURENCES", "   |NR",)
    print("-" * 40) 
    for length, sum_words in sorted(len_word.items()):
        print(length,"|", "*"* sum_words,sum_words)
    print("-" * 40) 
else:
    print("Unregistred user, terminating the programm...")

