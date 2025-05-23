import streamlit as st
import re
import random
import string

st.title("🔐 Password Strength Metre")

# Password input field
password = st.text_input("", type="password")

score = 0
weak_password = ["password123", "012345678","12345678", 
    "password", "qwertyui", "1234567a", "abcdefgh", "password321",
    "letmein12", "welcome1", "iloveyou", "1234abcd", "qwerty12",
    "sunshine", "monkey12", "1234abcd", "11111111", "password1", 
    "qwertyui", "1111111a", "1q2w3e4r", "abc12345", "123qwerty", 
    "qwerty88", "password2", "qwerty11", "asdfghjk", "123abcde"]

# strength metre
if password == "":
        strength_metre = ""

if (re.search(r"[a-z]",password) and re.search(r"[A-Z]",password)):
        score += 1

if re.search(r"[0-9]",password):
        score += 1

if re.search(r"[!@#$%^&*]",password):
        score += 1

if len(password) >= 8 :
        score += 1

if password in weak_password:
    strength_metre = "🔴 Very weak"
elif score == 1:
    strength_metre = "🟥 Weak"
elif score == 2:
    strength_metre = "🟧 Fair"
elif score == 3:
    strength_metre = "🟨 Good"
elif score == 4:
    strength_metre = "🟩 Strong"

st.markdown(f"<p style='font-size: 14px; color: gray; margin-top: -10px;'>{strength_metre}</p>",unsafe_allow_html=True)

# check Password 
if password == "":
        st.info("Enter Your Password")
elif password in weak_password:
        st.error("You can't proceed with this Password")
elif len(password) < 8:
        st.warning("Password should be at least 8 characters long.")
elif not(re.search(r"[a-z]",password) and re.search(r"[A-Z]",password)):
        st.warning('Include both "UPPERCASE" & "lowercase" letters')
elif not(re.search(r"\d", password)):
        st.warning("Add at least one number (0-9).")
elif not(re.search(r"[!@#$%^&*]", password)):
        st.warning("Include at least one special character (!@#$%^&*)")
else:
       st.success("Great! Your password is secure.")

col1 , col2 = st.columns([3.5, 1])

# Password genarator
with col1:
        if st.button("Generate Strong Password", key="generator"):
          characters = string.ascii_letters + string.digits + "!@#$%^&*"
          strong_password = ''.join(random.choices(characters, k=12))
          st.code(strong_password, language='')

with col2:
       if strength_metre == "🟩 Strong":
          if st.button("Done"):
                st.success("Success!")

