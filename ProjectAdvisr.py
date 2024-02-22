import requests
from bs4 import BeautifulSoup
import time

# SMS gateway API credentials
api_key = "x"
api_secret = "x"
sms_from = "x"
sms_to = "x"
message = "Website content changed!"

# URL of the webpage to monitor
url = "https://www.news.google.com/news"

# Function to fetch webpage content
def fetch_content(url):
    response = requests.get(url)
    return response.text

# Function to extract relevant information from HTML content
def extract_info(html_content):
    # Use BeautifulSoup to parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract relevant information here
    # For example:
    # info = soup.find('div', class_='info').text
    info = soup.find('div', class_='iNL53').text
    return info

# Function to send SMS notification
def send_sms(message):
    api_url = "https://api.sms-gateway-service.com/send"
    payload = {
        "api_key": api_key,
        "api_secret": api_secret,
        "from": sms_from,
        "to": sms_to,
        "text": message
    }
    response = requests.post(api_url, data=payload)
    if response.status_code == 200:
        print("SMS notification sent successfully!")
    else:
        print("Failed to send SMS notification:", response.text)

# Initial state
initial_state = extract_info(fetch_content(url))

# Main loop
while True:
    # Fetch current content
    current_content = extract_info(fetch_content(url))
    
    # Compare with initial state
    if current_content != initial_state:
        message = "Website content changed!\nCheck it out: " + url
        send_sms(message)
        # Update initial state
        initial_state = current_content
    
    # Wait for some time before checking again
    time.sleep(60)  # Check every 60 seconds