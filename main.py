                                                                                                       #edited program pt.2
jokes = [
    {"type": "robbers", "setup": "Calder", "punchline": "Calder police — I've been robbed!"},
    {"type": "tanks", "setup": "Tank", "punchline": "You're welcome!"},
    {"type": "pencils", "setup": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
]

def get_joke(joke_type):
    for joke in jokes:
        if joke["type"] == joke_type:
            return joke
    return None 

def tell_joke(joke):
    input("Knock knock...")
    input(joke["setup"])
    print(joke["punchline"])

def add_new_joke(new_type=None, new_setup=None, new_punchline=None): 
    print("--- Add a New Joke ---") 
    if new_type is None: 
        new_type = input("Enter a new joke category name: ").lower() 
    if new_setup is None: 
        new_setup = input("Enter the setup line: ") 
    if new_punchline is None: 
        new_punchline = input("Enter the punchline: ") 
    new_joke = { "type": new_type, "setup": new_setup, "punchline": new_punchline } 
    jokes.append(new_joke) 
    print(f"Joke added under category '{new_type}'!")

def program():
    answer = input("Do you want to hear a joke? (yes or no): ").lower()

    if answer == "no":
        answer == input("are you finished?:").lower


    while answer == "yes":
        category_list = [joke["type"] for joke in jokes]
        print(f"Available categories: {', '.join(category_list)}")
        
        choice = input("Choose a category or type 'add' to add a new joke: ").lower()
        
        if choice == "add":
            add_new_joke()
        else:
            selected_joke = get_joke(choice)
            if selected_joke:
                tell_joke(selected_joke)
            else:
                print("Sorry, that joke doesn't exist.")
        
        answer = input("Do you want to hear another joke or are you finished? (yes/finished): ").lower()
        
    if answer == "finished":
        rating = int(input("Rate our game from 1–10: "))
        print(str(rating * 10) + "% satisfaction rate")

        recommend = input("Would you recommend this game to a friend? (yes/no): ").lower()
        if recommend in ["yes", "maybe"]:
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you did not enjoy it.")

program()



# make this performance task ready for submission
# To give the user a fun experience hearing knock knock jokes

# joke = input("Do you want to hear a joke? ")                                             #---------------------Original Program-------------#
# if joke == "no":
#     print("Okay suit yourself!")
# while joke == "yes":
#     print("Great, Let's Play")
#     question = input("Do you want to hear a joke about robbers, tanks, or pencils? ")
#     if question == "robbers":
#         input("Knock Knock ")
#         input("Calder")
#         print("Calder police - I've been robbed!")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "tanks":
#         input("Knock Knock ")
#         input("Tank ")
#         input("You are welcome! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
#     elif question == "pencils":
#         input("Knock Knock ")
#         input("Broken pencil ")
#         input("Nevermind, it's pointless! ")
#         joke = input("Do you want to hear another joke or are you finished? ")
# if joke == "finished":
#     rate = int(input("Please rate our game 1-10! "))
#     final_score = int(rate * 10)
#     print(str(final_score) + " percent satisfaction rate")
#     friend = input("Would you recommend this game to a friend? ")

#     if friend == "yes" or friend == "maybe":
#         print("Thanks, we appreciate it. ")
#     else:
#         print("Sorry you did not enjoy it. ")

#-------------------------------------------------------------------------------

                                                                                            #-----------------------------edited program--------------#
# jokes = [
#     {"type": "robbers", "setup": "Calder", "punchline": "Calder police — I've been robbed!"},
#     {"type": "tanks", "setup": "Tank", "punchline": "You're welcome!"},
#     {"type": "pencils", "setup": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
# ]


# def get_joke(type):
#     for joke in jokes:
#         if joke["type"] == type:
#             return joke
#     return None

# def tell_joke(joke):
#     input("Knock knock... ")
#     input(joke["setup"])
#     print(joke["punchline"])


# def program():
#     answer = input("Do you want to hear a joke? (yes or no) ").lower()

#     while answer == "yes":
#         type = input("Choose a category: robbers, tanks, or pencils: ").lower()
#         selected_joke = get_joke(type)

#         if selected_joke:
#             tell_joke(selected_joke)
#         else:
#             print("Sorry, that joke doesn't exist.")

#         answer = input("Do you want to hear another joke or are you finished? ").lower()

#     if answer == "finished":
#         rating = int(input("Rate our game from 1–10: "))
#         print(str(rating * 10) + "% satisfaction rate")

#         recommend = input("Would you recommend this game to a friend? ").lower()
#         if recommend in ["yes", "maybe"]:
#             print("Thanks, we appreciate it!")
#         else:
#             print("Sorry you did not enjoy it.")

# program()
                                                                                                       #edited program pt.2
jokes = [
    {"type": "robbers", "setup": "Calder", "punchline": "Calder police — I've been robbed!"},
    {"type": "tanks", "setup": "Tank", "punchline": "You're welcome!"},
    {"type": "pencils", "setup": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
]

def get_joke(joke_type):
    for joke in jokes:
        if joke["type"] == joke_type:
            return joke
    return None 

def tell_joke(joke):
    input("Knock knock...")
    input(joke["setup"])
    print(joke["punchline"])

def add_new_joke(new_type=None, new_setup=None, new_punchline=None): 
    print("--- Add a New Joke ---") 
    if new_type is None: 
        new_type = input("Enter a new joke category name: ").lower() 
    if new_setup is None: 
        new_setup = input("Enter the setup line: ") 
    if new_punchline is None: 
        new_punchline = input("Enter the punchline: ") 
    new_joke = { "type": new_type, "setup": new_setup, "punchline": new_punchline } 
    jokes.append(new_joke) 
    print(f"Joke added under category '{new_type}'!")

def program():
    answer = input("Do you want to hear a joke? (yes or no): ").lower()
    while answer == "yes":
        category_list = [joke["type"] for joke in jokes]
        print(f"Available categories: {', '.join(category_list)}")
        
        choice = input("Choose a category or type 'add' to add a new joke: ").lower()
        
        if choice == "add":
            add_new_joke()
        else:
            selected_joke = get_joke(choice)
            if selected_joke:
                tell_joke(selected_joke)
            else:
                print("Sorry, that joke doesn't exist.")
        
        answer = input("Do you want to hear another joke or are you finished? (yes/finished): ").lower()
        
    if answer == "finished":
            rating = int(input("Rate our game from 1–10: "))
            print(str(rating * 10) + "% satisfaction rate")

    recommend = input("Would you recommend this game to a friend? (yes/no): ").lower()
    if recommend in ["yes", "maybe"]:
        print("Thanks, we appreciate it!")
    else:
        print("Sorry you did not enjoy it.")

program()
