from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

# Load credentials from JSON file
credentials = service_account.Credentials.from_service_account_file(
    'C:\Users\muham\OneDrive\Desktop\Mammu Folder\programming\ARK',
    scopes=['https://www.googleapis.com/auth/calendar.json()']
)

# Create a calendar service
service = build('calendar', 'v3', credentials=credentials)


