import streamlit as st
import requests
import pandas as pd

# Set up Streamlit page title
st.title("Seating Arrangement Generator")

# Upload Files
st.header("Step 1: Upload Required Files")
students_file = st.file_uploader("Upload Students File (CSV)", type=["csv"])
schedule_file = st.file_uploader("Upload Schedule File (CSV)", type=["csv"])
rooms_file = st.file_uploader("Upload Rooms File (CSV)", type=["csv"])
student_roll_map_file = st.file_uploader("Upload Student-Roll Mapping File (CSV)", type=["csv"])

# Form Inputs for Buffer and Seating Option
st.header("Step 2: Enter Configuration")
buffer = st.number_input("Enter Buffer Seats (default: 5)", min_value=0, max_value=10, value=5)
seating_option = st.selectbox("Select Seating Arrangement Option", ["dense", "sparse"])

# Button to Submit the Form
if st.button("Submit"):
    if students_file and schedule_file and rooms_file and student_roll_map_file:
        # Prepare form data to send in the POST request
        form_data = {
            'buffer': buffer,
            'seating': seating_option
        }
        
        # Prepare files to send in the POST request
        files = {
            'students_file': students_file,
            'schedule_file': schedule_file,
            'rooms_file': rooms_file,
            'student_roll_map': student_roll_map_file
        }

        # Send POST request to Flask server
        response = requests.post("http://127.0.0.1:5000/submit", data=form_data, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            # Display success message and provide download link
            st.success("Seating arrangement generated successfully!")
            st.write("You can download the generated files below:")

            # Assuming Flask server sends back the CSV file URL
            output_csv_url = "http://127.0.0.1:5000/download/seating_arrangement_final.csv"
            st.markdown(f"[Download Seating Arrangement CSV](output_csv_url)")

        else:
            st.error("There was an issue generating the seating arrangement.")
    else:
        st.error("Please upload all required files before submitting.")
