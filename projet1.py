#projet python
'''operator = input("Enter an operator (+ - / *): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print("result: ", round(result,2))
elif operator =="-":
    result = num1 - num2
    print("result: ", round(result,2))
elif operator == "*":
    result = num1 * num2
    print("result: ", round(result,2))
elif operator == "/":
    result = num1 / num2
    print("result: ", round(result,2))
else:
    print(f"{operator} is not valid operator")

#convertir en C ou F
unit = input("is this temperature in celsius or Fahrenhneit (C/F): ").upper()
temps = float(input("Enter the temperature: "))

if unit == "F":
    temps = round((9 * temps) / 5 + 32,1)
    print(f"The temperature en Celsius est: {temps}Celsius")
elif unit == "C":
    temps = round((temps * 32) * 5 / 9,1)
    print(f"The temperature in Farahneit is: {temps}Fahrenheit")
else:
    print(f"{unit} was not valid")

import time

my_time = int(input("Enter the time in secons: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(f"00:00:{seconds}")
    time.sleep(1)

print("HBD CHOUBABY.!!")

prenom = input("Enter your name: ").upper()
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input("Entrer le prix: "))
        foods.append(food)
        prices.append(price)

print("--------- YOUR CART ------------")
print('prenom: ',prenom)
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
    
print()
print(f"Your total price is: ${total}")


#python quiz guame
print("****jeux de supposition*****")
name = input("Enter your name:")
print("BIENVENUE DANS NOTRE JEUX, TOP C'EST PARTI", name)
questions = ("Il y'a combien de continents au monde?: ",
             "L'afrique compte combien de pays?: ",
             "Qui est l'actuel president des senegalais?: ",
             "Quel years le senegal a pris son independance?: ",
             "Qui est l'homme le plus riche du monde?: ")
options = (("A. 2", "B. 4", "C. 8", "D. 5"),
           ("A. 45", "B. 54", "C. 34", "D.60"), 
           ("A. Bassirou", "B. Ablaye", "C. Ousmane", "D.Macky"),
           ("A. 1900", "B. 1920", "C. 1960", "D.1980"),
           ("A.Macky", "B. Billgates", "C. ElonMusk", "D.Markzucker"))

answers = ("D","B", "A", "C", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A< B< C or D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!!!!")
    else:
         print("Incorrext")
         print(f"{answers[question_num]} is the correct answer.")  
    question_num += 1

print("------------------------------------")   
print('               RESULT !              ')
print("------------------------------------")   

print("answers: ",end=' ') 
for answer in answers:
    print(answer, end=' ')
print()   
print('guesses: ', end=' ')
for guess in guesses:
    print(guess, end=' ')

print()
smcore = int(score / len(questions) * 100)
print(f"Your score is:  {score}%")

#concession stand programme
menu = {
    "pizza": 3.60,
    "nachos": 4.5,
    "pink": 3.2,
    "soda": 3.4,
    "boisson": 7.8,
    "chips": 2.5,
}
cart = []
total = 0
print("----------- MENU -----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item or q to quit: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)  

for food in cart:
    total += menu.get(food)
    print(food, end=' ')

print()
print(f"Total is: ${total:.2f}")

#Python number guessing game
import random
min_num = 1
max_num = 10
answer = random.randint(min_num, max_num)
guesses = 0
is_running = True

print("Bienvenue Python Nnumber Guessing Guame")
print(f"Select a number between {min_num} et {max_num}: ")
while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += guess
        
        if guess < min_num or guess > max_num:
            print("That number is out of range")
            print(f"Please select a number between {min_num} and {max_num}")
        elif guess < answer:
            print("Too low! try again")
        elif guess > answer:
            print("Too higth! try again!")
        else:
            print(f"CORRECT!!")
            print("Congratulation!!!!")
            is_running = False    
    else:
        print("Invalid input")        
        print(f"Please select a number between {min_num} and {max_num}")
    
import random
options = ("rock", "paper", "scissors")
running = True
score = 0 
choix = []
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("enter a choice (rock, paper, scissors): ").lower()
    
    print(f"player: {player}")
    print(f"computer: {computer}")
    choix.append(player)
    if player == computer:
            print("It's a tie!")
    elif player == "rock" and computer == "scissors":
            print("You won CONGRATULATION!!!!!!*******")
            score += 1
    elif player == "scissors"  and computer == "paper":
            print("You won CONGRATULATION!!!!!!*******")
            score += 1
    elif player == "paper" and computer == "rock":
            print("You won CONGRATULATION!!!!!!*******")
            score += 1
    else:
             print("You lost!!!")
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        break
print("Thank you!! for gaming")
score = int(score/ len(choix ) * 100)
print(f"Votre score final est: {score}%")

#jeux de carte
import random
#●      ┌ ┐ 
#print("\u25CF \u250C \u2510 \u2502 \u2514 \u2518")
#┌ ┐ │ └ ┘
"┌————————————————┐"
"│                │" 
"│                │"
"│                │"
"│                │"
"│                │"
"│                │"
"└————————————————┘"                         

                       
dice_cart = {
    1: ( "┌————————————————┐",
         "│                │" ,
         "│                │",
         "│       ●        │",
         "│                │",
         "│                │",
         "└————————————————┘" ),
    2: (
         "┌————————————————┐",
         "│                │" ,
         "│   ●            │",
         "│                │",
         "│         ●      │",
         "│                │",
         "└————————————————┘" ),
    3: (  "┌————————————————┐",
          "│  ●             │", 
          "│                │",
          "│        ●       │",
          "│                │",
          "│            ●   │",
          "└————————————————┘" ),
    4: (  "┌————————————————┐",
          "│    ●      ●    │" ,
          "│                │",
          "│                │",
          "│    ●      ●    │",
          "│                │",
          "└————————————————┘" ),
    5: ("  ┌————————————————┐",
          "│    ●       ●   │", 
          "│                │",
          "│        ●       │",
          "│                │",
          "│    ●       ●   │",
          "└————————————————┘" ),
    6: (  "┌————————————————┐",
          "│    ●       ●   │" ,
          "│                │",
          "│    ●       ●   │",
          "│                │",
          "│    ●       ●   │",
          "└————————————————┘" ),
                              
}
dice = {}
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
        dice.append(random.randint(1, 6))
        
for die in dice:
    total += die
print()
'''





























