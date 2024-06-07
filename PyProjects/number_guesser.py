import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  if top_of_range <= 0:
    print('Please type a number larger than 0 next time.')
    quit()
else:
  print('Please type a number next time.')
  quit()
random_number = random.randint(0,top_of_range)
guess_count = 0
while True:
  user_guess = input("Make a guess: ")
  guess_count+=1
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('Please type a number next time.')
    continue
  if user_guess > random_number:
    print("Number is greater.")
  elif user_guess < random_number:
    print("Number is smaller.")
  else:
    print("You got it.")
    print("You guessed at "+str(guess_count)+" times")
    break
