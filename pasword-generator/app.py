import streamlit as st
import re

st.set_page_config(page_title="Pasword strength Checker",page_icon="🔒")

st.title("🔒Pasword Strength Checker")

st.markdown("""
## Welcome to the uiltimate Paswoed strength checker!🤚
use this simple tool to check the strength of your pasword and get suggestion on how to makit stronger.
        we will give you helpful tips to create a **Strong Pasword** 🔒""")

password=st.text_input("Enter Your password",type="password")

feedback =[]

score=0

if password:
    if len(password)>= 8:
        score += 1
    else:
        feedback.append( "❌Password should be at least 8 characters long.")
    
    if re.search(r'[A-Z]',password) and re.search('[a-z]',password):
        score += 1
    
    else:
        feedback.append("❌password should contain both upper and lower case character")

    if re.search(r'\d',password):
        score += 1
    else:
        feedback.append("❌password should contain atleat one digit.")

    if re.search(r'[!#@*&$]',password):
       score += 1
    else:
        feedback.append("❌password should contain atleat one special character(!#@*&$).")

    if score == 4:
        feedback.append("✅ Your Password is strong!🎉")

    elif score == 3:
        feedback.append("🟡Your Password is medium strength.It could be stronger.")

    else:
        feedback.append("🔴Your Password is weak.Please make it stronger.")
    
    if feedback:
        st.markdown("## Improvment Suggestions")
        for tip in feedback:
            st.write(tip)

else:
    st.info("Please Enter Your Password to get started")