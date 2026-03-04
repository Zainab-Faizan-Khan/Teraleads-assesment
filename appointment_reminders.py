import json

# Hardcoded JSON data simulating appointment objects
appointment_json = """
[
    {
        "patient_name": "Alice Smith",
        "appointment_date": "March 15th",
        "appointment_time": "10:30 AM",
        "service": "Dental Cleaning"
    },
    {
        "patient_name": "Bob Johnson",
        "appointment_date": "March 16th",
        "appointment_time": "2:00 PM",
        "service": "General Consultation"
    }
]
"""

def generate_reminder(appointment_data_str):
    """
    Parses a JSON string of appointment data and generates TTS-ready messages.
    """
    try:
        # Step 1: Parse the JSON string into a Python list
        appointments = json.loads(appointment_data_str)
        
        reminders = []
        for appt in appointments:
            # Step 2: Generate messages with tone and pause annotations for TTS processing
            message = (
                f"<friendly tone> Hello {appt['patient_name']}! <pause> "
                f"This is a friendly reminder for your {appt['service']} "
                f"on {appt['appointment_date']} at {appt['appointment_time']}. <pause> "
                f"We look forward to seeing you soon! </friendly tone>"
            )
            reminders.append(message)
        
        return reminders

    except json.JSONDecodeError as e:
        return [f"Error: Failed to parse JSON. {str(e)}"]
    except KeyError as e:
        # Common Issue: Accessing a missing key (e.g., mistyping 'patient_name' as 'client_name')
        # Fix: Ensure the key exists or use .get() for safer access.
        # One-line fix: patient = appt.get('patient_name', 'Valued Patient')
        return [f"Error: Data key {str(e)} is missing in the JSON."]

# --- Integration Paragraph ---
# This script would interface with a production TTS system (like Amazon Polly or Google Cloud TTS) 
# by sending the generated 'message' strings to the service's API endpoint. 
# The tone annotations (e.g., <friendly tone>) are often supported as SSML (Speech Synthesis Markup Language) tags, 
# allowing the system to adjust prosody, pitch, and timing based on the script's guidance.

# --- Debugging Scenario (Simulated) ---
# Common issue: Malformed JSON (e.g., trailing comma or unquoted keys).
# If 'appointment_json' had a trailing comma, json.loads() would raise a JSONDecodeError.
# Fix: Ensure JSON follows strict syntax or use a validator tools before parsing.

if __name__ == "__main__":
    # Generate and print the reminders
    tts_reminders = generate_reminder(appointment_json)
    
    print("--- Generated TTS Messages ---")
    for idx, reminder in enumerate(tts_reminders, 1):
        print(f"Message {idx}:\n{reminder}\n")
