# Project 1: Mini-Project Quiz Game

print("Mini-Project Quiz Game")

# Ask if the user wants to play
play = input("Do you want to play the quiz? (yes/no): ").lower()

if play == "yes" or play == "y":
    # Get player's name
    name = input("Enter your name: ")
    f_name = name.capitalize()
    print(f"\nHello {f_name}, welcome to the quiz!\n")

    # question
    print("Question 1: What is the capital of India?")
    print("a) Mumbai")
    print("b) New Delhi")
    print("c) Kolkata")
    print("d) Chennai")

    # Get user's answer
    opt = input("Enter your option (a/b/c/d): ").lower()  # convert to lowercase for easy comparison

    # Check answer
    if opt == 'b':
        print("Correct!")
    else:
        print("Wrong answer. The correct answer is b) New Delhi.")

else:
    print("Okay! Maybe next time. Goodbye!")
