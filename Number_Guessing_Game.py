import os
from random import randint
import sys
import time
import platform
import time
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
game_file = os.path.join(script_dir, "score_board.json")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data():
    if not os.path.exists(game_file):
        with open(game_file, 'w') as f:
            json.dump({"scores": []}, f, indent=4)
    with open(game_file, 'r') as f:
        return json.load(f)
        
def save_data(data):
    with open(game_file,'w') as f:
        json.dump(data, f, indent=4)

def start_timer():
    return time.time()

def stop_timer(start_time):
    return time.time() - start_time

def format_time(seconds):
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes:02d}:{secs:02d}"

def display_scores(data):
    scores_sorted = sorted(data["scores"], key=lambda x: time_to_seconds(x["time"]))
    print("          *LEADERBOARD*           ")
    print("|--------------------------------|")
    print("|    PLAYER     |     TIME       |")
    print("|--------------------------------|")
    for i, score in enumerate(scores_sorted, 1):
        print(f"| {i}. {score['player']:<10} |     {score['time']:<10} |")
        print("|--------------------------------|")

def reset_scores():
    save_data({"scores":[]})
    print("Scoreboard has been reset!")

def add_score(player, time_taken):
    data = load_data()
    data["scores"].append({"player": player, "time": time_taken})
    save_data(data)

def time_to_seconds(time_str):
    minutes, secs = map(int, time_str.split(":"))
    return minutes * 60 + secs

def has_scores(data):
    return len(data["scores"]) > 0

def start_menu():
    clear_screen()
    data = load_data()
    print("*WELCOME TO THE PYTHON NUMBER GUESSING GAME*\n")
    print("1. Start Game")
    print("2. View Scoreboard")
    print("3. Reset Scores")
    print("4. Exit Game\n")
    start_input = input("What would you like to do?\n").upper()
    while True:
        if start_input == "1":
            clear_screen()
            print("Taking you to the game now...")
            time.sleep(3)
            start_game()
        elif start_input == "2":
            if has_scores(data):
                clear_screen()
                display_scores(data)
                print("   ")
                user_input = input("Press enter to go back\n")
                if user_input == "":
                    start_menu()
                    clear_screen()
            else:
                clear_screen()
                print("You don't have a scoreboard yet, try playing the game first!")
                print("Taking you back to the start screen, please wait...")
                time.sleep(5)
                start_menu()
        elif start_input == "3":
            clear_screen()
            print("Hold on a second while we reset the scoreboard!...")
            time.sleep(3)
            reset_scores()
            clear_screen()
            print("SCOREBOARD RESET!")
            time.sleep(3)
            start_menu()
        elif start_input == "4":
            clear_screen()
            print("Exiting application now, please wait")
            time.sleep(4)
            exit()

def start_game():
    data = load_data()
    clear_screen()
    print("We need to be able put your results on the scoreboard")
    while True:
        player = input("What is your name?\n").upper()
        if player != "":
            clear_screen()
            print(f"Great '{player}'! Let's get you started...")
            time.sleep(4)
            clear_screen()
            break
        else:
            print(f"Please enter your name to begin")
    
    select_num = randint(0,1001)

    if not has_scores(data):
        clear_screen()
        print(f"The script now has thought of a number between 0 and 1000, {player}, your job is to find that number.")
        time.sleep(5)
        clear_screen()
        print(f"Each time you take a guess, the script will tell you how close you are to the number using signals like: 'Go Higher!' or 'Go Lower!'")
        time.sleep(7)
        clear_screen()
        print(f"{player}, you'll also be timed on how quickly you find the number and this timer starts the moment the game begins.")
        time.sleep(7)
        clear_screen()
        print("You'll be able to view your scores in the scoreboard at the start menu, with all that said, let's begin!")
        time.sleep(7)
        clear_screen()
        print("3...")
        time.sleep(2)
        clear_screen()
        print("2...")
        time.sleep(2)
        clear_screen()
        print("1...")
        time.sleep(2)
        clear_screen()

        start_time = start_timer()

        while True:
            user_input = input("Enter your guess: \n")
            
            if not user_input.isdigit():
                print(f"please enter digits only... {player}, Try again!")
                continue

            user_input = int(user_input)

            if user_input < select_num:
                print("Go higher!")
            elif user_input > select_num:
                print("Go lower!")
            elif user_input == select_num:
                print("You found the number!")
                elapsed_seconds = stop_timer(start_time)
                elapsed_formatted = format_time(elapsed_seconds)
                print(f"{player}! You finished in {elapsed_formatted}")
                add_score(player, elapsed_formatted)
                time.sleep(5)
                start_menu()
                break

    else:
        print("Starting game now...")
        clear_screen()
        print("3...")
        time.sleep(2)
        clear_screen()
        print("2...")
        time.sleep(2)
        clear_screen()
        print("1...")
        time.sleep(2)
        clear_screen()

        start_time = start_timer()

        while True:
            user_input = input("Enter your guess: \n")
            
            if not user_input.isdigit():
                print(f"please enter digits only... {player}, Try again!")
                continue

            user_input = int(user_input)

            if user_input < select_num:
                clear_screen()
                print("Go higher!")
            elif user_input > select_num:
                print("Go lower!")
            elif user_input == select_num:
                clear_screen()
                print("You found the number!")
                time.sleep(5)
                elapsed_seconds = stop_timer(start_time)
                elapsed_formatted = format_time(elapsed_seconds)
                print(f"{player}! You finished in {elapsed_formatted}")
                add_score(player, elapsed_formatted)
                time.sleep(5)
                start_menu()
                break

start_menu()


