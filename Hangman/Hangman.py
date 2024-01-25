import random

print("Hangman!\n") 

themes_list = {"Theme 1" : "Stationary", "Theme 2" : "Computational terms", "Theme 3" : "Human Anatomy ", "Theme 4" : "Seasonal Aspects"}

rules = {"Rule 1" : "All words entered have to start with a captital letter, unless stated otherwise", 
         "Rule 2" : "Words like 'small toy', do include a space in between [, ' ',]",
         "Rule 3" : "Have FUN !!!"
         }

print(f"{rules}\n")

print(f"{themes_list}\n")

theme = input("Choose a theme: ")

themes_1 = open("Stationary.txt", 'r')
stationary = themes_1.readlines()
    
theme_1 = []
for line in stationary:
    theme_1.append(line.strip()) # removes "/n"
    
random.shuffle(theme_1)
      
###### Theme 2   
        
themes_2 = open("Computational_terms.txt", 'r')
computational_terms = themes_2.readlines()
    
theme_2 = []
for line in computational_terms:
    theme_2.append(line.strip()) # removes "/n"

random.shuffle(theme_2)    
     
########## Theme 3

themes_3 = open("Human_Anatomy.txt", 'r')
human_anatomy = themes_3.readlines()
    
theme_3 = []
for line in human_anatomy:
    theme_3.append(line.strip()) # removes "/n"
    
random.shuffle(theme_3)    

######## Theme 4

themes_4 = open("Seasonal_Aspects.txt", 'r')
seasonal_aspects = themes_4.readlines()
    
theme_4 = []
for line in seasonal_aspects:
    theme_4.append(line.strip()) # removes "/n"
    
random.shuffle(theme_4)   

theme_dict = {}
theme_dict.update({"Theme 1" : theme_1, "Theme 2" : theme_2, "Theme 3" : theme_3, "Theme 4" : theme_4,})

theme_keys = theme_dict.keys()

theme_key_list = []
for key in theme_keys:
    theme_key_list.append(key)



while True:
    if not theme in theme_key_list:
        print("ValueError: Theme not found. The categories are case sensitive, did you mean Theme _ instead of theme _?\n")
        theme = input("Choose a theme: ")
    else:
        break

theme_value = theme_dict[theme]

random_word =random.choice(theme_value)

split_word = list(random_word)

word = []

for letter in split_word:
    word.append(letter)

start = input("\nPress 's' to start: ")

while True:
    if start != "s":
        print("Error : Press 's' to start.")
        start = input("\nPress 's' to start: ")
    else:
        break



wordlist = ['' for _ in word]

word_ans = "".join(word)

guess_counter = 8


while guess_counter > 0:

    letter_choice = input("\nChoose a letter: ") 
    while True:
        if not len(letter_choice) == 1 and letter_choice.isalpha():
            print("ValueError: Enter one LETTER at a time.")
            letter_choice = input("\nChoose a letter: ")
        else:
            break
    
    guess_in_list = False
   
    for i in range(len(letter_choice)):
        if letter_choice[i] in word:
            # add the letter to the new list at the same index as the constant list
            wordlist[word.index(letter_choice[i])] = letter_choice[i]
            indices = [j for j, x in enumerate(word) if x == letter_choice[i]]
            for index in indices:
                wordlist[index] = letter_choice[i]
            guess_in_list = True

    
    
    print(wordlist)

    
    # check if all letters are guessed
    if all(letter in wordlist for letter in word):
        print(f"\nCongratulations! You WIN. Your word is {word_ans}\n")
        break
     
    if not guess_in_list:
        guess_counter -= 1
        print(f"\nYou have {guess_counter} try/tries left.")

    if guess_counter <= 0:
        print("Sorry, you've run out of guesses.")
        print(f"The word was {word_ans}.")
        break

