def cal_accuracy_score(given_word: str, user_text: str, no_of_backspaces: int) -> tuple:
    """Calculates the accuracy score for typing tester"""

    wrong_letter = 0
    try:
        wrong_letter = sum(
            [1 for i in range(len(given_word)) if given_word[i] != user_text[i]]
        )
    except IndexError:
        wrong_letter += 1

    total_mistakes = wrong_letter + no_of_backspaces
    accuracy = (len(given_word) - total_mistakes) / len(given_word) * 100
    # assign 0 if accuracy is negative
    accuracy = 0 if accuracy < 0 else accuracy

    return float(f"{accuracy:.2f}"), wrong_letter


def cal_time_score(elapsed_time: float, given_word: str) -> float:
    """Calculates the time score for typing tester"""

    # Avg. time for one keystroke
    KEYSTROKE_TIME = 0.28
    # Avg. time to hover hands from mouse to keyboard
    MOUSE_TO_KEYBOARD_TIME = 0.4
    # formula to calculate raw score
    raw_score = elapsed_time / (
        MOUSE_TO_KEYBOARD_TIME + (KEYSTROKE_TIME * (len(given_word) + 1))
    )

    return float(100) if raw_score < 1 else float(f"{(100/raw_score):.2f}")
