import random

def generate_secret() -> int:
    """Return a random number between 1 and 100."""
    return random.randint(1, 100)

def check_guess(secret: int, guess: int) -> dict:
    """Return a message based on the guess."""
    if guess == secret:
        return {"message": "Correct!", "win": True}
    elif guess < secret:
        return {"message": "Higher!", "win": False}
    else:
        return {"message": "Lower!", "win": False}