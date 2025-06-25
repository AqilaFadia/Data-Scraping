import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv()

SPREADSHEET_NAME = os.getenv("SPREADSHEET_NAME")
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")


def authorize_gsheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    return client

def save_data_to_sheet(data: list[dict]):
    client = authorize_gsheet()
    sheet = client.open(SPREADSHEET_NAME).worksheet(WORKSHEET_NAME)

    # OPTIONAL: Clear old data first
    sheet.clear()

    # Set header
    headers = ["title", "username", "viewers","timestamp"]
    sheet.append_row(headers)

    # Append data rows
    for row in data:
        sheet.append_row([row["title"], row["username"], row["viewers"], row["timestamp"]])