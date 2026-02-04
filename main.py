


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
jokes = [
    {"type": "robbers", "setup": "Calder", "punchline": "Calder police — I've been robbed!"},
    {"type": "tanks", "setup": "Tank", "punchline": "You're welcome!"},
    {"type": "pencils", "setup": "Broken pencil", "punchline": "Nevermind, it's pointless!"}
]


def get_joke(type):
    for joke in jokes:
        if joke["type"] == type:
            return joke
    return None

def tell_joke(joke):
    input("Knock knock... ")
    input(joke["setup"])
    print(joke["punchline"])

def program():
    answer = input("Do you want to hear a joke? (yes or no) ").lower()

    while answer == "yes":
        type = input("Choose a category: robbers, tanks, or pencils: ").lower()
        selected_joke = get_joke(type)

        if selected_joke:
            tell_joke(selected_joke)
        else:
            print("Sorry, that joke doesn't exist.")

        answer = input("Do you want to hear another joke or are you finished? ").lower()

    if answer == "finished":
        rating = int(input("Rate our game from 1–10: "))
        print(str(rating * 10) + "% satisfaction rate")

        recommend = input("Would you recommend this game to a friend? ").lower()
        if recommend == ["yes", "maybe"]:
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you did not enjoy it.")

program()
