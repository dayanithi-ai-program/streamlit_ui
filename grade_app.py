import streamlit as st


# Grading function
def calculate_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Create student list in session state
if "students" not in st.session_state:
    st.session_state.students = []


st.title("Student Grade Application")

st.write("Add student marks and view the class performance.")


# Student form
with st.form("student_form"):

    name = st.text_input("Student Name")

    mark = st.number_input(
        "Mark",
        min_value=0,
        max_value=100,
        step=1
    )

    submitted = st.form_submit_button("Add Student")

    if submitted:

        if name.strip() == "": #basically removes the space in front and back of the string, here after removing the space if nothig is left 
            st.error("Please enter the student name.")

        else:
            student = {
                "name": name,
                "mark": mark,
                "grade": calculate_grade(mark)
            }

            st.session_state.students.append(student)

            st.success(f"{name} added successfully!")


# Display students
st.subheader("Students")

if st.session_state.students:

    st.table(st.session_state.students)

    marks = [
        student["mark"]
        for student in st.session_state.students
    ]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Metrics
    col1, col2, col3 = st.columns(3)

    col1.metric("Class Average", f"{average:.2f}")
    col2.metric("Highest Mark", highest)
    col3.metric("Lowest Mark", lowest)

else:

    st.info("No students added yet.")