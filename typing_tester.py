import curses
from curses import wrapper
import time

# To calcukate accuracy
def cal_accuracy(given_word, user_text, backspaces):
    wrong_letter = 0
    try:
        for i in range(len(given_word)):
            if user_text[i] != given_word[i]:
                wrong_letter = wrong_letter + 1
    except:
        wrong_letter = wrong_letter+1

    total_mistakes = wrong_letter + backspaces
    accuracy = len(given_word) - total_mistakes
    accuracy =  accuracy/len(given_word)*100
    return float("{:.2f}".format(accuracy))

# To calculate Time Score
def cal_time(elapsed_time, given_word):
    raw_score = elapsed_time / (0.4 + (0.28 * (len(given_word) + 1)))
    if raw_score < 1:
         return float(100)
    else:
         return float("{:.2f}".format(100/raw_score))

def display_result(stdscr, elapsed_time, given_word, user_text, backspaces):
      user_text = "".join(user_text)

      # To calculate Accuracy
      accuracy_score = cal_accuracy(given_word, user_text, backspaces)
      # To calculate Time
      time_score = cal_time(elapsed_time, given_word)
      # Calculate total score
      total_score = "{:.2f}".format((accuracy_score + time_score)/2)

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
    stdscr.addstr(2,0,"Typing Tester", curses.color_pair(1))
    stdscr.addstr(3,0,"Press any key to start.....")
    stdscr.refresh()
    stdscr.getkey()
    typing_tester_screen(stdscr) # Test Screen where user input is evalauted

def display_text(stdscr, word, user_text):
    stdscr.addstr(2, 0, "||*** Typing Tester ***||", curses.color_pair(1))
    stdscr.addstr(4, 0, "Press Enter when done...")
    stdscr.addstr(6, 0, f"Word : {word}")
    stdscr.addstr(7, 0, "Enter the above word: ")

    # for loop is used for every key user input
    for char in user_text:
        stdscr.addstr(char, curses.color_pair(1))

def typing_tester_screen(stdscr):
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

        if ord(key) == 127:
            if len(user_text) > 0:
                    user_text.pop()
                    backspaces = backspaces + 1

        elif len(user_text) < len(given_word):
              user_text.append(key)

        if ord(key) == 10:
              elapsed_time = time.time() - start_time
              display_result(stdscr, elapsed_time, given_word, user_text, backspaces)
              break


# stdscr = standard console screen, curses overrides the console temporarily
def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    stdscr.clear()
    start_screen(stdscr) # Initial Screen before test
    stdscr.refresh()

wrapper(main)