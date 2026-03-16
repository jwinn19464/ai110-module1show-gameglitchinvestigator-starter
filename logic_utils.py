import random


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def reset_game_state(session_state: dict, difficulty: str, forced_secret: int = None):
    """Reset game state for a new game round."""
    low, high = get_range_for_difficulty(difficulty)
    session_state["status"] = "playing"
    session_state["attempts"] = 1
    session_state["history"] = []
    session_state["score"] = 0
    session_state["secret"] = forced_secret if forced_secret is not None else random.randint(low, high)
    return session_state


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return an outcome string.

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        if guess == secret:
            return "Win"
        if guess < secret:
            return "Too Low"
        return "Too High"
    except TypeError:
        # Fallback to string comparisons if type mismatch occurs.
        g = str(guess)
        s = str(secret)
        if g == s:
            return "Win"
        if g < s:
            return "Too Low"
        return "Too High"


def get_feedback_message(outcome: str):
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too Low":
        return "📈 Go HIGHER!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    return ""


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
