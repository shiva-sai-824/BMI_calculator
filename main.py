import streamlit as st
st.set_page_config(page_title="BMI Calculator",
                   page_icon=":tada", layout="wide")

st.title("BMI Calculator")
st.write("By Shiva Sai")
st.write("---")

st.text_input("Enter Your Name")

st.radio(label="Gender", options=("Male", "Female", "Prefer not to say"))

st.number_input("Enter your Age:", value=False)

st.text_area("Address:")
st.write("Hobbies:")
st.checkbox("Music")
st.checkbox("Playing")
st.checkbox("Singing")
st.checkbox("Coding")
weight = st.number_input("Enter your weight in (Kg):", step=1, value=False)
height = st.number_input("Enter your height in (cm):", step=1, value=True)

BMI = weight/(height)**2
BMI = BMI*10000

st.success(f"Your BMI values is {BMI} kg/m^2")
if BMI >= 18.5 and BMI <= 24.9:
    st.success(f"You are Healthy 🫡")
else:
    st.warning(f"You're Unhealthy 🥺")
