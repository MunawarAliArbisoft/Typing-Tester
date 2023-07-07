import curses
import time
from get_words import get_random_word
from calculate_score import cal_accuracy_score, cal_time_score

def start_screen(stdscr):
    """Displays initial screen of typing tester"""

    stdscr.clear()
    stdscr.addstr(2,0,"Typing Tester", curses.color_pair(1))
    stdscr.addstr(3,0,"Press any key to start.....")
    stdscr.refresh()
    stdscr.getkey()
    typing_tester_screen(stdscr) # Test Screen where user input is evalauted

def typing_tester_screen(stdscr):
    """Displays typing tester screen"""

    DELETE_KEY_ASCII = 127
    ENTER_KEY_ASCII = 10
    word_obj = get_random_word()
    user_text_list = []
    start_time = time.time()
    no_of_backspaces = 0

    while True:

        # clear the initial screen
        stdscr.clear()

        # display user text everytime user enters key
        display_text(stdscr, word_obj, user_text_list) 
        stdscr.refresh()
        key = stdscr.getkey()

        try:
            if ord(key) == DELETE_KEY_ASCII:
                if len(user_text_list) > 0:
                        user_text_list.pop()
                        no_of_backspaces = no_of_backspaces + 1

            elif len(user_text_list) < len(word_obj.get('word')):
                user_text_list.append(str(key))
        except:
            continue

        if ord(key) == ENTER_KEY_ASCII:
            elapsed_time = float(time.time() - start_time)
            # Coverts user_text list to string
            user_text = "".join(user_text_list)
            display_result(stdscr, elapsed_time, 
                            word_obj, user_text, no_of_backspaces)
            break
        
def display_result(stdscr, elapsed_time: float, 
                   word_obj: str, user_text: str, backspaces: int):
      """Displays result of typing tester"""
    
      # Gets word, definition and pronunciation from word object
      word = word_obj.get('word')
      definition = word_obj.get('definition')
      pronunciation = word_obj.get('pronunciation')

      # Calculates accuracy score
      accuracy_score, misspelling = cal_accuracy_score(word, user_text, backspaces)
      # Calculates time score
      time_score = cal_time_score(elapsed_time, word)
      # Calculates total score
      total_score = f"{(accuracy_score + time_score)/2:.2f}"

      stdscr.clear()

      # Overall Result/Output
      stdscr.addstr(f"Word: {word}\n")
      stdscr.addstr(f"No. of letters: {len(word)}\n")

      stdscr.addstr(f"\nUser typed: {user_text}\n")
      stdscr.addstr(f"Time taken by the user: {int(elapsed_time)}s\n")

      stdscr.addstr(f"\nAccuracy score: {accuracy_score}\n")
      stdscr.addstr(f"Time score: {time_score}\n")

      stdscr.addstr(f"\nNo. of backspaces: {backspaces}\n")
      stdscr.addstr(f"Misspelling: {misspelling}\n")

      stdscr.addstr(f"\nTotal score: {total_score}\n")

      stdscr.addstr(f"\nDefinition: {definition}\n")
      stdscr.addstr(f"Pronunciation: {pronunciation}\n")

      stdscr.addstr(f"\nPress q key to exit...")
      stdscr.addstr(f"\nPress anykey to play again...")

      stdscr.refresh()
      key = stdscr.getch()

      if key != ord('q'):
        typing_tester_screen(stdscr)
      

def display_text(stdscr, word_obj: str, user_text_list: list):
    """Displays the user input dynamically on each keystroke"""

    stdscr.addstr(2, 20, "||*** Typing Tester ***||", curses.color_pair(1))
    stdscr.addstr(4, 20, "Press Enter when done...")
    stdscr.addstr(6, 20, f"Word : {word_obj.get('word')}")
    stdscr.addstr(7, 20, "Enter the above word: ")

    # for loop is used for every key user input
    [stdscr.addstr(char, curses.color_pair(1)) for char in user_text_list]
    
        