animal_list = ['zebra', 'hippo', 'gazelle' , 'deer', 'antelope', 'sheep']

while len(animal_list) > 0:
  print("You have to guess " + str(len(animal_list)) + " more animals.")
  guess = input("What's your guess?\n:")
  if guess in animal_list:
      animal_list.remove(guess)
      print("Correct!")
  else:
      print("Wrong, guess again!")
