import random
magic_answers = ["Of course!", "Sorry... I really am.","Try again. Bad question. You don't want to know.", "Yes, if you stand up right now.", "You should probably ask something else.","It's totally possible.","Maybe, the future is foggy.","Yes."]

running = True

while running == True:
    tell_me = input('Think of a question and type "ask" :-)\n:')
    if tell_me == "ask":
        running = False
        print(random.choice(magic_answers))
    else:
        print('Try again!')
