from logic_utils import (
    check_guess,
    get_feedback_message,
    get_range_for_difficulty,
    reset_game_state,
)

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_feedback_message_too_low_maps_to_go_higher():
    # This is the fix for reversed hints: Too Low means guess is below secret, so we must go higher.
    assert get_feedback_message("Too Low") == "📈 Go HIGHER!"

def test_feedback_message_too_high_maps_to_go_lower():
    # This is the fix for reversed hints: Too High means guess is above secret, so we must go lower.
    assert get_feedback_message("Too High") == "📉 Go LOWER!"

def test_difficulty_ranges_are_correct():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_reset_game_state_clears_history_and_resets_attempts_and_score():
    state = {
        "status": "lost",
        "attempts": 5,
        "history": [10, 20, 30],
        "score": 75,
        "secret": 42,
    }

    reset_game_state(state, "Normal", forced_secret=77)

    assert state["status"] == "playing"
    assert state["attempts"] == 1
    assert state["history"] == []
    assert state["score"] == 0
    assert state["secret"] == 77


def test_reset_game_state_after_win_or_loss_allows_new_round():
    state = {
        "status": "won",
        "attempts": 8,
        "history": [5, 12, 25],
        "score": 200,
        "secret": 99,
    }
    reset_game_state(state, "Hard", forced_secret=15)

    assert state["status"] == "playing"
    assert state["attempts"] == 1
    assert state["history"] == []
    assert state["score"] == 0
    assert state["secret"] == 15


def test_reset_game_state_changes_secret_for_new_game():
    state = {
        "status": "playing",
        "attempts": 2,
        "history": [10],
        "score": 10,
        "secret": 1,
    }
    reset_game_state(state, "Easy", forced_secret=5)

    assert state["secret"] == 5
