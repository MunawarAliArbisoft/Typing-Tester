import curses
from curses import wrapper
from screens import start_screen
         
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
