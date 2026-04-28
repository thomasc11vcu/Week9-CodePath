import streamlit as st
from logic_utils import generate_secret, check_guess

# Initialize secret number once
if "secret" not in st.session_state:
    st.session_state.secret = generate_secret()

st.title("🎮 Game Glitch Investigator: The Impossible Guesser")

st.write("Try to guess the secret number between 1 and 100!")

guess = st.number_input("Your Guess:", min_value=1, max_value=100, step=1)

if st.button("Submit"):
    verdict = check_guess(st.session_state.secret, guess)
    st.write(verdict["message"])
    if verdict["win"]:
        st.success("🎉 You won! 🎉")
    else:
        st.info("Try again!")