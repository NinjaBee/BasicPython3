#This is a list of my shirt colors
shirt_colors = ['red','purple','yellow','black']

#This section will ask questions and reduce list size
while len(shirt_colors) > 0:
    print("Can you guess all the colors of my shirt? You have " + str(len(shirt_colors)) + " more colors to guess!")
    color = input("Tell me a color from my shirt.\n:")
    if color in shirt_colors:
        print("Right on! You got it.")
        shirt_colors.remove(color)
    else:
        print("Oh, so close! Try again.")
