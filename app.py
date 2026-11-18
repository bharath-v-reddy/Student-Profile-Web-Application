
import streamlit as st

st.set_page_config(
    page_title="Student Profile Web Application",
    layout="centered"
)

st.title("Student Profile Application")
st.caption("Enter your details to create your student profile.")

# Student Details
name = st.text_input("Student Name", placeholder="Enter Your Name")

usn = st.text_input("USN / Roll No.", placeholder="Enter Your USN")

dept = st.text_input("Department", placeholder="Enter Your Department")

year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# Button
btn = st.button("View My Profile")

if btn:
    if name and usn and dept:
        st.success("Profile Created Successfully!")

        st.subheader("🎓 Student Profile Details")

        st.write("**Student Name:**", name)
        st.write("**USN / Roll No.:**", usn)
        st.write("**Department:**", dept)
        st.write("**Current Year:**", year)

    else:
        st.warning("Please fill in all the details.")
