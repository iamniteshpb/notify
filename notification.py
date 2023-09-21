import streamlit as st
from twilio.rest import Client

# Twilio Account SID and Auth Token
TWILIO_SID = 'ACab9bf9c7f5dbd81de1c2c5eecc7ccf6a'
TWILIO_AUTH_TOKEN = 'a8038f463b0057cf9f39592e9b4966bc'

# Streamlit UI
st.title("Absent Student ")

# Input fields for student information
student_name = st.text_input("Student Name")
parent_phone = st.text_input("Parent's Phone Number")

# Button to send SMS notification
if st.button("Send SMS Notification"):
    if parent_phone:
        # Send SMS notification
        message = f"Dear parent/guardian,\n\n{student_name} was absent from school today. Please contact the school for more information."
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_='+19513092137',
            to=parent_phone
        )
        st.success("SMS notification sent successfully!")
    else:
        st.error("Please enter a valid phone number.")
