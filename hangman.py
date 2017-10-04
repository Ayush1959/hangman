import random

def choose_word(fname):
    good_words = []

    f = open(fname)
    for i in f:
        i = i.strip()
        if i.islower() and i.isalpha() and len(i) >= 6:
            good_words.append(i)
    f.close()
    
    return random.sample(good_words, 1)[0]

def masking_words(fname):
    selected_word =  choose_word(fname)
    print(selected_word)
    s= len(selected_word)
    masked_word = '-' * s
    return masked_word

def no_of_remaining_turns(fname):
    no_of_turn = 8
    selected_word = choose_word(fname)
    print(selected_word)
    letters=[]
    guesses=[]
    correct_guesses=[]
    for i in selected_word:
        letters.append(i)
    print(letters)
   # print(sorted(letters))
    while no_of_turn > 0:
        x = input("Guess a Letter > ")
       # print(x)
        if x not in guesses:
            guesses.append(x)
            print("You have guessed the following {}".format(guesses))
            if x not in letters:
                no_of_turn -= 1
                print("{} is not in this word".format(x))
                print("The remaining no of turns left  = {}".format(no_of_turn))
            else:
                print("Yeah! {} is in the Word".format(x) )
                correct_guesses.append(x)
            if no_of_turn == 0:
                    print("You have no remaining turns left")
        else:
             print("{} is already guessed".format(x))
        #print(sorted(guesses))
        if sorted(correct_guesses) == sorted(list(set(letters))):
            print("Wow you have guessed all the letters of the  word *{}* correctly".format(selected_word))
            quit()
            exit()
        
