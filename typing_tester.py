import curses
from curses import wrapper
import time

def cal_accuracy_score(given_word, user_text, no_of_backspaces):
    """Calculates the accuracy score for typing tester"""

    wrong_letter = 0
    try:
        wrong_letter = sum([1 for i in range(len(given_word)) if user_text[i] != given_word[i]])
    except:
        wrong_letter += 1

    total_mistakes = wrong_letter + no_of_backspaces
    accuracy = len(given_word) - total_mistakes
    accuracy =  accuracy/len(given_word)*100

    return float(f"{accuracy:.2f}")


def cal_time_score(elapsed_time, given_word):
    """Calculates the time score for typing tester"""

    # Avg. time for one keystroke
    keystroke_time = 0.28 
    # Avg. time to hover hands from mouse to keyboard
    mouse_to_keyboard_time = 0.4 
    # formula to calculate raw score
    raw_score = elapsed_time / (mouse_to_keyboard_time + (keystroke_time * (len(given_word) + 1)))

    if raw_score < 1:
         return float(100)
    else:
         return float(f"{(100/raw_score):.2f}")

def display_result(stdscr, elapsed_time, given_word, user_text, backspaces):
      """Displays result of typing tester"""

      # Coverts user_text list to string
      user_text = "".join(user_text)
      # Calculates accuracy score
      accuracy_score = cal_accuracy_score(given_word, user_text, backspaces)
      # Calculates time score
      time_score = cal_time_score(elapsed_time, given_word)
      # Calculates total score
      total_score = f"{(accuracy_score + time_score)/2:.2f}"

      stdscr.clear()

      # Overall Result/Output
      stdscr.addstr(f"Word: {given_word}\n")
      stdscr.addstr(f"No. of letters: {len(given_word)}\n")

      stdscr.addstr(f"\nUser typed: {user_text}\n")
      stdscr.addstr(f"Time taken by the user: {int(elapsed_time)}s\n")

      stdscr.addstr(f"\nAccuracy score: {accuracy_score}\n")
      stdscr.addstr(f"Time score: {time_score}\n")

      stdscr.addstr(f"\nTotal score: {total_score}\n")

      stdscr.addstr(f"\nDefinition: {given_word}\n")
      stdscr.addstr(f"Pronunciation: {given_word}\n")

      stdscr.addstr(f"\nPress any key to exit...")

      stdscr.refresh()
      stdscr.getch()
      

def start_screen(stdscr):
    """Displays initial screen of typing tester"""

    stdscr.addstr(2,0,"Typing Tester", curses.color_pair(1))
    stdscr.addstr(3,0,"Press any key to start.....")
    stdscr.refresh()
    stdscr.getkey()
    typing_tester_screen(stdscr) # Test Screen where user input is evalauted

def display_text(stdscr, word, user_text):
    """Displays the user input dynamically on each keystroke"""

    stdscr.addstr(2, 0, "||*** Typing Tester ***||", curses.color_pair(1))
    stdscr.addstr(4, 0, "Press Enter when done...")
    stdscr.addstr(6, 0, f"Word : {word}")
    stdscr.addstr(7, 0, "Enter the above word: ")

    # for loop is used for every key user input
    for char in user_text:
        stdscr.addstr(char, curses.color_pair(1))

def typing_tester_screen(stdscr):
    """Displays typing tester screen"""

    DELETE_KEY_ASCII = 127
    ENTER_KEY_ASCII = 10
    given_word = "Intellectualism"
    user_text = []
    start_time = time.time()
    backspaces = 0
    while True:

        # clear the initial screen
        stdscr.clear()

        # display user text everytime user enters key
        display_text(stdscr, given_word, user_text) 
        stdscr.refresh()
        key = stdscr.getkey()

        if ord(key) == DELETE_KEY_ASCII:
            if len(user_text) > 0:
                    user_text.pop()
                    backspaces = backspaces + 1

        elif len(user_text) < len(given_word):
              user_text.append(key)

        if ord(key) == ENTER_KEY_ASCII:
              elapsed_time = time.time() - start_time
              display_result(stdscr, elapsed_time, 
                             given_word, user_text, backspaces)
              break


# stdscr = standard console screen, curses overrides the console temporarily
def main(stdscr):
    """Main function to start the program"""

    # color pair for terminal(red, black)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    start_screen(stdscr) # Initial Screen before test
    stdscr.refresh()

if __name__ == '__main__':
    wrapper(main)
