import streamlit as st

st.set_page_config(
    page_icon="📈", page_title="Growth Mindset AI", layout="centered")
st.title("📈Growth Mindset AI")

st.header("🚀Welcome to your success journey")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This Al-powered app helps you build a growth mindset with reflection, challenges, and achievements!")

# Quote Section
st.header("💡Today's Growth Mindset Quote")
st.write("*Success is not final, failure is not fatal: it is the courage to continue that counts*.Winston Churchill")
st.header("🧿 What's your challenge today")
user_input = st.text_input("Describe a challenge you are facing:")

# condition
if user_input:
    st.success(
        f"You're facing: {user_input}. Keep pushing forward towards your goal!🎯")
else:
    st.warning("Tell us about your challenge to get started!")

# reflexing
st.header("🔃Reflect on your learning!")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨Great Insight! Your Reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

# achievements
st.header("🥇Celebrate your wins!")
achievement = st.text_input("Share something you've recently accomplished:")
if achievement:
    st.success(f"🎆Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now🎉")


# footer
st.write("---")
st.write("🚀Keep believing in yourself. Growth is a journey, not a destination!🎊")
st.write("Created by 😎Hafiz Siddiqui")
