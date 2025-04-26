import random

def generate_story():
    genres = ["Fantasy", "Science Fiction", "Mystery", "Horror", "Romance", "Thriller"]
    characters = ["a rebellious scientist", "a lonely detective", "a young orphan with magical powers", 
                  "an alien stranded on Earth", "a warrior with a forgotten past", "a time traveler stuck in the future"]
    themes = ["overcoming fear", "betrayal and revenge", "self-discovery", "friendship and loyalty", "a race against time"]
    settings = ["a futuristic city", "a haunted mansion", "an underground bunker", "a lost kingdom", "a spaceship drifting in space"]
    
    genre = random.choice(genres)
    character = random.choice(characters)
    theme = random.choice(themes)
    setting = random.choice(settings)
    
    story = (f"In a {setting}, {character} must navigate a journey of {theme}. "
             f"As they uncover secrets, they realize the world they know is not what it seems. "
             f"A thrilling {genre} adventure unfolds!\n\n")
    
    # Expanding into a full story
    full_story = (f"Once upon a time in {setting}, {character} found themselves facing an unexpected challenge. "
                  f"One day, a mysterious event forced them to confront their deepest fears. "
                  f"Determined to overcome the obstacles, they embarked on a journey that would change their life forever.\n\n"
                  f"As they ventured further, they encountered allies and enemies alike, each playing a role in their quest. "
                  f"With each revelation, the truth about their past and future began to unfold. "
                  f"Would they succeed in their mission, or would the forces against them prove too strong?\n\n"
                  f"The fate of everything rested on their decisions, and with time running out, "
                  f"they had to make the ultimate choice that would shape the destiny of their world. "
                  f"This was not just any adventure; this was a legendary tale of {theme} in the world of {genre}.")
    
    return full_story

# Main Program Loop
def main():
    print("\n📝 Welcome to the AI Story Generator! 📝\n")
    while True:
        user_input = input("Press Enter to generate a new full story or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Happy writing!")
            break
        print("\n🔹 Your Generated Story: \n")
        print(generate_story())
        print("\n------------------------------------------\n")

if __name__ == "__main__":
    main()