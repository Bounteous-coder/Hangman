import random
stages = ['''
      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |      | |
     |
    _|___
    
 ''','''
      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |      | 
     |
    _|___

 ''','''
      _______
     |/      |
     |      (_)
     |     --|--
     |       |
     |      
     |
    _|___

 ''','''
      _______
     |/      |
     |      (_)
     |     --|
     |       |
     |       
     |
    _|___

 ''','''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |       
     |
    _|___

 ''','''
      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___
    
''','''
      _______
     |/      |
     |      (_)
     |     
     |      
     |      
     |
    _|___

'''] # 0 -> 6 index


word_list = ['lion', 'tiger', 'leopard', 'panther', 'monkey', 'gorilla', 'elephant']
lives = 6

print("Welcome to Hangman! (Animal Edition)")
random_animal = random.choice(word_list)

placeholder = ""
word_length = len(random_animal)
for blank in range(word_length):
    placeholder += '_'
print(placeholder)

game_over = False
ct_letters = []

while not game_over:
    guess = input("Guess a character").lower()

    display = ""

    for letter in random_animal:
        if letter == guess:
            display += letter
            ct_letters.append(guess)
        elif letter in ct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in random_animal:
        lives -= 1
        print(f"You guessed {guess}, You have {lives} remaining")
        if lives == 0:
            game_over = True
            print("********You lost! You have 0 remaining lives!*********")



    if "_" not in display:
        game_over =  True
        print("********You have guessed all the letters! You WIN !!!*********")

    print(stages[lives])