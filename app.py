import streamlit as st
st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: white;
}
.block-container {
    max-width: 950px;
    padding-top: 2rem;
}

h1, h2, h3, p, label {
    color: white !important;
}

div.stButton > button {
    background-color: white;
    color: black;
    border-radius: 40px;
    padding: 10px 30px;
    border: none;
    font-size: 18px;
}

div.stButton > button:hover {
    background-color: #dddddd;
    color: black;
}

[data-testid="stForm"] {
    border: 1px solid #333333;
    border-radius: 20px;
    padding: 25px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 Student Profile Application")

st.subheader("Developed by Student Name")

st.info("Fill in your details and click View My Profile.")

with st.form("student_form"):

    name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )

    usn = st.text_input(
        "USN / Roll Number",
        placeholder="Enter roll number"
    )

    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE", "ME", "Civil"]
    )

    year = st.radio(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    submit = st.form_submit_button("View My Profile")

if submit:

    if name.strip() == "" or usn.strip() == "":
        st.warning("Please enter your name and roll number.")

    else:
        st.success("Student Profile Created Successfully!")

        st.header("Student Profile")

        st.write("**Student Name:**", name)
        st.write("**USN / Roll Number:**", usn)
        st.write("**Department:**", department)
        st.write("**Current Year:**", year)

        st.info("Thank you for using Student Profile Application!")
