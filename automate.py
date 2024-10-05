import pywhatkit
import pandas as pd
import time

# Load phone numbers from CSV
data = pd.read_csv('contacts.csv')
numbers = data['numbers'].tolist()

# Message to send
message = '''
Heyy,
Welcome to the KJDG Community! 🎉

You've made a great choice, and we’re excited to have you onboard!

Join the link for updates and all the action: 
https://chat.whatsapp.com/K0oM1EztlrQAKP2bB4UAZR

'''

# Send message to each number with a delay
for number in numbers:
    try:
        print(f'Sending message to {number}...')
        pywhatkit.sendwhatmsg_instantly(f'+{number}', message)  # Add '+' if needed
        print(f'Message sent to {number}')
        
        # Add a delay to avoid being flagged for spam (adjust as needed)
        time.sleep(5)  # Delay of 10 seconds between each message
    except Exception as e:
        print(f'Failed to send message to {number}. Error: {e}')
